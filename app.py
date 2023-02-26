from flask import Flask, render_template, request
from utils import get_posts_all, get_comment_by_id, search_for_posts, get_posts_by_user, get_post_by_pk
from werkzeug.exceptions import BadRequest
from json import dumps
import logging

logging.basicConfig(filename='api.log/basiclog.log', level=logging.INFO)
app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def main_page():
    items = get_posts_all('D:\pythonProject\mini_instagram\data\posts.json')
    return render_template('index.html', items=items)

@app.route('/users', methods=["GET", "POST"])
def users():
    if request.method == 'GET':
        amount = 0
        return render_template('user-feed.html', amount=amount)
    else:
        items = get_posts_by_user(request.form.get('user_name'))
        amount = len(items)
        return render_template('user-feed.html', items=items, amount=amount)


@app.route('/posts/<int:id>')
def post_page(id):
    for post in get_posts_all('D:\pythonProject\mini_instagram\data\posts.json'):
        if post['pk'] == id:
            post1 = post
    items = get_comment_by_id(id)
    return render_template('post.html', items=items, post=post1)


@app.route('/search', methods=["GET", "POST"])
def search_page():
    if request.method == 'GET':
        amount = 0
        return render_template('search.html', amount=amount)
    else:
        items = search_for_posts(request.form.get('searching_string'))
        amount = len(items)
        return render_template('search.html', items=items, amount=amount)

@app.route('/api/posts')
def api_posts():
    logging.info('Запрос /api/posts')
    return dumps(get_posts_all('D:\pythonProject\mini_instagram\data\posts.json'), ensure_ascii=False, indent=4)


@app.route('/api/posts/<int:id>')
def api_post(id):
    logging.info(f'Запрос /api/posts{id}/')
    return dumps(get_post_by_pk(id), ensure_ascii=False, indent=4)


@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'Такого адреса не найдено', 404

@app.errorhandler(BadRequest)
def handle_bad_request1(e):
    return 'Проблемма на стороне сервера', 500


app.register_error_handler(500, handle_bad_request1)
app.register_error_handler(404, handle_bad_request)


if __name__ == '__main__':
    app.run()
