def test_register_empty_password(client):
    response = client.post('/auth/register', data={'username': 'user2', 'password': ''})
    assert b'Password is required.' in response.data
