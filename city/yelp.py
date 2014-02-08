"""Example for signing a search request using the oauth2 library."""

import oauth2
import urllib2
import json

# Fill in these values

def yelp_values(full_url):
    obj = urllib2.urlopen(full_url)
    
    data = json.load(obj)
    businesses = {}
    locations = []
#            locations.append([abc['name'], abc['id']])
    for business in data['businesses']:
        
        biz_name = business['name']
        for deals in business['deals']:
            try:
                the_title = deals['title']
                length = len(the_title)
                large = int(the_title[length-2:length]) + 0.0
                title_index = the_title.index(" ")
                small = int(the_title[1:title_index]) + 0.0
                the_deal = abs((small - large) / large) * 100
                str_deal = str(the_deal)
                str_deal = str_deal[0:2]
                deal = '%s%s off' %(str_deal, "%")
            except:
                deal = 'Fake out! No deal. They lied to us both!'
            
            try:
                url = business['url']
            except:
                pass
            locations.append([biz_name, deal])
        rating_img_url = business['rating_img_url_small']
        address = business['location']['display_address'][0] + ", " + business['location']['city'] + ", " + business['location']['state_code']
        print address
        businesses[biz_name] = [url, rating_img_url, deal, address]
    

    
    return locations, businesses

def yelp_request_url(zip_code):
    from yelp_secrets import consumer_key, consumer_secret, token, token_secret
    consumer_key = consumer_key
    consumer_secret = consumer_secret
    token = token
    token_secret = token_secret
    
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    url = 'http://api.yelp.com/v2/search?term=bars&location=' + zip_code + '&deals_filter=true'
    
    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                          'oauth_timestamp': oauth2.generate_timestamp(),
                          'oauth_token': token,
                          'oauth_consumer_key': consumer_key})
    
    token = oauth2.Token(token, token_secret)
    
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    
    signed_url = oauth_request.to_url()
    print signed_url
    return signed_url