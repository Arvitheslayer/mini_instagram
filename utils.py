from json import load

def get_posts_all():
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        posts = load(file)
        return posts