from Helpers.variables import base_url



def test_get_list_of_objects_by_id(request_context,get_multiple_object_ids):

    id1 = get_multiple_object_ids()
    id2 = get_multiple_object_ids()
    id3 = get_multiple_object_ids()


    response = request_context.get(f"{base_url}/objects?id={id1}&id={id2}&id={id3}")
    response_body = response.json()

    print(response_body)
    print(response_body[0])

    assert response.ok
    assert response.status == 200

    assert id1 == response_body[0]["id"]
    assert id2 == response_body[1]["id"]
    assert id3 == response_body[2]["id"]