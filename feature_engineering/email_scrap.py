import re

import pandas as pd
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque, Counter
from bs4 import BeautifulSoup
import difflib
import streamlit as st

DEBUG = False


def main_scrap(list_of_links):
    # List of links from csv
    queue_of_link = deque(list_of_links)
    result = pd.DataFrame([], columns=['link', 'email'])

    while queue_of_link:
        link = queue_of_link.popleft()
        emails = process_links(link)
        if not emails:
            emails['None'] = 0
        row = {'link': link, 'email': list(emails.keys())}
        result.append(row,  ignore_index=True)
        st.dataframe(row, )
        print(f"result {result}")

    return result


def process_links(starting_url):
    # a queue of urls to be crawled
    unprocessed_urls = deque([starting_url])
    # set of already crawled urls for email
    processed_urls = set()
    # a set of fetched emails
    emails = {}
    # process urls one by one from unprocessed_url queue until queue is empty

    print(f">>> starting_url {starting_url}")

    # counter to stop diving in anchor website at some point
    anchors_counter = 0
    while len(unprocessed_urls) and anchors_counter < 10:
        print(f">>> test enter {starting_url} {anchors_counter}, {unprocessed_urls} ")

        # move next url from the queue to the set of processed urls
        url = unprocessed_urls.popleft()

        processed_urls.add(url)

        # extract base url to resolve relative links
        parts = urlsplit(url)
        base_url = "{0.scheme}://{0.netloc}".format(parts)
        path = url[:url.rfind('/') + 1] if '/' in parts.path else url

        # get url's content
        if DEBUG:
            print("Crawling URL %s" % url)
        try:
            response = requests.get(url, timeout=10)
            anchors_counter += 1
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.Timeout,
                Exception) as err:
            # ignore pages with errors and continue with next url
            print(f"ignoring {url} pages with errors and continue with next url -- {err}")
            continue

        emails = get_emails(response.text, emails)

        if DEBUG:
            print(f"emails 11 {emails}")

        if sum(emails.values()) > 10:
            print(f">>>   returnnn  {emails}")
            return emails

        # create a beutiful soup for the html document
        soup = BeautifulSoup(response.text, 'lxml')

        # Once this document is parsed and processed, now find and process all the anchors i.e. linked urls in this
        # document
        for anchor in soup.find_all("a"):
            # extract link url from the anchor
            link = anchor.attrs["href"] if "href" in anchor.attrs else ''
            # resolve relative links (starting with /)
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            # add the new url to the queue if it was not in unprocessed list nor in processed list yet
            if not link in unprocessed_urls and not link in processed_urls:
                unprocessed_urls.append(link)

        unprocessed_urls = sorted(unprocessed_urls,
                                  key=lambda z: difflib.SequenceMatcher(None, z, "mail contact customer about").ratio(),
                                  reverse=True)
        if DEBUG:
            print('unprocessed_urls ===', unprocessed_urls)
        unprocessed_urls = deque(unprocessed_urls)
    return emails


def get_emails(website, emails_list):
    # extract all email addresses and add them into the resulting set
    # You may edit the regular expression as per your requirement
    new_emails = Counter(re.findall(r"[a-z\.\-+_]+@[a-z\.\-+_]+\.[a-z]+", website, re.I))
    if DEBUG:
        print(new_emails, "emails_list  === ", emails_list)
    emails_list.update(new_emails)
    return emails_list


def form_callback():
    st.write(st.session_state.email_list)