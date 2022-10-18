import re
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque, Counter
from bs4 import BeautifulSoup
import difflib
import streamlit as st

DEBUG = True


def main_scrap(list_of_links):
    # List of links from csv
    print('1&&&&&&&<<<<<<<<<&&&&')
    queue_of_link = deque(list_of_links)
    result = {}
    while queue_of_link:
        print('1&&&&&&&&&&&')
        link = queue_of_link.popleft()
        emails = process_links(link)

        print(f"emails {emails}")
        for email in emails:
            result[link] = list(email.keys())
            st.write(email)
        print(f"result {result}")

    yield result


def process_links(starting_url):
    # a queue of urls to be crawled
    unprocessed_urls = deque([starting_url])
    # set of already crawled urls for email
    processed_urls = set()
    # a set of fetched emails
    emails = {}
    # process urls one by one from unprocessed_url queue until queue is empty

    # counter to stop diving in anchor website at some point
    anchors_counter = 0
    while len(unprocessed_urls) and anchors_counter < 10:

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
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            # ignore pages with errors and continue with next url
            continue

        emails = get_emails(response.text, emails)

        if DEBUG:
            print(f"emails 11 {emails}")

        if sum(emails.values()) > 10:
            yield emails

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
    yield emails


def get_emails(website, emails_list):
    # extract all email addresses and add them into the resulting set
    # You may edit the regular expression as per your requirement
    new_emails = Counter(re.findall(r"[a-z\.\-+_]+@[a-z\.\-+_]+\.[a-z]+", website, re.I))
    if DEBUG:
        print(new_emails, "emails_list  === ", emails_list)
    emails_list.update(new_emails)
    return emails_list
