def test_create_requires_login(client):
    response = client.get('/create')
    assert response.status_code == 302  # Redirect
    assert '/auth/login' in response.headers['Location']
