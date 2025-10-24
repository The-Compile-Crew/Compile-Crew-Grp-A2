import unittest
from App.models import User
from App.controllers.user_controller import (
    create_user,
    get_user_by_username,
    get_user,
    get_all_users,
    get_all_users_json,
    update_user
)
from App.database import db

class UserControllerUnitTests(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()

    def test_create_user(self):
        user = create_user("aisha", "securepass")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "aisha")
        self.assertTrue(user.check_password("securepass"))

    def test_get_user_by_username(self):
        create_user("aisha", "securepass")
        user = get_user_by_username("aisha")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "aisha")

    def test_get_user(self):
        user = create_user("aisha", "securepass")
        fetched = get_user(user.id)
        self.assertEqual(fetched.username, "aisha")

    def test_get_all_users(self):
        create_user("aisha", "securepass")
        create_user("bibi", "pass123")
        users = get_all_users()
        self.assertEqual(len(users), 2)

    def test_get_all_users_json(self):
        create_user("aisha", "securepass")
        json_list = get_all_users_json()
        self.assertEqual(json_list[0]["username"], "aisha")

    def test_update_user(self):
        user = create_user("aisha", "securepass")
        success = update_user(user.id, "updated_aisha")
        self.assertTrue(success)
        updated = get_user(user.id)
        self.assertEqual(updated.username, "updated_aisha")