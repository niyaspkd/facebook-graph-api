
import requests
import json

def del_comment():
    
    TOKEN=''
    parameters = {'access_token': TOKEN}
    r = requests.delete('https://graph.facebook.com/me/{comment-id}?method=delete', params=parameters)
    print r.content, "deleted"
   
    
 del_comment()