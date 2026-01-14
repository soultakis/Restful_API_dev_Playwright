from Helpers.read_file import read_json
from Helpers.variables import base_url

def test_patch_partially_update_object(request_context, get_multiple_object_ids):
    object_id = get_multiple_object_ids()

    data = read_json("testdata/patch_request_partially_update_object.json")

    response = request_context.patch(f"{base_url}/objects/{object_id}", data=data)
    response_body = response.json()

    print(response_body)

    assert response.status == 200
    assert response.ok

    assert "id" in response_body
    assert "updatedAt" in response_body
    assert "name" in response_body
    assert "data" in response_body

