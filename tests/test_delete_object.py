from Helpers.variables import base_url

def test_delete_object(request_context, get_multiple_object_ids):
    object_id = get_multiple_object_ids()
    response = request_context.delete(f"{base_url}/objects/{object_id}")

    response_body = response.json()
    print(response_body)

    assert response.ok
    assert response.status == 200

    assert "message" in response_body

    assert response_body["message"] == f"Object with id = {object_id} has been deleted."