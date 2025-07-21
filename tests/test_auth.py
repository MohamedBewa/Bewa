def test_register_empty_password(client):
    response = client.post('/auth/register', data={'username': 'user2', 'password': ''})
    assert b'Password is required.' in response.data
def test_register_existing_username(client, auth):
    auth.register()
    response = client.post('/auth/register', data={'username': 'test', 'password': 'abc'})
    assert b'already registered' in response.data
