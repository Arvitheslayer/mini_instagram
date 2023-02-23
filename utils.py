from json import load

def get_posts_all(path):
    with open(path, 'r', encoding='utf-8') as file:
        posts = load(file)
    return posts

def get_posts_by_user(user_name):
    list_users = []
    for i in map(lambda x: x['poster_name'], get_posts_all('D:\pythonProject\mini_instagram\data\posts.json')):
        list_users.append(i)
    if user_name not in list_users:
        raise ValueError
        return []
    list_ = []
    for post in get_posts_all('D:\pythonProject\mini_instagram\data\posts.json'):
        if post['poster_name'] == user_name:
            list_.append(post)
    return list_


def get_comment_by_id(post_id):
    list_ids = []
    for i in map(lambda x: x['post_id'], get_posts_all('D:\pythonProject\mini_instagram\data\comments.json')):
        list_ids.append(i)
    if post_id not in list_ids:
        raise ValueError
        return []
    list_ = []
    for comment in get_posts_all('D:\pythonProject\mini_instagram\data\comments.json'):
        if comment['post_id'] == post_id:
            list_.append(comment['comment'])
    return list_


def search_for_posts(query):
    list_ = []
    for post in get_posts_all('D:\pythonProject\mini_instagram\data\posts.json'):
        if query in post['content']:
            list_.append(post)
    return list_


def get_post_by_pk(pk):
    list_ = []
    for post in get_posts_all('D:\pythonProject\mini_instagram\data\posts.json'):
        if pk == post['pk']:
            list_.append(post)
    return list_




