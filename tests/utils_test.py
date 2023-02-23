import pytest
from utils import get_posts_all,get_posts_by_user,get_post_by_pk,get_comment_by_id, search_for_posts

class TestGetAllPosts():
    def test_type(self):
        assert isinstance(get_posts_all('D:\pythonProject\mini_instagram\data\posts.json'), list) == True, 'не возвращает список'

    def test_availability(self):
        assert len(get_posts_all('D:\pythonProject\mini_instagram\data\posts.json')) > 0, 'список пуст'


class TestGetPostByUser(TestGetAllPosts):
    def test_value_error(self):
        with pytest.raises(ValueError):
            get_posts_by_user('Olga')

    def test_value_error1(self):
        with pytest.raises(ValueError):
            get_posts_by_user('Mike')

    def test_value_error2(self):
        with pytest.raises(ValueError):
            get_posts_by_user('Natan')


class TestCommentById(TestGetPostByUser):
    def test_1(self):
        assert len(get_comment_by_id(5)) == 2, 'неверное количество коментариев'

    def test_2(self):
        assert len(get_comment_by_id(7)) == 1, 'неверное количество коментариев'

    def test_3(self):
        assert len(get_comment_by_id(1)) == 4, 'неверное количество коментариев'

    def test_4(self):
        assert get_comment_by_id(5) == ["Давно тебя тут не было, с возвращением!", "Ничего себе, вот это ты молодец!"], 'неверный коментарий'

    def test_5(self):
        assert get_comment_by_id(7) == ["Очень необычная фоторафия! Где это?"], 'неверный коментарий'


class TestSearchForPosts(TestGetAllPosts):
    def test_1(self):
        assert search_for_posts("Ага, опять еда") == [get_posts_all('D:\pythonProject\mini_instagram\data\posts.json')[0]], 'неверный результат'

    def test_2(self):
        assert search_for_posts("острова в основном каменные") == [get_posts_all('D:\pythonProject\mini_instagram\data\posts.json')[-1]], 'неверный результат'

    def test_3(self):
        assert search_for_posts("чтобы посмотреть на него") == [get_posts_all('D:\pythonProject\mini_instagram\data\posts.json')[-2]], 'неверный результат'


class TestGetPostsByPk(TestGetAllPosts):
    def test_1(self):
        assert get_post_by_pk(3) == [get_posts_all('D:\pythonProject\mini_instagram\data\posts.json')[2]], 'неверный результат'

    def test_2(self):
        assert get_post_by_pk(6) == [get_posts_all('D:\pythonProject\mini_instagram\data\posts.json')[5]], 'неверный результат'

    def test_3(self):
        assert get_post_by_pk(1) == [get_posts_all('D:\pythonProject\mini_instagram\data\posts.json')[0]], 'неверный результат'







