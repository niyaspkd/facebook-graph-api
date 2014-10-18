def user_likes_page(user_id, page_id):
    TOKEN=''
    url = 'https://graph.facebook.com/%d/likes/%d/' % (user_id, page_id)
    parameters = {'access_token': TOKEN}
    r = requests.get(url, params = parameters)
    result = json.loads(r.text)
    if result['data']:
        return True
    else:
        return False