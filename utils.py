from json import load
from json import dumps
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
            list_.append(comment)
    return list_


def search_for_posts(query):
    list_ = []
    for post in get_posts_all('D:\pythonProject\mini_instagram\data\posts.json'):
        if query.lower() in post['content'].lower():
            list_.append(post)
    return list_


def get_post_by_pk(pk):
    list_ = []
    for post in get_posts_all('D:\pythonProject\mini_instagram\data\posts.json'):
        if pk == post['pk']:
            list_.append(post)
    return list_

def get_post_by_tag(tag):
    list_ = []
    for post in get_posts_all('D:\pythonProject\mini_instagram\data\posts.json'):
        if f'#{tag}' in post['content']:
            list_.append(post)
    return list_

def get_bookmarks():
    with open(r'D:\pythonProject\mini_instagram\data\bookmarks.json', 'r', encoding='utf-8') as file:
        posts = load(file)
    return posts


def add_bookmark(post):
    with open(r'D:\pythonProject\mini_instagram\data\bookmarks.json', 'r', encoding='utf-8') as file:
        list_ = load(file)
    list_.append(post)
    with open(r'D:\pythonProject\mini_instagram\data\bookmarks.json', 'w', encoding='utf-8') as file:
        x = dumps(list_, ensure_ascii=False, indent=4)
        file.write(x)


def delete_bookmarkx(postid):
    with open(r'D:\pythonProject\mini_instagram\data\bookmarks.json', 'r', encoding='utf-8') as file:
        list_ = load(file)
    for i in range(len(list_)):
        if list_[i]['pk'] == postid:
            list_.pop(i)
            break
    with open(r'D:\pythonProject\mini_instagram\data\bookmarks.json', 'w', encoding='utf-8') as file:
        x = dumps(list_, ensure_ascii=False, indent=4)
        file.write(x)








