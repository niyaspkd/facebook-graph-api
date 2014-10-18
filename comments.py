def comment_on_posts(posts):
    TOKEN=''
    message=raw_input()
    for post in posts:
        url = 'https://graph.facebook.com/%s/comments' % post['post_id']
        message = 'Commenting through the Graph API'
        parameters = {'access_token': TOKEN, 'message': message}
        s = requests.post(url, data = parameters)
        pprint(s)
comment_on_posts(post_id)