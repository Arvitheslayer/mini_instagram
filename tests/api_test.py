import pytest
from app import api_posts, api_post
from utils import get_posts_all,get_post_by_pk
from json import dumps

class TestPostApi:
    def test_type(self):
        assert api_posts() == dumps(get_posts_all('D:\pythonProject\mini_instagram\data\posts.json'), ensure_ascii=False, indent=4), 'не возвращает список'


class TestPostsApi:
    def test_post1(self):
        assert api_post(1) == dumps(get_post_by_pk(1), ensure_ascii=False, indent=4), 'неверный пост'

    def test_post3(self):
        assert api_post(3) == dumps(get_post_by_pk(3), ensure_ascii=False, indent=4), 'неверный пост'

    def test_post7(self):
        assert api_post(7) == dumps(get_post_by_pk(7), ensure_ascii=False, indent=4), 'неверный пост'

    def test_post4(self):
        assert api_post(4) == dumps(get_post_by_pk(4), ensure_ascii=False, indent=4), 'неверный пост'