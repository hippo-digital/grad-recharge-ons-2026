def test_example_page_uses_the_ons_layout(client):
    response = client.get("/")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "<h1>Example page</h1>" in page
    assert 'class="ons-header' in page
    assert 'class="ons-footer' in page
