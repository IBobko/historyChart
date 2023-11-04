def test_example(client):
    response = client.get('/greet')
    assert response.status_code == 200
