import requests 

def get():
	payload = {'page': 2, 'count': 25} # Query parameters.
	r = requests.get("https://httpbin.org/get", params=payload)

	return r.url

def post():
	payload = {'username': "John Doe", "password": "test"} # Key parameters
	r = requests.post('https://httpbin.org/post', data=payload)
	r_dict = r.json()

	return r_dict['form']

def test_auth():
	r = requests.get('https://httpbin.org/basic-auth/Daquiver/randomP', auth=('Daquiver', 'randomP'))

	return r

print(test_auth())