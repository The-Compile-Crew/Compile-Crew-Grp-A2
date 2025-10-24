import unittest
from App.models import Request

class RequestModelUnitTests(unittest.TestCase):

    def test_create_request(self):
        request = Request(residentId=1, driveId=2)
        self.assertEqual(request.residentId, 1)
        self.assertEqual(request.driveId, 2)
        self.assertEqual(request.status, "pending")
        self.assertIsNone(request.description)

    def test_request_json(self):
        request = Request(residentId=1, driveId=2, description="Pickup groceries")
        expected = {
            'requestId': None,
            'residentId': 1,
            'driveId': 2,
            'status': 'pending',
            'description': "Pickup groceries"
        }
        self.assertDictEqual(request.toJSON(), expected)