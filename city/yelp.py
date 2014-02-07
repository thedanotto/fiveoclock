"""Example for signing a search request using the oauth2 library."""

import oauth2
import urllib2
import json

# Fill in these values

def yelp_values(full_url):
    obj = urllib2.urlopen(full_url)
    
    data = json.load(obj)
    
    locations = []
#            locations.append([abc['name'], abc['id']])
    for business in data['businesses']:
        biz_name = business['name']
        for deals in business['deals']:
            deal = deals['what_you_get']
            deal = deal.split(".")
            deal = deal[0]
            locations.append([biz_name, deal])
    return locations

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

    return signed_url