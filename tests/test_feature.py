import pytest

from feature_engineering.email_scrap import get_emails


def test_email_grab_is_correct():
    # GIVE \
    HTML = '<div class="container-indent"> \
      <div class="container"> \
        <meta charset="utf-8"> \
    <h4 class="tt-collapse-title">CONTACT US</h4> \
    <div class="tt-collapse-content"> \
    <p><span>PHONE:</span><span>&nbsp;</span>(888) 912-6529</p> \
    <p><span>HOURS:</span><span>&nbsp;</span>Monday - Friday from 9 AM to 5 PM</p> \
    <p><span>E-MAIL:</span><span>&nbsp;</span><a href="mailto:orders@streetwearofficial.com">orders@streetwearofficial.com</a></p> \
    </div> \
      </div> \
    </div> '
    expected = {"orders@streetwearofficial.com" : 2}
    # WHE \
    actual = get_emails(HTML, {})
    # THE \
    assert actual == expected



def test_email_grab_multiple_is_correct():
    # GIVE \
    HTML = '<body class="pagepage loaded"><div id="shopify-section-show-helper" class="shopify-section"></div><div id="shopify-section-header-template" class="shopify-section"><header class="desctop-menu-large small-header"><nav class="panel-menu mobile-main-menu"><div class="mmpanels"><div class="mmpanel mmopened mmcurrent" id="mm0"><ul><li class="mm-close-parent"><a href="#close" data-target="#close" class="mm-close">Close</a></li><li> \
      <a href="#mm1" data-target="#mm1" class="mm-next-level">New Arrivals</a></li><li> \
          <a href="/collections/best-sellers">Best Sellers</a></li><li> \
          <a href="#mm4" data-target="#mm4" class="mm-next-level">Mens</a></li><li> \
          <a href="#mm9" data-target="#mm9" class="mm-next-level">Womens</a></li><li> \
          <a href="#mm14" data-target="#mm14" class="mm-next-level">Kids</a></li><li> \
          <a href="#mm15" data-target="#mm15" class="mm-next-level">Brands</a></li><li> \
          <a href="#mm22" data-target="#mm22" class="mm-next-level">Sale</a></li><li id="entrypoint-objects"></li></ul></div><div class="mmpanel mmhidden" id="mm1"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/fresh-arrivals" class="mm-original-link">New Arrivals</a></li><li> \
              <a href="#mm2" data-target="#mm2" class="mm-next-level">New Arrivals</a></li><li> \
              <a href="#mm3" data-target="#mm3" class="mm-next-level">Latest Brands</a></li></ul></div><div class="mmpanel mmhidden" id="mm2"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/fresh-arrivals" class="mm-original-link">New Arrivals</a></li><li><a href="/collections/latest-arrivals">New This Week</a></li><li><a href="/collections/supreme-new-arrivals">New Supreme Arrivals</a></li></ul></div><div class="mmpanel mmhidden" id="mm3"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="#" class="mm-original-link">Latest Brands</a></li><li><a href="/collections/father-forgive-me">Father Forgive Me</a></li><li><a href="/collections/reason-brand">Reason</a></li><li><a href="/collections/rodman-brand">Rodman Brand</a></li><li><a href="/collections/shhh-brand">SHHH BRAND</a></li><li><a href="/collections/wave-club">Wave Club</a></li><li><a href="/collections/hasta-muerte">Hastamuerte</a></li><li><a href="/collections/never-broke-again-nba-youngboy">Never Broke Again</a></li><li><a href="/collections/retro-kings">Retro Kings</a></li></ul></div><div class="mmpanel mmhidden" id="mm4"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/mens" class="mm-original-link">Mens</a></li><li> \
              <a href="#mm5" data-target="#mm5" class="mm-next-level">Mens Tops</a></li><li> \
              <a href="#mm6" data-target="#mm6" class="mm-next-level">Mens Outerwear</a></li><li> \
              <a href="#mm7" data-target="#mm7" class="mm-next-level">Mens Bottoms</a></li><li> \
              <a href="#mm8" data-target="#mm8" class="mm-next-level">Accessories</a></li></ul></div><div class="mmpanel mmhidden" id="mm5"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="#" class="mm-original-link">Mens Tops</a></li><li><a href="/collections/graphic-t-shirts">Mens Graphic Tees</a></li><li><a href="/collections/big-and-tall-tees">Mens Big and Tall Tees</a></li></ul></div><div class="mmpanel mmhidden" id="mm6"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/outerwear" class="mm-original-link">Mens Outerwear</a></li><li><a href="/collections/hoodies">Mens Hoodies</a></li><li><a href="/collections/big-and-tall-hoodies">Mens Big and Tall Hoodies</a></li></ul></div><div class="mmpanel mmhidden" id="mm7"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/bottoms" class="mm-original-link">Mens Bottoms</a></li><li><a href="/collections/mens-denim">Mens Denim</a></li><li><a href="/collections/mens-shorts">Mens Shorts</a></li><li><a href="/collections/mens-joggers">Mens Joggers</a></li></ul></div><div class="mmpanel mmhidden" id="mm8"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/accessories" class="mm-original-link">Accessories</a></li><li><a href="/collections/headwear">Headwear</a></li><li><a href="/collections/footwear">Footwear</a></li><li><a href="/collections/jewelry">Jewelry</a></li><li><a href="/collections/socks">Socks</a></li><li><a href="/collections/belts">Belts</a></li><li><a href="/collections/bags">Bags</a></li><li><a href="/collections/mens-undergarments">Undergarments</a></li><li><a href="/collections/home">Lifestyle</a></li></ul></div><div class="mmpanel mmhidden" id="mm9"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/womens" class="mm-original-link">Womens</a></li><li> \
              <a href="#mm10" data-target="#mm10" class="mm-next-level">Womens Tops</a></li><li> \
              <a href="#mm11" data-target="#mm11" class="mm-next-level">Womens Outerwear</a></li><li> \
              <a href="#mm12" data-target="#mm12" class="mm-next-level">Womens Bottoms</a></li><li> \
              <a href="#mm13" data-target="#mm13" class="mm-next-level">Womens Accessories</a></li></ul></div><div class="mmpanel mmhidden" id="mm10"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="#" class="mm-original-link">Womens Tops</a></li><li><a href="/collections/womens-t-shirts">Womens Graphic Tees</a></li><li><a href="/collections/womens-crop-tops">Womens Crop Tops</a></li></ul></div><div class="mmpanel mmhidden" id="mm11"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="#" class="mm-original-link">Womens Outerwear</a></li><li><a href="/collections/hoodies">Womens Hoodies</a></li><li><a href="/collections/womens-crop-hoodies">Womens Crop Hoodies</a></li></ul></div><div class="mmpanel mmhidden" id="mm12"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/womens-bottoms" class="mm-original-link">Womens Bottoms</a></li><li><a href="/collections/womens-shorts">Womens Shorts</a></li><li><a href="/collections/womens-joggers">Womens Joggers</a></li></ul></div><div class="mmpanel mmhidden" id="mm13"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="#" class="mm-original-link">Womens Accessories</a></li><li><a href="/collections/headwear">Headwear</a></li><li><a href="/collections/jewelry">Jewelry</a></li><li><a href="/collections/socks">Socks</a></li><li><a href="/collections/belts">Belts</a></li><li><a href="/collections/womens-undergarment">Womens Undergarments</a></li><li><a href="/collections/home">Lifestyle</a></li></ul></div><div class="mmpanel mmhidden" id="mm14"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/kids-1" class="mm-original-link">Kids</a></li><li> \
              <a href="/collections/kids-bottoms">Kids Bottoms</a></li><li> \
              <a href="/collections/kids-tops">Kids Tops</a></li></ul></div><div class="mmpanel mmhidden" id="mm15"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="#" class="mm-original-link">Brands</a></li><li> \
              <a href="#mm16" data-target="#mm16" class="mm-next-level">Popular Brands</a></li><li> \
              <a href="#mm18" data-target="#mm18" class="mm-next-level">Hype Brands</a></li><li> \
              <a href="#mm20" data-target="#mm20" class="mm-next-level">ALL BRANDS</a></li></ul></div><div class="mmpanel mmhidden" id="mm16"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="#" class="mm-original-link">Popular Brands</a></li><li><a href="#mm17" data-target="#mm17" class="mm-next-level">Supreme</a></li><li><a href="/collections/hasta-muerte">Hastamuerte</a></li><li><a href="/collections/streetwear-official">Streetwear Official</a></li><li><a href="/collections/retro-kings">Retro Kings</a></li><li><a href="/collections/never-broke-again-nba-youngboy">Never Broke Again</a></li><li><a href="/collections/divine-felons">Divine Felons</a></li><li><a href="/collections/vlone">VLONE</a></li><li><a href="/collections/reason-brand">Reason</a></li></ul></div><div class="mmpanel mmhidden" id="mm17"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/supreme-new-arrivals" class="mm-original-link">Supreme</a></li><li><a href="/collections/supreme-new-arrivals">Supreme - New Arrivals</a></li><li><a href="/collections/supreme-top-ten-items-of-the-week">Supreme - Top 10 sellers</a></li><li><a href="/collections/supreme-t-shirts">Supreme - T-Shirts</a></li><li><a href="/collections/supreme-outerwear">Supreme - Outerwear </a></li><li><a href="/collections/supreme-headwear">Supreme - Headwear</a></li><li><a href="/collections/supreme-accessories">Supreme - Accessories</a></li></ul></div><div class="mmpanel mmhidden" id="mm18"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="#" class="mm-original-link">Hype Brands</a></li><li><a href="#mm19" data-target="#mm19" class="mm-next-level">Supreme</a></li><li><a href="/collections/a-bathing-ape-bape">BAPE</a></li><li><a href="/collections/ftp">FTP</a></li><li><a href="/collections/palace-1">Palace</a></li><li><a href="/collections/kaws">KAWS</a></li><li><a href="/collections/hype-streetwear">ALL </a></li></ul></div><div class="mmpanel mmhidden" id="mm19"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/supreme-new-arrivals" class="mm-original-link">Supreme</a></li><li><a href="/collections/supreme-new-arrivals">Supreme - New Arrivals</a></li><li><a href="/collections/supreme-top-ten-items-of-the-week">Supreme - Top 10 sellers</a></li><li><a href="/collections/supreme-t-shirts">Supreme - T-Shirts</a></li><li><a href="/collections/supreme-outerwear">Supreme - Outerwear </a></li><li><a href="/collections/supreme-headwear">Supreme - Headwear</a></li><li><a href="/collections/supreme-accessories">Supreme - Accessories</a></li></ul></div><div class="mmpanel mmhidden" id="mm20"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/all" class="mm-original-link">ALL BRANDS</a></li><li><a href="/collections/hasta-muerte">Hastamuerte</a></li><li><a href="/collections/streetwear-official">Streetwear Official</a></li><li><a href="/collections/retro-kings">Retro Kings</a></li><li><a href="/collections/never-broke-again-nba-youngboy">Never Broke Again</a></li><li><a href="/collections/27-club">27 Club</a></li><li><a href="/collections/divine-felons">Divine Felons</a></li><li><a href="/collections/thrt-denim">THRT Denim</a></li><li><a href="/collections/no-cap">NO CAP</a></li><li><a href="/collections/hustlers-only">Hustlers Only</a></li><li><a href="/collections/just-hustle">Just Hustle</a></li><li><a href="/collections/popular-demand">Popular Demand</a></li><li><a href="/collections/love">LOVE</a></li><li><a href="#mm21" data-target="#mm21" class="mm-next-level">Supreme</a></li><li><a href="/collections/odd-sox">ODD SOX</a></li><li><a href="/collections/hk-stuntwear">HK Stuntwear</a></li><li><a href="/collections/legendary-minds">Legendary Minds</a></li><li><a href="/collections/reason-brand">Reason</a></li></ul></div><div class="mmpanel mmhidden" id="mm21"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/supreme-new-arrivals" class="mm-original-link">Supreme</a></li><li><a href="/collections/supreme-new-arrivals">Supreme - New Arrivals</a></li><li><a href="/collections/supreme-top-ten-items-of-the-week">Supreme - Top 10 sellers</a></li><li><a href="/collections/supreme-t-shirts">Supreme - T-Shirts</a></li><li><a href="/collections/supreme-outerwear">Supreme - Outerwear </a></li><li><a href="/collections/supreme-headwear">Supreme - Headwear</a></li><li><a href="/collections/supreme-accessories">Supreme - Accessories</a></li></ul></div><div class="mmpanel mmhidden" id="mm22"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/clearance" class="mm-original-link">Sale</a></li><li> \
              <a href="#mm23" data-target="#mm23" class="mm-next-level">Clearance</a></li><li> \
              <a href="#mm24" data-target="#mm24" class="mm-next-level">Mystery</a></li></ul></div><div class="mmpanel mmhidden" id="mm23"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="/collections/clearance" class="mm-original-link">Clearance</a></li><li><a href="/collections/sale-headwear">Headwear</a></li><li><a href="/collections/sale-shirts">Shirts</a></li><li><a href="/collections/sale-outerwear">Outerwear</a></li><li><a href="/collections/sale-bottoms">Bottoms</a></li><li><a href="/collections/sale-kids">Kids</a></li><li><a href="/collections/sale-womens">Womens</a></li><li><a href="/collections/sale-jewelry">Jewelry</a></li><li><a href="/collections/sale-bags">Bags</a></li><li><a href="/collections/sale-footwear">Footwear</a></li></ul></div><div class="mmpanel mmhidden" id="mm24"><ul><li><a href="#" data-target="#" class="mm-prev-level">Back</a></li><li><a href="#" class="mm-original-link">Mystery</a></li><li><a href="/collections/mystery">Mystery Items</a></li></ul></div></div></nav><!-- tt-top-panel --> \
    <div class="tt-top-panel"> \
      <div class="container"> \
        <div class="tt-row" style="padding-top:17px;min-height:5px;"> \
          <div class="tt-description" style="font-size:15px;line-height:22px;font-weight:400;"> \
            SITEWIDE SALE: USE CODE: 40 AT CHECK OUT FOR 40% OFF! \
          </div> \
          <button class="tt-btn-close" style="top:-2px;"></button> \
        </div> \
      </div> \
    </div><!-- tt-mobile-header --> \
    <div class="tt-mobile-header tt-mobile-header-inline tt-mobile-header-inline-stuck"> \
      <div class="container-fluid"> \
        <div class="tt-header-row"> \
          <div class="tt-mobile-parent-menu"> \
            <div class="tt-menu-toggle mainmenumob-js" style="display: inline-block;"> \
              <svg width="17" height="15" viewBox="0 0 17 15" fill="none" xmlns="http://www.w3.org/2000/svg"> \
    <path d="M16.4023 0.292969C16.4935 0.397135 16.5651 0.507812 16.6172 0.625C16.6693 0.742188 16.6953 0.865885 16.6953 0.996094C16.6953 1.13932 16.6693 1.26953 16.6172 1.38672C16.5651 1.50391 16.4935 1.60807 16.4023 1.69922C16.2982 1.80339 16.1875 1.88151 16.0703 1.93359C15.9531 1.97266 15.8294 1.99219 15.6992 1.99219H1.69531C1.55208 1.99219 1.42188 1.97266 1.30469 1.93359C1.1875 1.88151 1.08333 1.80339 0.992188 1.69922C0.888021 1.60807 0.809896 1.50391 0.757812 1.38672C0.71875 1.26953 0.699219 1.13932 0.699219 0.996094C0.699219 0.865885 0.71875 0.742188 0.757812 0.625C0.809896 0.507812 0.888021 0.397135 0.992188 0.292969C1.08333 0.201823 1.1875 0.130208 1.30469 0.078125C1.42188 0.0260417 1.55208 0 1.69531 0H15.6992C15.8294 0 15.9531 0.0260417 16.0703 0.078125C16.1875 0.130208 16.2982 0.201823 16.4023 0.292969ZM16.4023 6.28906C16.4935 6.39323 16.5651 6.50391 16.6172 6.62109C16.6693 6.73828 16.6953 6.86198 16.6953 6.99219C16.6953 7.13542 16.6693 7.26562 16.6172 7.38281C16.5651 7.5 16.4935 7.60417 16.4023 7.69531C16.2982 7.79948 16.1875 7.8776 16.0703 7.92969C15.9531 7.98177 15.8294 8.00781 15.6992 8.00781H1.69531C1.55208 8.00781 1.42188 7.98177 1.30469 7.92969C1.1875 7.8776 1.08333 7.79948 0.992188 7.69531C0.888021 7.60417 0.809896 7.5 0.757812 7.38281C0.71875 7.26562 0.699219 7.13542 0.699219 6.99219C0.699219 6.86198 0.71875 6.73828 0.757812 6.62109C0.809896 6.50391 0.888021 6.39323 0.992188 6.28906C1.08333 6.19792 1.1875 6.1263 1.30469 6.07422C1.42188 6.02214 1.55208 5.99609 1.69531 5.99609H15.6992C15.8294 5.99609 15.9531 6.02214 16.0703 6.07422C16.1875 6.1263 16.2982 6.19792 16.4023 6.28906ZM16.4023 12.3047C16.4935 12.3958 16.5651 12.5 16.6172 12.6172C16.6693 12.7344 16.6953 12.8646 16.6953 13.0078C16.6953 13.138 16.6693 13.2617 16.6172 13.3789C16.5651 13.4961 16.4935 13.6068 16.4023 13.7109C16.2982 13.8021 16.1875 13.8737 16.0703 13.9258C15.9531 13.9779 15.8294 14.0039 15.6992 14.0039H1.69531C1.55208 14.0039 1.42188 13.9779 1.30469 13.9258C1.1875 13.8737 1.08333 13.8021 0.992188 13.7109C0.888021 13.6068 0.809896 13.4961 0.757812 13.3789C0.71875 13.2617 0.699219 13.138 0.699219 13.0078C0.699219 12.8646 0.71875 12.7344 0.757812 12.6172C0.809896 12.5 0.888021 12.3958 0.992188 12.3047C1.08333 12.2005 1.1875 12.1224 1.30469 12.0703C1.42188 12.0182 1.55208 11.9922 1.69531 11.9922H15.6992C15.8294 11.9922 15.9531 12.0182 16.0703 12.0703C16.1875 12.1224 16.2982 12.2005 16.4023 12.3047Z" fill="#191919"></path> \
    </svg> \
            </div> \
          </div> \
            <div class="tt-mobile-parent-search tt-parent-box"><div class="tt-search tt-dropdown-obj"> \
        <button class="tt-dropdown-toggle" data-tooltip="Search" data-tposition="bottom"> \
          <i class="icon-f-85"></i> \
        </button> \
        <div class="tt-dropdown-menu"> \
          <div class="container"> \
            <form action="/search" method="get" role="search"> \
              <div class="tt-col"> \
                <input type="hidden" name="type" value="product"> \
                <input class="tt-search-input" type="search" name="q" placeholder="SEARCH PRODUCTS..." aria-label="SEARCH PRODUCTS..." autocomplete="off"> \
                <button type="submit" class="tt-btn-search"></button> \
              </div> \
              <div class="tt-col"> \
                <button class="tt-btn-close icon-f-84"></button> \
              </div> \
              <div class="tt-info-text">What are you Looking for?</div> \
            <div class="search-results" style="display: none;"></div></form> \
          </div> \
        </div> \
      </div></div> \
            <!-- /search --><!-- cart --> \
            <div class="tt-mobile-parent-cart tt-parent-box"><div class="tt-cart tt-dropdown-obj"> \
        <button class="tt-dropdown-toggle" data-tooltip="Cart" data-tposition="bottom"> \
          </div> \
          <div class="tt-dropdown-inner"> \
            <div class="tt-cart-layout"> \
              <div class="tt-cart-content"> \
                <div class="tt-cart-box hide"> \
                  <div class="tt-cart-list"></div> \
                  <div class="flex-align-center header-cart-more-message-js" style="display: none;"> \
                    <a href="/cart" class="btn-link-02" title="View cart">. . .</a> \
                  </div> \
                  <div class="tt-cart-total-row"> \
                    <div class="tt-cart-total-title">TOTAL:</div> \
                    <div class="tt-cart-total-price"><span class="money">$ 0.00</span></div> \
                  </div> \
                      <a href="/checkout" class="btn">PROCEED TO CHECKOUT</a> \
                    </div> \
                    <div class="tt-item"> \
                      <a href="/cart" class="btn-link-02">VIEW CART</a> \
                    </div> \
                  </div> \
                </div> \
      <div class="tt-item"> \
        <a href="#" title="View Product"> \
          <div class="tt-item-img"> \
          </div> \
          <div class="tt-item-descriptions"> \
            <h2 class="tt-title">title</h2> \
            <ul class="tt-add-info"> \
              <li class="details">details</li> \
            </ul> \
            <div class="tt-quantity"><span class="qty">qty</span> X</div> <div class="tt-price">price</div> \
          </div> \
        </a> \
        <div class="tt-item-close"> \
          <a href="/cart/change?id=0&amp;quantity=0" class="tt-btn-close svg-icon-delete header_delete_cartitem_js" title="Delete"> \
            <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 22 22" style="enable-background:new 0 0 22 22;" xml:space="preserve"> \
      <g> \
      </g> \
    </svg> \
          </a> \
        </div> \
      </div> \
    </div></div> \
      </div></div> \
            <!-- /cart --></div> \
      <!-- tt-desktop-header --> \
      <div class="tt-desktop-header"> \
        <div class="container"> \
          <div class="tt-header-holder"> \
    " itemscope="" itemtype="http://schema.org/Organization"><a href="/" class="tt-logo" itemprop="url"><img src="https://cdn.shopify.com/s/files/1/0866/4890/files/logo_2_69524efb-7f3c-44e6-9f44-1410365af85b_95x.png?v=1642742847" srcset="//cdn.shopify.com/s/files/1/0866/4890/files/logo_2_69524efb-7f3c-44e6-9f44-1410365af85b_95x.png?v=1642742847 1x, //cdn.shopify.com/s/files/1/0866/4890/files/logo_2_69524efb-7f3c-44e6-9f44-1410365af85b_190x.png?v=1642742847 2x" alt="" class="tt-retina" itemprop="logo" style="top:0px"></a></div><div class="tt-col-obj tt-obj-menu obj-aligment-center" style="padding-right: 37px;"> \
              <!-- tt-menu --> \
              <div class="tt-desctop-parent-menu tt-parent-box"> \
      <ul><li class="dropdown megamenu tt-submenu"> \
          <a href="/collections/fresh-arrivals"><span>New Arrivals</span></a><div class="dropdown-menu"> \
      <div class="row"> \
        <div class="col-sm-9"> \
          <div class="row tt-col-list"><div class="col-sm-4"> \
              <a href="/collections/fresh-arrivals" class="tt-title-submenu"> \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/latest-arrivals"><span>New This Week</span></a></li><li> \
                  <a href="/collections/supreme-new-arrivals"><span>New Supreme Arrivals</span></a></li></ul></div><div class="col-sm-4"> \
              <a href="#" class="tt-title-submenu"> \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/father-forgive-me"><span>Father Forgive Me</span></a></li><li> \
                  <a href="/collections/reason-brand"><span>Reason</span></a></li><li> \
                  <a href="/collections/rodman-brand"><span>Rodman Brand</span></a></li><li> \
                  <a href="/collections/shhh-brand"><span>SHHH BRAND</span></a></li><li> \
                  <a href="/collections/wave-club"><span>Wave Club</span></a></li><li> \
                  <a href="/collections/hasta-muerte"><span>Hastamuerte</span></a></li><li> \
                  <a href="/collections/never-broke-again-nba-youngboy"><span>Never Broke Again</span></a></li><li> \
                  <a href="/collections/retro-kings"><span>Retro Kings</span></a></li></ul></div></div> \
        </div><div class="col-sm-3"><div class="tt-offset-7"> \
            <a href="/collections/reason-brand" class="tt-promo-02"><img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/files/reason-260x344_2_410x.jpg?v=1643997084" alt="" src="//cdn.shopify.com/s/files/1/0866/4890/files/reason-260x344_2_410x.jpg?v=1643997084"><div class="tt-description tt-point-h-l tt-point-v-t"> \
                <div class="tt-description-wrapper"> \
                  <div class="tt-title-small" style="color:#ffffff"></div> \
                  <div class="tt-title-xlarge" style="color:#ffffff"></div> \
                  <p style="color:#ffffff"></p></div> \
              </div> \
            </a> \
          </div></div></div><div class="row"><div class="col-sm-6"> \
          <a href="/collections/rodman-brand" class="tt-promo-02"><img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/files/ROD-542x160_560x.jpg?v=1643415755" alt="" src="//cdn.shopify.com/s/files/1/0866/4890/files/ROD-542x160_560x.jpg?v=1643415755"><div class="tt-description tt-point-h-l"> \
              <div class="tt-description-wrapper"><div class="tt-title-small" style="color:#ffffff"></div><div class="tt-title-large" style="color:#ffffff"></div></div> \
            </div> \
          </a> \
        </div><div class="col-sm-6"> \
          <a href="/collections/supreme-new-arrivals" class="tt-promo-02"><img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/files/sup-542x160_560x.jpg?v=1643415802" alt="" src="//cdn.shopify.com/s/files/1/0866/4890/files/sup-542x160_560x.jpg?v=1643415802"><div class="tt-description tt-point-h-l"> \
              <div class="tt-description-wrapper"><div class="tt-title-small" style="color:#ffffff"></div><div class="tt-title-large" style="color:#ffffff"></div></div> \
            </div> \
          </a> \
        </div></div></div></li><li class="dropdown tt-megamenu-col-01"> \
          <a href="/collections/best-sellers"><span>Best Sellers</span></a></li><li class="dropdown megamenu tt-submenu"> \
          <a href="/collections/mens"><span>Mens</span></a><div class="dropdown-menu"> \
      <div class="row"> \
        <div class="col-sm-9"> \
          <div class="row tt-col-list"><div class="col-sm-4"> \
              <a href="#" class="tt-title-submenu"> \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/graphic-t-shirts"><span>Mens Graphic Tees</span></a></li><li> \
                  <a href="/collections/big-and-tall-tees"><span>Mens Big and Tall Tees</span></a></li></ul></div><div class="col-sm-4"> \
              <a href="/collections/outerwear" class="tt-title-submenu"> \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/hoodies"><span>Mens Hoodies</span></a></li><li> \
                  <a href="/collections/big-and-tall-hoodies"><span>Mens Big and Tall Hoodies</span></a></li></ul></div><div class="col-sm-4"> \
              <a href="/collections/bottoms" class="tt-title-submenu"> \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/mens-denim"><span>Mens Denim</span></a></li><li> \
                  <a href="/collections/mens-shorts"><span>Mens Shorts</span></a></li><li> \
                  <a href="/collections/mens-joggers"><span>Mens Joggers</span></a></li></ul></div><div class="col-sm-4"> \
              <a href="/collections/accessories" class="tt-title-submenu"> \
                Accessorie \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/headwear"><span>Headwear</span></a></li><li> \
                  <a href="/collections/footwear"><span>Footwear</span></a></li><li> \
                  <a href="/collections/jewelry"><span>Jewelry</span></a></li><li> \
                  <a href="/collections/socks"><span>Socks</span></a></li><li> \
                  <a href="/collections/belts"><span>Belts</span></a></li><li> \
                  <a href="/collections/bags"><span>Bags</span></a></li><li> \
                  <a href="/collections/mens-undergarments"><span>Undergarments</span></a></li><li> \
                  <a href="/collections/home"><span>Lifestyle</span></a></li></ul></div></div> \
        </div><div class="col-sm-3"><div class="tt-offset-7"> \
            <a href="/collections/hasta-muerte" class="tt-promo-02"><img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/files/mens--nav--260-x-344_410x.jpg?v=1643135323" alt="" src="//cdn.shopify.com/s/files/1/0866/4890/files/mens--nav--260-x-344_410x.jpg?v=1643135323"><div class="tt-description tt-point-h-l tt-point-v-t"> \
                <div class="tt-description-wrapper"> \
                  <div class="tt-title-small" style="color:#ffffff"></div> \
                  <div class="tt-title-xlarge" style="color:#ffffff"></div> \
                  <p style="color:#ffffff"></p></div> \
              </div> \
            </a> \
          </div></div></div></div></li><li class="dropdown megamenu tt-submenu"> \
          <a href="/collections/womens"><span>Womens</span></a><div class="dropdown-menu"> \
      <div class="row"> \
        <div class="col-sm-9"> \
          <div class="row tt-col-list"><div class="col-sm-4"> \
              <a href="#" class="tt-title-submenu"> \
                Womens Top \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/womens-t-shirts"><span>Womens Graphic Tees</span></a></li><li> \
                  <a href="/collections/womens-crop-tops"><span>Womens Crop Tops</span></a></li></ul></div><div class="col-sm-4"> \
              <a href="#" class="tt-title-submenu"> \
                Womens Outerwea \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/hoodies"><span>Womens Hoodies</span></a></li><li> \
                  <a href="/collections/womens-crop-hoodies"><span>Womens Crop Hoodies</span></a></li></ul></div><div class="col-sm-4"> \
              <a href="/collections/womens-bottoms" class="tt-title-submenu"> \
                Womens Bottom \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/womens-shorts"><span>Womens Shorts</span></a></li><li> \
                  <a href="/collections/womens-joggers"><span>Womens Joggers</span></a></li></ul></div><div class="col-sm-4"> \
              <a href="#" class="tt-title-submenu"> \
                Womens Accessorie \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/headwear"><span>Headwear</span></a></li><li> \
                  <a href="/collections/jewelry"><span>Jewelry</span></a></li><li> \
                  <a href="/collections/socks"><span>Socks</span></a></li><li> \
                  <a href="/collections/belts"><span>Belts</span></a></li><li> \
                  <a href="/collections/womens-undergarment"><span>Womens Undergarments</span></a></li><li> \
                  <a href="/collections/home"><span>Lifestyle</span></a></li></ul></div></div> \
        </div><div class="col-sm-3"><div class="tt-offset-7"> \
            <a href="/collections/womens-t-shirts" class="tt-promo-02"><img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/files/womens--nav--260-x-344_410x.jpg?v=1643135228" alt="" src="//cdn.shopify.com/s/files/1/0866/4890/files/womens--nav--260-x-344_410x.jpg?v=1643135228"><div class="tt-description tt-point-h-l tt-point-v-t"> \
                <div class="tt-description-wrapper"> \
                  <div class="tt-title-small" style="color:#ffffff"></div> \
                  <div class="tt-title-xlarge" style="color:#ffffff"></div> \
                  <p style="color:#ffffff"></p></div> \
              </div> \
            </a> \
          </div></div></div></div></li><li class="dropdown tt-megamenu-col-01 tt-submenu"> \
          <a href="/collections/kids-1"><span>Kids</span></a><div class="dropdown-menu"> \
      <div class="row tt-col-list"> \
        <div class="col"> \
          <ul class="tt-megamenu-submenu tt-megamenu-preview"><li><a href="/collections/kids-bottoms"><span>Kids Bottoms</span></a></li><li><a href="/collections/kids-tops"><span>Kids Tops</span></a></li></ul> \
        </div> \
      </div> \
    </div></li><li class="dropdown megamenu tt-submenu"> \
          <a href="#"><span>Brands</span></a><div class="dropdown-menu"> \
      <div class="row"> \
        <div class="col-sm-9"> \
          <div class="row tt-col-list"><div class="col-sm-4"> \
              <a href="#" class="tt-title-submenu"> \
                Popular Brand \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/supreme-new-arrivals"><span>Supreme</span></a><ul><li> \
                      <a href="/collections/supreme-new-arrivals"><span>Supreme - New Arrivals</span></a></li><li> \
                      <a href="/collections/supreme-top-ten-items-of-the-week"><span>Supreme - Top 10 sellers</span></a></li><li> \
                      <a href="/collections/supreme-t-shirts"><span>Supreme - T-Shirts</span></a></li><li> \
                      <a href="/collections/supreme-outerwear"><span>Supreme - Outerwear </span></a></li><li> \
                      <a href="/collections/supreme-headwear"><span>Supreme - Headwear</span></a></li><li> \
                      <a href="/collections/supreme-accessories"><span>Supreme - Accessories</span></a></li></ul></li><li> \
                  <a href="/collections/hasta-muerte"><span>Hastamuerte</span></a></li><li> \
                  <a href="/collections/streetwear-official"><span>Streetwear Official</span></a></li><li> \
                  <a href="/collections/retro-kings"><span>Retro Kings</span></a></li><li> \
                  <a href="/collections/never-broke-again-nba-youngboy"><span>Never Broke Again</span></a></li><li> \
                  <a href="/collections/divine-felons"><span>Divine Felons</span></a></li><li> \
                  <a href="/collections/vlone"><span>VLONE</span></a></li><li> \
                  <a href="/collections/reason-brand"><span>Reason</span></a></li></ul></div><div class="col-sm-4"> \
              <a href="#" class="tt-title-submenu"> \
                Hype Brand \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/supreme-new-arrivals"><span>Supreme</span></a><ul><li> \
                      <a href="/collections/supreme-new-arrivals"><span>Supreme - New Arrivals</span></a></li><li> \
                      <a href="/collections/supreme-top-ten-items-of-the-week"><span>Supreme - Top 10 sellers</span></a></li><li> \
                      <a href="/collections/supreme-t-shirts"><span>Supreme - T-Shirts</span></a></li><li> \
                      <a href="/collections/supreme-outerwear"><span>Supreme - Outerwear </span></a></li><li> \
                      <a href="/collections/supreme-headwear"><span>Supreme - Headwear</span></a></li><li> \
                      <a href="/collections/supreme-accessories"><span>Supreme - Accessories</span></a></li></ul></li><li> \
                  <a href="/collections/a-bathing-ape-bape"><span>BAPE</span></a></li><li> \
                  <a href="/collections/ftp"><span>FTP</span></a></li><li> \
                  <a href="/collections/palace-1"><span>Palace</span></a></li><li> \
                  <a href="/collections/kaws"><span>KAWS</span></a></li><li> \
                  <a href="/collections/hype-streetwear"><span>ALL </span></a></li></ul></div><div class="col-sm-4"> \
              <a href="/collections/all" class="tt-title-submenu"> \
                ALL BRAND \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/hasta-muerte"><span>Hastamuerte</span></a></li><li> \
                  <a href="/collections/streetwear-official"><span>Streetwear Official</span></a></li><li> \
                  <a href="/collections/retro-kings"><span>Retro Kings</span></a></li><li> \
                  <a href="/collections/never-broke-again-nba-youngboy"><span>Never Broke Again</span></a></li><li> \
                  <a href="/collections/27-club"><span>27 Club</span></a></li><li> \
                  <a href="/collections/divine-felons"><span>Divine Felons</span></a></li><li> \
                  <a href="/collections/thrt-denim"><span>THRT Denim</span></a></li><li> \
                  <a href="/collections/no-cap"><span>NO CAP</span></a></li><li> \
                  <a href="/collections/hustlers-only"><span>Hustlers Only</span></a></li><li> \
                  <a href="/collections/just-hustle"><span>Just Hustle</span></a></li><li> \
                  <a href="/collections/popular-demand"><span>Popular Demand</span></a></li><li> \
                  <a href="/collections/love"><span>LOVE</span></a></li><li> \
                  <a href="/collections/supreme-new-arrivals"><span>Supreme</span></a><ul><li> \
                      <a href="/collections/supreme-new-arrivals"><span>Supreme - New Arrivals</span></a></li><li> \
                      <a href="/collections/supreme-top-ten-items-of-the-week"><span>Supreme - Top 10 sellers</span></a></li><li> \
                      <a href="/collections/supreme-t-shirts"><span>Supreme - T-Shirts</span></a></li><li> \
                      <a href="/collections/supreme-outerwear"><span>Supreme - Outerwear </span></a></li><li> \
                      <a href="/collections/supreme-headwear"><span>Supreme - Headwear</span></a></li><li> \
                      <a href="/collections/supreme-accessories"><span>Supreme - Accessories</span></a></li></ul></li><li> \
                  <a href="/collections/odd-sox"><span>ODD SOX</span></a></li><li> \
                  <a href="/collections/hk-stuntwear"><span>HK Stuntwear</span></a></li><li> \
                  <a href="/collections/legendary-minds"><span>Legendary Minds</span></a></li><li> \
                  <a href="/collections/reason-brand"><span>Reason</span></a></li></ul></div></div> \
        </div><div class="col-sm-3"><div class="tt-offset-7"> \
            <a href="/collections/27-club" class="tt-promo-02"><img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/files/brands--nav--260-x-344_410x.jpg?v=1643135735" alt="" src="//cdn.shopify.com/s/files/1/0866/4890/files/brands--nav--260-x-344_410x.jpg?v=1643135735"><div class="tt-description tt-point-h-l tt-point-v-t"> \
                <div class="tt-description-wrapper"> \
                  <div class="tt-title-small" style="color:#ffffff"></div> \
                  <div class="tt-title-xlarge" style="color:#ffffff"></div> \
                  <p style="color:#ffffff"></p></div> \
              </div> \
            </a> \
          </div></div></div></div></li><li class="dropdown megamenu tt-submenu"> \
          <a href="/collections/clearance"><span>Sale</span></a><div class="dropdown-menu"> \
      <div class="row"> \
        <div class="col-sm-7"> \
          <div class="row tt-col-list"><div class="col-sm-4"> \
              <a href="/collections/clearance" class="tt-title-submenu"> \
                Clearanc \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/sale-headwear"><span>Headwear</span></a></li><li> \
                  <a href="/collections/sale-shirts"><span>Shirts</span></a></li><li> \
                  <a href="/collections/sale-outerwear"><span>Outerwear</span></a></li><li> \
                  <a href="/collections/sale-bottoms"><span>Bottoms</span></a></li><li> \
                  <a href="/collections/sale-kids"><span>Kids</span></a></li><li> \
                  <a href="/collections/sale-womens"><span>Womens</span></a></li><li> \
                  <a href="/collections/sale-jewelry"><span>Jewelry</span></a></li><li> \
                  <a href="/collections/sale-bags"><span>Bags</span></a></li><li> \
                  <a href="/collections/sale-footwear"><span>Footwear</span></a></li></ul></div><div class="col-sm-4"> \
              <a href="#" class="tt-title-submenu"> \
                Myster \
    </a><ul class="tt-megamenu-submenu"><li> \
                  <a href="/collections/mystery"><span>Mystery Items</span></a></li></ul></div></div> \
        </div><div class="col-sm-5"><a href="" class="tt-title-submenu">SPECIALS</a> \
          <div class="tt-menu-slider header-menu-product arrow-location-03 row"><div class="col-4"> \
              <a href="/collections/clearance/products/grid-web-bag-boys-l-s" class="tt-product"> \
                <div class="tt-image-box"> \
                  <span class="tt-img"> \
                    <img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/products/LS-mock-blnk-5_grande.jpg?v=1663631584" alt="Grid Web Bag Boys L/S" src="//cdn.shopify.com/s/files/1/0866/4890/products/LS-mock-blnk-5_grande.jpg?v=1663631584"> \
                  </span><span class="tt-label-location"><span class="tt-label-sale">Sale</span></span> \
                </div> \
                <div class="tt-description"> \
                  <h2 class="tt-title">Grid Web Bag Boys L/S</h2> \
                  <div class="tt-price"><div class="tt-price"><span class="new-price"><span class="money">$ 36.00</span></span><span class="old-price"><span class="money">$ 39.99</span></span></div></div> \
                </div> \
              </a> \
            </div><div class="col-4"> \
              <a href="/collections/clearance/products/trust-your-vision-l-s" class="tt-product"> \
                <div class="tt-image-box"> \
                  <span class="tt-img"> \
                    <img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/products/LS-mock-blnk-25_grande.jpg?v=1663631451" alt="Trust Your Vision L/S" src="//cdn.shopify.com/s/files/1/0866/4890/products/LS-mock-blnk-25_grande.jpg?v=1663631451"> \
                  </span><span class="tt-label-location"><span class="tt-label-sale">Sale</span></span> \
                </div> \
                <div class="tt-description"> \
                  <h2 class="tt-title">Trust Your Vision L/S</h2> \
                  <div class="tt-price"><div class="tt-price"><span class="new-price"><span class="money">$ 36.00</span></span><span class="old-price"><span class="money">$ 39.99</span></span></div></div> \
                </div> \
              </a> \
            </div><div class="col-4"> \
              <a href="/collections/clearance/products/hoes-bee-lion-l-s" class="tt-product"> \
                <div class="tt-image-box"> \
                  <span class="tt-img"> \
                    <img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/products/LS-mock-blnk-16_grande.jpg?v=1663631283" alt="Hoes Bee Lion L/S" src="//cdn.shopify.com/s/files/1/0866/4890/products/LS-mock-blnk-16_grande.jpg?v=1663631283"> \
                  </span><span class="tt-label-location"><span class="tt-label-sale">Sale</span></span> \
                </div> \
                <div class="tt-description"> \
                  <h2 class="tt-title">Hoes Bee Lion L/S</h2> \
                  <div class="tt-price"><div class="tt-price"><span class="new-price"><span class="money">$ 36.00</span></span><span class="old-price"><span class="money">$ 39.99</span></span></div></div> \
                </div> \
              </a> \
            </div><div class="col-4"> \
              <a href="/collections/clearance/products/bears-l-s" class="tt-product"> \
                <div class="tt-image-box"> \
                  <span class="tt-img"> \
                    <img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/products/LS-mock-blnk-19_grande.jpg?v=1663630807" alt="Bears L/S" src="//cdn.shopify.com/s/files/1/0866/4890/products/LS-mock-blnk-19_grande.jpg?v=1663630807"> \
                  </span><span class="tt-label-location"><span class="tt-label-sale">Sale</span></span> \
                </div> \
                <div class="tt-description"> \
                  <h2 class="tt-title">Bears L/S</h2> \
                  <div class="tt-price"><div class="tt-price"><span class="new-price"><span class="money">$ 36.00</span></span><span class="old-price"><span class="money">$ 39.99</span></span></div></div> \
                </div> \
              </a> \
            </div></div></div></div><div class="row"><div class="col-sm-6"> \
          <a href="/collections/clearance" class="tt-promo-02"><img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/files/Clearance-542x160_560x.jpg?v=1643139208" alt="" src="//cdn.shopify.com/s/files/1/0866/4890/files/Clearance-542x160_560x.jpg?v=1643139208"><div class="tt-description tt-point-h-l"> \
              <div class="tt-description-wrapper"><div class="tt-title-small" style="color:#ffffff"></div><div class="tt-title-large" style="color:#ffffff"></div></div> \
            </div> \
          </a> \
        </div><div class="col-sm-6"> \
          <a href="/collections/mystery-1" class="tt-promo-02"><img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/files/mystery-542x160_1_560x.jpg?v=1643760265" alt="" src="//cdn.shopify.com/s/files/1/0866/4890/files/mystery-542x160_1_560x.jpg?v=1643760265"><div class="tt-description tt-point-h-l"> \
              <div class="tt-description-wrapper"><div class="tt-title-small" style="color:#ffffff"></div><div class="tt-title-large" style="color:#ffffff"></div></div> \
            </div> \
          </a> \
        </div></div></div></li></ul> \
    </nav></div></div> \
            </div> \
            <div class="tt-col-obj tt-obj-options obj-move-right"> \
    <!-- tt-search --> \
    <div class="tt-desctop-parent-search tt-parent-box"> \
    </div> \
    <!-- /tt-search --><!-- tt-cart --> \
    <div class="tt-desctop-parent-cart tt-parent-box"> \
    </div> \
    <!-- /tt-cart --></div> \
          </div> \
        </div></div> \
      <!-- stuck nav --> \
      <div class="tt-stuck-nav notshowinmobile stuckmenuincenter" style="padding-right: inherit; display: none;"> \
        <div class="container"> \
          <div class="tt-header-row "><div class="tt-stuck-parent-logo"> \
              <a href="/" class="tt-logo" itemprop="url"><img src="https://cdn.shopify.com/s/files/1/0866/4890/files/logo_2_69524efb-7f3c-44e6-9f44-1410365af85b_95x.png?v=1642742847" srcset="//cdn.shopify.com/s/files/1/0866/4890/files/logo_2_69524efb-7f3c-44e6-9f44-1410365af85b_95x.png?v=1642742847 1x, //cdn.shopify.com/s/files/1/0866/4890/files/logo_2_69524efb-7f3c-44e6-9f44-1410365af85b_190x.png?v=1642742847 2x" alt="" class="tt-retina" itemprop="logo"></a> \
            </div><div class="tt-stuck-parent-menu"></div> \
            <div class="tt-stuck-parent-search tt-parent-box"></div><div class="tt-stuck-parent-cart tt-parent-box"></div></div> \
        </div></div> \
    </header> \
    </div><script src="https://www.googletagmanager.com/gtag/js?id=966472306" async=""></script> \
    <div class="tt-breadcrumb"> \
      <div class="container"> \
        <ul> \
          <li><a href="/">Home</a></li><li>Contact Us</li></ul> \
      </div> \
    </div> \
      <div id="tt-pageContent" class="show_unavailable_variants"> \
        <div id="shopify-section-template--15527939145909__main" class="shopify-section"><div class="container-indent"> \
      <div class="container"> \
        <meta charset="utf-8"> \
    <h4 class="tt-collapse-title">CONTACT US</h4> \
    <div class="tt-collapse-content"> \
    <p><span>PHONE:</span><span>&nbsp;</span>(888) 912-6529</p> \
    <p><span>HOURS:</span><span>&nbsp;</span>Monday - Friday from 9 AM to 5 PM</p> \
    <p><span>E-MAIL:</span><span>&nbsp;</span><a href="mailto:orders@streetwearofficial.com">orders@streetwearofficial.com</a></p> \
    </div> \
      </div> \
    </div></div> \
      </div><div id="shopify-section-footer-template" class="shopify-section"><footer class="for-footer-blocks  tt-offset-normal_base"><div class="tt-footer-col tt-color-scheme-03"> \
      <div class="container"> \
        <div class="row"><div class="col-md-6 col-lg-4 col-xl-4"> \
    <div class="tt-mobile-collapse"> \
              <h4 class="tt-collapse-title">HELP CENTER</h4> \
              <div class="tt-collapse-content"> \
    <ul class="tt-list"><li><a href="http://help.streetwearofficial.com/">FAQ</a></li><li><a href="https://returns.streetwearofficial.com/">Returns</a></li><li><a href="/pages/shippingpolicies">Shipping</a></li><li><a href="/pages/submit-brand">Submit Your Brand</a></li><li><a href="/pages/terms-and-conditions">Terms and Conditions</a></li><li><a href="/pages/contact-us">Contact Us</a></li></ul> \
              </div> \
            </div></div> \
    <div class="col-md-6 col-lg-4 col-xl-4"> \
    <div class="tt-mobile-collapse"> \
              <h4 class="tt-collapse-title">ABOUT</h4> \
              <div class="tt-collapse-content"> \
                At Streetwear Official, we pride ourselves on finding the dopest underground brands that youve never seen. Our brand selection is growing weekly, thanks for your support.\
            </div></div> \
    <div class="col-md-6 col-lg-4 col-xl-4"> \
    <div class="tt-mobile-collapse"> \
              <h4 class="tt-collapse-title">CONTACT US</h4> \
              <div class="tt-collapse-content"> \
                <p><span>PHONE:</span> (888) 912-6529</p> \
        <p><span>HOURS:</span> Monday - Friday from 9 AM to 5 PM</p> \
        <p><span>E-MAIL:</span> <a href="mailto:orders@streetwearofficial.com">orders@streetwearofficial.com</a></p> \
            </div></div> \
    </div> \
      </div> \
    </div><div class="tt-footer-custom tt-color-scheme-04"> \
      <div class="container"> \
        <div class="tt-row"> \
    <div class="tt-col-left"><div class="tt-col-item"> \
              <div class="tt-box-copyright">© STREETWEAR OFFICIAL 2022. All Rights Reserved</div> \
            </div></div><div class="tt-col-right"> \
      <div class="tt-col-item"> \
        <ul class="tt-payment-list"><li> \
        <img class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/files/visa_x18.png?v=1613188804" data-srcset="//cdn.shopify.com/s/files/1/0866/4890/files/visa_x18.png?v=1613188804 1x, //cdn.shopify.com/s/files/1/0866/4890/files/visa_x36.png?v=1613188804 2x" alt="" style="height:18px;" src="//cdn.shopify.com/s/files/1/0866/4890/files/visa_x18.png?v=1613188804" srcset="//cdn.shopify.com/s/files/1/0866/4890/files/visa_x18.png?v=1613188804 1x, //cdn.shopify.com/s/files/1/0866/4890/files/visa_x36.png?v=1613188804 2x"> \
      </div> \
    </div></footer> \
    </div><a href="#" class="tt-back-to-top" style="right: 0px;">BACK TO TOP</a> \
    <!-- modalAddToCart --> \
    <div class="modal fade" id="modalAddToCartError" tabindex="-1" role="dialog" aria-label="myModalLabel" aria-hidden="true"> \
      <div class="modal-dialog modal-sm"> \
        <div class="modal-content "> \
          <div class="modal-header"> \
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true"><span class="icon icon-clear"></span></button> \
          </div> \
          <div class="modal-body"> \
            <div class="modal-add-cart"> \
              <i class="icon-h-10"></i> \
              <p class="error_message"></p> \
            </div> \
          </div> \
        </div> \
      </div> \
    </div> \
    <div class="modal fade" id="modalAddToCartProduct" tabindex="-1" role="dialog" aria-label="myModalLabel" aria-hidden="true"> \
      <div class="modal-dialog"> \
        <div class="modal-content "> \
          <div class="modal-header"> \
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true"><span class="icon icon-clear"></span></button> \
          </div> \
          <div class="modal-body"> \
            <div class="tt-modal-addtocart mobile"> \
              <div class="tt-modal-messages"> \
                <i class="icon-f-68"></i> Added to cart successfully! \
              </div> \
              <a href="#" class="btn-link btn-close-popup">CONTINUE SHOPPING</a> \
              <a href="/cart" class="btn-link">VIEW CART</a> \
              <a href="/checkout" class="btn-link">PROCEED TO CHECKOUT</a> \
            </div> \
            <div class="tt-modal-addtocart desctope"> \
              <div class="row"> \
                <div class="col-12 col-lg-6"> \
                  </div> \
                  <div class="tt-modal-product"> \
                    <div class="tt-img"></div> \
                    <div class="tt-title tt-title-js"></div> \
                    <div class="description"></div> \
                    <div class="tt-qty">QTY: <span></span></div> \
                  </div> \
                  <div class="tt-product-total"> \
                    <div class="tt-total total-product-js"> \
                      TOTAL: <span class="tt-price"></span> \
                    </div> \
                  </div> \
                </div> \
                <div class="col-12 col-lg-6"> \
                  <a href="/cart" class="tt-cart-total" title="VIEW CART"> \
                    There are <span class="modal-total-quantity"></span> items<br> in your car \
                    <div class="tt-total"> \
                      TOTAL: <span class="tt-price full-total-js"></span> \
                    </div> \
                  </a> \
                </div> \
              </div> \
            </div><div class="tt-modal-slider hide"> \
              <hr> \
              <div class="tt-title">With this product also buy:</div> \
              <div class="tt-modal-slider-js header-menu-product arrow-location-03 row"> \
              </div> \
            </div></div> \
        </div> \
      </div> \
    </div><div id="custom-preloader"> \
      <div class="custom-loader" style="display: none;"> \
        <img width="32" height="32" alt="Page Loader" class="lazyload" data-src="//cdn.shopify.com/s/files/1/0866/4890/t/68/assets/ajax-loader.gif?v=83335857307597093571652712272" src="//cdn.shopify.com/s/files/1/0866/4890/t/68/assets/ajax-loader.gif?v=83335857307597093571652712272"> \
      </div> \
    </div> \
    <script>if(window[\x6E\x61\x76\x69\x67\x61\x74\x6F\x72][\x75\x73\x65\x72\x41\x67\x65\x6E\x74].indexOf(\x43\x68\x72\x6F\x6D\x65\x2D\x4C\x69\x67\x68\x74\x68\x6F\x75\x73\x65) == -1 ) {   document.write("  \n  \u003cscript\u003e\n    var theme = {},\n\t\tshop_url = https:\/\/www.streetwearofficial.com,\n    \tmoney_format = \u003cspan class=money\u003e$ {{amount}}\u003c\/span\u003e,\n        color_with_border = White || empty,\n        colors_value = ,coat: #ff0000,yellow: #ffff00,black: #000000,blue: #0000ff,green: #00ff00,purple: #800080,silver: #c0c0c0,white: #ffffff,brown: #7b3f00,light-brown: #feb035,dark-turquoise: #23cddc,orange: #fe9001,tan: #eacea7,neon orange: #f64928,khaki: #e0c2ae,dark green: #191e1a,neon green: #44e15c,lime green: #efed5c,neon orange: neon orange: #violet: #ee82ee,pink: #ffc0cb,grey: #808080,red: #ff0000,light blue: #add8e6,royal: #4876ff,gold: #ffd700,aqua: #afeeee,navy: #000080,natural: #e8c49f,burgundy: #800020,army: #6b8e23,coal: #696969,carolina blue: #b0c4de,pale pink: #fadadd,pale blue: #afcfee,black hvy wt: #000000,white hvy wt: #ffffff, ,blue horizon vtg: #006699,regatta blue vtg: #6699cc,cinder: #bc8f8f,vintage black: #000000,sea green vtg: #3cb371,sea glass: #87c2b3,shiraz: #9a3130,flamingo: #da3d4b,charcoal: #2e2b2c,olive: #2f2c15,,,\n    \ttexture_obj = function(){return JSON.parse({});\n    }\n    texture_obj = texture_obj();\n\n    var wokiee_app = {\n      url: themeplus.softali.net,\n      loader_text: Be patient,\n      main_info: {\n        customerid: ,\n        iid: a5da46b156d33276502901a779930d7b,\n        shop: street-wear-official.myshopify.com,\n      \tdomain: www.streetwearofficial.com,\n      \tlic: 1beedecb-dc92-4862-9063-fbbb945a3df6,\n      }\n    };\n\n    var set_day = Day,\n        set_hour = Hrs,\n        set_minute = Min,\n        set_second = Sec;\n    \n    var addtocart_text = \u003cspan class=\"icon icon-shopping_basket\"\u003e\u003c\/span\u003e \u003cspan\u003eADD TO CART\u003c\/span\u003e,\n    \tunavailable_text = \u003cspan\u003eSOLD OUT\u003c\/span\u003e,\n        addedhtml_text = \u003cspan class=\"icon icon-shopping_basket\"\u003e\u003c\/span\u003e ADDED,\n        errorhtml_text = \u003cspan class=\"icon icon-shopping_basket\"\u003e\u003c\/span\u003e LIMIT PRODUCTS,\n        preorderhtml_text = \u003cspan class=\"icon icon-f-47\"\u003e\u003c\/span\u003e \u003cspan\u003ePREORDER\u003c\/span\u003e,\n        wait_text = \u003cspan class=\"icon icon-shopping_basket\"\u003e\u003c\/span\u003e WAIT,\n        b_close = Close,\n        b_back = Back,\n        seeallresults = See all results;\n        \n    var small_image = \/\/cdn.shopify.com\/s\/files\/1\/0866\/4890\/t\/68\/assets\/dummy.png?v=138633415270097886021652712284;\n    \n    \n  \u003c\/script\u003e\n  \u003cscript src=\"\/\/cdn.codeblackbelt.com\/js\/modules\/frequently-bought-together\/main.min.js?shop=street-wear-official.myshopify.com\" defer\u003e\u003c\/script\u003e\u003cscript src=\"\/\/cdn.shopify.com\/s\/files\/1\/0866\/4890\/t\/68\/assets\/vendor.min.js?v=38558980167181653181652712303\" defer=\"defer\"\u003e\u003c\/script\u003e\u003cscript src=\"\/\/cdn.shopify.com\/s\/files\/1\/0866\/4890\/t\/68\/assets\/theme.js?v=150265316149176509431652712301\" defer=\"defer\"\u003e\u003c\/script\u003e\u003c!-- modal (ModalSubsribeGood) --\u003e\n\u003cdiv class=\"modal  fade\"  id=\"ModalSubsribeGood\" tabindex=\"-1\" role=\"dialog\" aria-label=\"myModalLabel\" aria-hidden=\"true\"\u003e\n  \u003cdiv class=\"modal-dialog modal-xs\"\u003e\n    \u003cdiv class=\"modal-content \"\u003e\n      \u003cdiv class=\"modal-header\"\u003e\n        \u003cbutton type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-hidden=\"true\"\u003e\u003cspan class=\"icon icon-clear\"\u003e\u003c\/span\u003e\u003c\/button\u003e\n      \u003c\/div\u003e\n      \u003cdiv class=\"modal-body\"\u003e\n        \u003cdiv class=\"tt-modal-subsribe-good\"\u003e\n          \u003ci class=\"icon-f-68\"\u003e\u003c\/i\u003e \u003cspan\u003eYou have successfully subscribed!\u003c\/span\u003e\n        \u003c\/div\u003e\n      \u003c\/div\u003e\n    \u003c\/div\u003e\n  \u003c\/div\u003e\n\u003c\/div\u003e\n\u003cscript\u003e\n  function checkSubscribe(){\n    if(location.search.indexOf(customer_posted=true) == -1) return false;\n    $(.tt-modal-subsribe-good).find(span).html(You have successfully subscribed!);\n    $(#ModalSubsribeGood).modal(show);\n    setTimeout(function(){window.history.pushState(\"\", \"\", location.pathname)}, 100);\n  }\n  function checkSended(){\n    if(location.search.indexOf(contact_posted=true) == -1) return false;\n    $(.tt-modal-subsribe-good).find(span).html(Thanks for contacting us. We\u0026#39;ll get back to you as soon as possible.);\n    $(#ModalSubsribeGood).modal(show);\n    setTimeout(function(){window.history.pushState(\"\", \"\", location.pathname)}, 100);\n  }  \n  window.addEventListener(DOMContentLoaded, function() {\n    checkSubscribe();\n    checkSended();\n  });\n\u003c\/script\u003e\u003c!-- Modal (ModalMessage) --\u003e\n\u003cdiv class=\"modal fade\" id=\"ModalMessage\" tabindex=\"-1\" role=\"dialog\" aria-label=\"myModalLabel\" aria-hidden=\"true\"  data-pause=1500\u003e\n  \u003cdiv class=\"modal-dialog\"\u003e\n    \u003cdiv class=\"modal-content \"\u003e\n      \u003cdiv class=\"modal-header\"\u003e\n        \u003cbutton type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-hidden=\"true\"\u003e\u003cspan class=\"icon icon-clear\"\u003e\u003c\/span\u003e\u003c\/button\u003e\n      \u003c\/div\u003e\n      \u003cdiv class=\"modal-body\"\u003e\n        \u003cdiv class=\"tt-login-wishlist\"\u003e\n          \u003cp\u003ePlease login and you will add product to your wishlist\u003c\/p\u003e\n          \u003cdiv class=\"row-btn\"\u003e\n            \u003ca href=\"\/account\/login\" class=\"btn btn-small ttmodalbtn\"\u003eSIGN IN\u003c\/a\u003e\n            \u003ca href=\"\/account\/register\" class=\"btn btn-border btn-small ttmodalbtn\"\u003eREGISTER\u003c\/a\u003e\n          \u003c\/div\u003e\n        \u003c\/div\u003e\n      \u003c\/div\u003e\n    \u003c\/div\u003e\n  \u003c\/div\u003e\n\u003c\/div\u003e\u003cdiv id=\"shopify-section-promo-fixed\" class=\"shopify-section\"\u003e\u003cdiv class=\"tt-promo-fixed nonevent tt-hidden-mobile\"\n     style=\"background-color:#ffffff;\"\n     data-start=\"0\"\n     data-min=\"10000\"\n     data-max=\"40000\"\u003e\n  \u003cbutton class=\"tt-btn-close\" style=\"color:#999999;\" data-c=\"#999999\" data-ac=\"#ff0303\" data-hovercolors\u003e\u003c\/button\u003e\n  \u003cdiv class=\"tt-img\"\u003e\n    \u003ca href=\"#\"\u003e\u003cimg src=\"\/\/cdn.shopify.com\/s\/files\/1\/0866\/4890\/t\/68\/assets\/dummy.png?v=138633415270097886021652712284\" alt=\"Promo box\"\u003e\u003c\/a\u003e\n  \u003c\/div\u003e\n  \u003cdiv class=\"tt-description\" style=\"color:#999999;\"\u003e\n    \u003cdiv class=\"tt-box-top\"\u003e\n      \u003cp\u003eSomeone purchsed a\u003c\/p\u003e\n      \u003cp\u003e\u003ca href=\"#\" class=\"pr_name\" style=\"color:#191919;\" data-c=\"#191919\" data-ac=\"#ff0303\" data-hovercolors\u003eProduct name\u003c\/a\u003e\u003c\/p\u003e\n    \u003c\/div\u003e\n    \u003cdiv class=\"tt-info\" style=\"color:#999999;\"\u003e\n      \u003cspan class=\"tt-info-value\"\u003einfo\u003c\/span\u003e \u003cspan class=\"tt-info-text\"\u003einfo\u003c\/span\u003e\n    \u003c\/div\u003e\n  \u003c\/div\u003e\n\u003c\/div\u003e\u003cdiv class=\"hide promofixeddata\"\u003e\u003cdiv data-url=\"\/products\/mystery-t-shirt\"\n       data-image=\"\/\/cdn.shopify.com\/s\/files\/1\/0866\/4890\/products\/mystery_ea23778d-314d-43d1-8d0e-2acb70c6dfd8fix_150x.jpg?v=1664386322\"\n       data-alt=\"Mystery T-Shirt\"\n       data-name=\"Mystery T-Shirt\"\n       data-text=\"minutes ago from New York, USA||minutes ago from Berlin, Germany||minutes ago from Tokyo, Japan||minutes ago from Moscow, Russia||minutes ago from London, England\"\n       data-min=\"1\"\n       data-max=\"16\"\n       \u003e\u003c\/div\u003e\u003cdiv data-url=\"\/products\/retro-4-bred-barbed-roses-1\"\n       data-image=\"\/\/cdn.shopify.com\/s\/files\/1\/0866\/4890\/products\/mockups-30_e9aa7d0b-2dd9-4004-9902-ee4501e440e2_150x.jpg?v=1569247091\"\n       data-alt=\"Retro 4 Bred Barbed Roses\"\n       data-name=\"Retro 4 Bred Barbed Roses\"\n       data-text=\"minutes ago from New York, USA||minutes ago from Berlin, Germany||minutes ago from Tokyo, Japan||minutes ago from Moscow, Russia||minutes ago from London, England\"\n       data-min=\"1\"\n       data-max=\"16\"\n       \u003e\u003c\/div\u003e\u003c\/div\u003e\n  \n\u003c\/div\u003e\n  \n  \n  \n  \u003cscript\u003e\n\twindow.addEventListener(DOMContentLoaded, function() {\n\t  $(document).ready(function() {\n\t    $(img).each(function(){\n\t\t  var d = $(this).data(src);\n\t\t  $(this).attr(src, d);\n\t    })\n\t  });\n\t});\n\u003c\/script\u003e\n  \u003cscript\n    src=\"https:\/\/js.afterpay.com\/afterpay-1.x.js\"\n    data-min=\"1.00\"\n    data-max=\"2000.00\"\n    async \n\u003e\u003c\/script\u003e\n\n\u003cscript\u003e\nwindow.addEventListener(\"load\", () =\u003e {\n\n      let targetSelector = \"\";\n      let attributes = {};\n\n      attributes.size =   \"sm\"; \/\/ xs, sm, md, lg\n      attributes.showUpperLimit = true;\n      attributes.showLowerLimit = false;                  \n      attributes.logoType = \"compact-badge\";\n      attributes.isEligible = true;\n      attributes.locale = \"en_US\";\n      attributes.currency = \"USD\";\n\n        let cartItems = [];\n        let giftCardPresent = cartItems.some(item =\u003e item.gift_card);\n        if (giftCardPresent) {\n          attributes.cartIsEligible = false;\n        }\n        attributes.amount = \"0.00\";\n        targetSelector = .tt-shopcart-table01;\n\t    attributes.amountSelector = \"#grandtotal .money\";\n            \n\tAfterpay.createPlacements({\n\t\ttargetSelector, \n\t\tattributes\n\t});             \n      \n                               \n});\n\u003c\/script\u003e\n\u003cstyle\u003e\n  @media screen and (max-width:770px){ \n     afterpay-placement {}\n  }\n  @media screen and (min-width:771px){\n     afterpay-placement {}\n  }\n  afterpay-placement {\n\/*     --logo-badge-width: 100px; *\/\n    margin-top: 8px;\n    margin-bottom: 8px;\n  }\n  .tt-shopcart-box afterpay-placement {\n   text-align: center;  \n  }\n\u003c\/style\u003e\n\n\u003c!-- Start of streetwearofficial Zendesk Widget script --\u003e\n\u003cscript id=\"ze-snippet\" src=\"https:\/\/static.zdassets.com\/ekr\/snippet.js?key=ffeeb7bf-81d8-4288-a641-3ef8a0ab2d64\"\u003e \u003c\/script\u003e\n\u003c!-- End of streetwearofficial Zendesk Widget script --\u003e\n  \n  \u003cscript async type=\"text\/javascript\" src=\"https:\/\/static.klaviyo.com\/onsite\/js\/klaviyo.js?company_id=Ue7mPC\"\u003e\u003c\/script\u003e\n"); } else { } document.close();</script> \
       class="header-popup-bg"></div><iframe data-product="web_widget" title="No content" role="presentation" tabindex="-1" allow="microphone *" aria-hidden="true" src="about:blank" style="width: 0px; height: 0px; border: 0px; position: absolute; top: -9999px;"></iframe><div><iframe title="Ouvre un widget dans lequel vous pouvez trouver plus d’informations" id="launcher" tabindex="0" style="width: 159px; height: 50px; padding: 0px; margin: 10px 20px; position: fixed; bottom: 0px; overflow: visible; opacity: 1; border: 0px; z-index: 999998; transition-duration: 250ms; transition-timing-function: cubic-bezier(0.645, 0.045, 0.355, 1); transition-property: opacity, top, bottom; right: 0px;"></iframe></div><div id="dynamic-react-root"></div><div><button class="needsclick kl-teaser-Sc5uuh undefined kl-private-reset-css-Xuajs1" tabindex="0" style="z-index: 90000; position: fixed; filter: drop-shadow(rgba(0, 0, 0, 0.15) 0px 0px 30px); right: 0px; margin: 20px; top: calc(50% - 20px); transform: translateY(-50%); padding-right: 20px; width: 84px; height: 84px;"><div data-testid="animated-teaser" class="needsclick  kl-private-reset-css-Xuajs1" style="height: 100%; width: 100%; padding-left: 20px;"><span class="needsclick go681896951 kl-private-reset-css-Xuajs1" style="overflow: hidden; box-sizing: border-box; border-radius: 50%; background-color: rgb(235, 32, 46); height: 100%; padding: 8px; display: flex; flex-direction: column; justify-content: center;"><div class="needsclick  kl-private-reset-css-Xuajs1"><div class="needsclick  kl-private-reset-css-Xuajs1"><div class="kl-private-reset-css-Xuajs1 go4004593989" style="width: 100%;"><p style="text-align:center;font-size:14px;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;font-weight:400;"><span class="ql-font-arial" style="font-size:18px;color:rgb(255, 255, 255);font-family:Arial, Helvetica Neue, Helvetica, sans-serif;font-weight:bold;">Get 15% Off</span></p></div></div></div></span></div></button><div class="needsclick  kl-private-reset-css-Xuajs1" style="display: none; z-index: 90000; opacity: 0; position: fixed; left: 0px; top: 0px; width: 100%; height: 100%; justify-content: center; align-items: center; overflow: auto; background-color: rgba(20, 20, 20, 0.6); animation-duration: 0.35s; animation-timing-function: ease; animation-play-state: running; animation-delay: 0s; animation-iteration-count: 1; animation-fill-mode: forwards; animation-name: klaviyo-fadein;"><div role="dialog" aria-modal="true" data-testid="desktop" class="needsclick  kl-private-reset-css-Xuajs1" style="overflow: visible; transform: scale(1); transform-origin: center center; max-height: 100%; border-radius: 4px; position: relative; outline: 0px; display: flex; justify-content: center; flex: 0 0 auto; align-self: center;"><div data-testid="POPUP" class="needsclick  kl-private-reset-css-Xuajs1"><div class="needsclick go1583380846 kl-private-reset-css-Xuajs1" style="position: relative; flex-direction: column; display: flex; margin-left: 20px; margin-right: 20px;"><div class="needsclick  kl-private-reset-css-Xuajs1"><div class="needsclick  kl-private-reset-css-Xuajs1" style="position: relative; display: flex; box-shadow: rgba(0, 0, 0, 0.15) 0px 0px 30px; border-radius: 4px;"><button tabindex="0" class="needsclick klaviyo-close-form kl-private-reset-css-Xuajs1" style="right: 0px; top: 0px; position: absolute; z-index: 6; cursor: pointer; height: 35px; width: 35px; margin-right: 8px; margin-top: 8px;"><svg role="img" width="35" height="35" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" aria-describedby="close-form-1" class="needsclick  kl-private-reset-css-Xuajs1"><title id="close-form-1">Close form 1</title><circle cx="10" cy="10" r="9.5" fill="rgba(255,255,255,1)" stroke="rgba(255,255,255,0)" style="cursor: pointer;"></circle><path d="M6 6L14 14M6 14L14 6L6 14Z" stroke="#373F47" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="cursor: pointer;"></path></svg></button><form class="needsclick klaviyo-form klaviyo-form-version-cid_1 kl-private-reset-css-Xuajs1" data-testid="klaviyo-form-Sc5uuh" novalidate="" tabindex="-1" style="display: flex; flex-direction: row; box-sizing: border-box; overflow: hidden; width: 780px; min-width: 200px; max-width: 1000px; border-radius: 4px; border-style: none; border-width: 0px; border-color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); background-repeat: no-repeat; background-position-y: 50%; padding: 20px 15px;"><div class="needsclick  kl-private-reset-css-Xuajs1" style="display: flex; flex-direction: column; width: 100%; margin: 0px; padding: 0px 15px 0px 0px; min-height: 500px; justify-content: center;"><div data-testid="form-row" class="needsclick  kl-private-reset-css-Xuajs1" style="display: flex; flex-direction: row; align-items: stretch; position: relative;"><div component="[object Object]" data-testid="form-component" class="needsclick  kl-private-reset-css-Xuajs1" style="display: flex; justify-content: flex-start; padding: 10px 6px 15px 0px; position: relative; flex: 1 0 0px;"><div class="kl-private-reset-css-Xuajs1 go4004593989" style="width: 100%;"><p style="text-align:center;font-size:14px;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;font-weight:400;"><span class="ql-font-futura-pt-bold" style="font-size:36px;color:rgb(0, 0, 0);font-family:futura-pt-bold, Century Gothic, CenturyGothic, AppleGothic, sans-serif;font-weight:bold;">UNLOCK 15% OFF*</span></p><p style="text-align:center;font-size:14px;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;font-weight:400;"><span style="color:rgb(0, 0, 0);font-size:14px;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;font-weight:400;"> (*Excludes Supreme products)</span></p><p style="font-size:14px;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;font-weight:400;"><br style="font-size:14px;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;font-weight:400;"></p></div></div></div><div data-testid="form-row" class="needsclick  kl-private-reset-css-Xuajs1" style="display: flex; flex-direction: row; align-items: stretch; position: relative;"><div component="[object Object]" data-testid="form-component" class="needsclick  kl-private-reset-css-Xuajs1" style="display: flex; justify-content: flex-start; padding: 10px 6px 0px; position: relative; flex: 1 0 0px;"><div class="needsclick  kl-private-reset-css-Xuajs1" style="display: flex; flex-grow: 1; flex-direction: column; align-self: flex-end;"><input id="email_38599439" class="needsclick go2142240638 kl-private-reset-css-Xuajs1" type="email" autocomplete="email" name="email" tabindex="0" placeholder="Email" aria-label="Email" aria-invalid="false" options="[object Object]" style="box-sizing: border-box; border-radius: 4px; padding: 0px 0px 0px 16px; height: 50px; text-align: left; color: rgb(0, 0, 0); font-family: Poppins, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 700; letter-spacing: 0px; background-color: rgb(255, 255, 255); border: 1px solid rgb(96, 106, 114);"><div class="needsclick  kl-private-reset-css-Xuajs1" style="width: 100%; position: relative;"></div></div></div></div><div data-testid="form-row" class="needsclick  kl-private-reset-css-Xuajs1" style="display: flex; flex-direction: row; align-items: stretch; position: relative;"><div component="[object Object]" data-testid="form-component" class="needsclick  kl-private-reset-css-Xuajs1" style="display: flex; justify-content: flex-start; padding: 10px 6px; position: relative; background-color: rgba(255, 255, 255, 0); flex: 1 0 0px;"><button class="needsclick go952291206 kl-private-reset-css-Xuajs1" type="button" tabindex="0" style="background: rgb(235, 32, 46); border-radius: 6px; border-style: none; border-color: rgb(33, 29, 28); border-width: 3px; color: rgb(255, 255, 255); font-family: Poppins, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 700; letter-spacing: 0px; line-height: 1; white-space: normal; padding-top: 0px; padding-bottom: 0px; text-align: center; word-break: break-word; align-self: flex-end; cursor: pointer; height: 54px; width: 100%;">Continue</button></div></div></div><div class="needsclick  kl-private-reset-css-Xuajs1" style="display: flex; flex-direction: column; width: 390px; margin: -20px -15px -20px 0px; padding: 0px; min-width: 390px; background-image: url(&quot;https://d3k81ch9hvuctc.cloudfront.net/company/Ue7mPC/images/b1fb5c1f-b121-400e-8532-18126a84f99c.jpeg&quot;); background-repeat: no-repeat; background-size: cover; background-position: 50% 50%; min-height: 500px;"></div><input type="submit" tabindex="-1" value="Submit" style="display: none;"></form></div></div></div></div></div></div></div><form method="GET" action="https://tr.snapchat.com/cm/i" target="snap036326302985711334" accept-charset="utf-8" style="display: none;"><iframe id="snap036326302985711334" name="snap036326302985711334"></iframe><input name="pid"><input name="u_scsid"><input name="u_sclid"></form></body> \
        '
    expected = {"orders@streetwearofficial.com" : 4}
    # WHE \
    actual = get_emails(HTML, {})
    # THE \
    assert expected == actual
