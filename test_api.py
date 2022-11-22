#Unit tests for flaskAPI. Cannot be used at the same time that flaskAPI.py is running

import unittest
from flaskAPI import *


class TestAPI(unittest.TestCase):

    def test_coin_put(self):
        test_server = app.test_client(self)
        response = test_server.put("/", json= {"coin": 1})
        self.assertEqual(response.status_code, 204, "status code should be 204")
        self.assertEqual(response.data, b'', "The coin PUT command doesn't have the right data")
        self.assertEqual(response.content_type, "application/json", "content-type should be application/json")

    def test_coin_delete(self):
        test_server = app.test_client(self)
        response = test_server.delete("/")
        self.assertEqual(response.status_code, 204, "status code should be 204")
        self.assertEqual(response.data, b'', "response body should be empty")
        self.assertEqual(response.content_type, "application/json", "content-type should be application/json")

    def test_inventory_get(self):
        test_server = app.test_client(self)
        response = test_server.get("/inventory")
        self.assertEqual(response.status_code, 200, "status code should be 200")
        self.assertEqual(response.data, b'[5, 5, 5]', "response body should be array of quantities left")
        self.assertEqual(response.content_type, "application/json", "content-type should be application/json")

    def test_specific_inventory_get(self):
        test_server = app.test_client(self)
        response = test_server.get("/inventory/1")
        self.assertEqual(response.status_code, 200, "status code should be 200")
        self.assertEqual(response.data, b'5', "response body should be integer of item quantity")
        self.assertEqual(response.content_type, "application/json", "content-type should be application/json")

    def test_specific_inventory_put(self):
        test_server = app.test_client(self)
        response = test_server.put("/inventory/1")
        self.assertEqual(response.status_code, 403, "status code should be 403 with less than 2 coins")
        self.assertEqual(response.data, b'', "response body should be empty with less than 2 coins")
        self.assertEqual(response.content_type, "application/json", "content-type should be application/json")

if __name__ == "__main__":
    unittest.main()