import requests
import json
import pprint
def get_posts():
    
    TOKEN=''
    parameters = {'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/me/feed', params=parameters)
    result = json.loads(r.text)
    return pprint.pprint(result['data'])
    
print get_posts()