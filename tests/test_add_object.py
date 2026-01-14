import json
import pytest
from playwright.sync_api import Playwright
from Helpers.read_file import read_json
from Helpers.variables import base_url


# Base url is the same for all requests --> the endpoint changes
#base_url = "https://restful-booker.herokuapp.com"


# Utility function for reading the json file
# I will use it in all requests that need to read the data from a file
# So I create a function that opens a file from a file_path (not the same for all requests)
# and returns the json output

# def read_json(file_path):
#     file  = open(file_path, "r")
#     return json.load(file)


# # Fixture for the request context --> it's the same for all requests
# @pytest.fixture(scope="session")
# def request_context(playwright:Playwright):
#     request_context = playwright.request.new_context() # create a new request_context to send the different requests
#     yield request_context
#     request_context.dispose # --> This will dispose the context after the test is executed because it's after the yield



# 1) First test is to create a booking

def test_add_object(request_context):
    data = read_json("testdata/post_request_add_object.json")

    response = request_context.post(f"{base_url}/objects", data=data)

    assert response.status == 200
    assert response.ok

    response_body = response.json()
    print("This is the response body:", response_body)

    assert "id" in response_body
    assert "createdAt" in response_body
    assert "name" in response_body
    assert "data" in response_body

    assert response_body["name"] == data["name"]

    nested_data = response_body["data"]

    assert nested_data["year"] == data["data"]["year"]
    assert nested_data["price"] == data["data"]["price"]
    assert nested_data["CPU model"] == data["data"]["CPU model"]
    assert nested_data["Hard disk size"] == data["data"]["Hard disk size"]



# def test_create_booking(request_context):
#     data = read_json("testdata/post_request_body.json")
#     response = request_context.post(f"{base_url}/booking", data=data)
#
#     assert response.status == 200
#     assert response.ok
#
#     response_body = response.json() # gets only the body of the response
#     print("This is the response body:", response_body)
#
#     assert "bookingid" in response_body
#     assert "booking" in response_body
#
#     booking = response_body["booking"]
#     assert booking["firstname"] == data["firstname"]
#     assert booking["lastname"] == data["lastname"]
#     assert booking["totalprice"] == data["totalprice"]
#     assert booking["depositpaid"] == data["depositpaid"]
#     assert booking["additionalneeds"] == data["additionalneeds"]
#     assert booking["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
#     assert booking["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]
#     assert booking["additionalneeds"] == data["additionalneeds"]
#
#     # We need to use the booking id that is created in the other tests
#     # This is a local variable. I cannot use the return command because I don't want to return values from tests
#     # We need to make it a global variable so I can use it everywhere. First we need to declare it
#     global booking_id, firstname, lastname, check_in, check_out
#     booking_id = response_body["bookingid"] # This is the booking id from the response body
#     firstname = booking["firstname"]
#     lastname = booking["lastname"]
#     check_in = booking["bookingdates"]["checkin"]
#     check_out = booking["bookingdates"]["checkout"]
