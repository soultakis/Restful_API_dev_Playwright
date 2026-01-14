from Helpers.variables import base_url


def test_get_single_object_by_id(request_context, get_multiple_object_ids):
    object_id = get_multiple_object_ids()
    response = request_context.get(f"{base_url}/objects/{object_id}")


    response_body = response.json()
    print("This is the object with object_id {}:".format(object_id), response_body)

    assert response.ok
    assert response.status == 200

    assert "id" in response_body
    assert "name" in response_body
    assert "data" in response_body

    assert response_body["id"] == object_id


