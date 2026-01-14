from Helpers.variables import base_url
from Helpers.read_file import read_json


def test_full_update_object(request_context, get_multiple_object_ids):
    data = read_json("testdata/put_request_full_update_object.json")
    object_id = get_multiple_object_ids()

    response = request_context.put(f"{base_url}/objects/{object_id}", data=data)

    response_body = response.json()
    print(response_body)

    assert response.ok
    assert response.status == 200

    assert "id" in response_body
    assert "updatedAt" in response_body
    assert "name" in response_body
    assert "data" in response_body

    if response_body["name"] is not None:
        assert response_body["name"] == data["name"]

    if response_body["data"] is not None:
        assert response_body["data"] == data["data"]

    # assert object_id == response_body["id"]
    # assert response_body["name"] == data["name"]
    #
    # nested_data = response_body["data"]
    # assert nested_data["year"] == data["data"]["year"]
    # assert nested_data["price"] == data["data"]["price"]
    # assert nested_data["CPU model"] == data["data"]["CPU model"]
    # assert nested_data["Hard disk size"] == data["data"]["Hard disk size"]


