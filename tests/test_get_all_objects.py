from Helpers.variables import base_url



def test_get_all_objects(request_context):
    response = request_context.get(f"{base_url}/objects")

    response_body = response.json()
    print("This is the response body:", response_body)

    assert response.status == 200
    assert response.ok



