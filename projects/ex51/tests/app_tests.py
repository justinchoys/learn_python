from nose.tools import *
from ex51.app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
	rv = web.get('/', follow_redirects=True)
	assert_equal(rv.status_code, 404)

	rv = web.get('/hello', follow_redirects=True)
	assert_equal(rv.status_code, 200)
	#note that data we get from web is in bytes, so need to decode (DBES) to string
	assert_in("Fill Out This Form", rv.data.decode("utf-8"))


	data = {'name' : 'Zed', 'greet' : 'Hola'}
	#can send form data as dict via .post() function
	rv = web.post('/hello', follow_redirects=True, data=data)
	assert_in(b"Zed", rv.data)
	assert_in(b"Hola", rv.data)
	