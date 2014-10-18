def get_common_likes(post_id, page_id):
    
    TOKEN=''
    count_likes = 0
    url = 'https://graph.facebook.com/%d/likes/' % post_id
    parameters = {'access_token': TOKEN}
    r = requests.get(url, params = parameters)
    result = json.loads(r.text)
    for like in result['data']:
        if user_likes_page(int(like['id']), page_id):
            count_likes += 1
            print 1
    return count_likes
get_common_likes(post_id,page_id)