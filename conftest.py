# Fixture for the request context --> it's the same for all requests
import pytest
from playwright.sync_api import Playwright
from Helpers.variables import base_url
from Helpers.read_file import read_json


@pytest.fixture(scope="session")
def request_context(playwright:Playwright):
    request_context = playwright.request.new_context() # create a new request_context to send the different requests
    yield request_context
    request_context.dispose # --> This will dispose the context after the test is executed because it's after the yield


@pytest.fixture()
def get_multiple_object_ids(request_context):
    data = read_json("testdata/post_request_add_object.json")

    def get_object_id():
        # request_context = playwright.request.new_context()

        response = request_context.post(f"{base_url}/objects", data=data)
        response_body = response.json()

        # booking = response_body["booking"]
        object_id = response_body["id"]  # This is the booking id from the response body
        # firstname = booking["firstname"]
        # lastname = booking["lastname"]
        # check_in = booking["bookingdates"]["checkin"]
        # check_out = booking["bookingdates"]["checkout"]
        return object_id

    return get_object_id



# @pytest.fixture(scope="session")
# def get_new_object_id(request_context):
#     #request_context = playwright.request.new_context()
#     data = read_json("testdata/post_request_add_object.json")
#     response = request_context.post(f"{base_url}/objects", data=data)
#     response_body = response.json()
#
#     #booking = response_body["booking"]
#     object_id = response_body["id"]  # This is the booking id from the response body
#     # firstname = booking["firstname"]
#     # lastname = booking["lastname"]
#     # check_in = booking["bookingdates"]["checkin"]
#     # check_out = booking["bookingdates"]["checkout"]
#     return object_id


