
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert rv.status_code == 404

    rv = web.get('/hello', follow_redirects=True)
    assert rv.status_code == 200
    assert "이 폼을 채우세요" in rv.data.decode()

    data = {'name': '제드', 'greet': 'Hello'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert "제드" in rv.data.decode()
    assert b"Hello" in rv.data
