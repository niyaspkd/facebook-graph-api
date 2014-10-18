import requests
import json
import pprint
def get_pic():
    
    TOKEN=''
    parameters = {'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/me?feilds=picture, params=parameters)
    result = json.loads(r.text)
    return pprint.pprint(result['data'])
get_pic()