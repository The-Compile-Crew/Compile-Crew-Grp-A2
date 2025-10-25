import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User
from App.controllers import (
    create_user,
    get_all_users_json,
    login,
    get_user,
    get_user_by_username,
    update_user
)

LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("bob", "bobpass")
        assert user.username == "bob"

    def test_get_json(self):
        user = User("bob", "bobpass")
        user_json = user.get_json()
        # model.get_json includes the polymorphic type field
        self.assertDictEqual(user_json, {"id": None, "username": "bob", "type": "user"})

    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password)
        user = User("bob", password)
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password)
        assert user.check_password(password)

'''
    Integration Tests
'''

@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()

def test_authenticate():
    user = create_user("bob", "bobpass")
    assert login("bob", "bobpass") is not None

class UsersIntegrationTests(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()

    def test_create_user(self):
        user = create_user("rick", "bobpass")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        create_user("bob", "bobpass")
        create_user("rick", "bobpass")
        users_json = get_all_users_json()
        # include the 'type' field returned by User.get_json()
        self.assertListEqual(
            [{"id": 1, "username": "bob", "type": "user"}, {"id": 2, "username": "rick", "type": "user"}],
            users_json
        )

    def test_update_user(self):
        create_user("bob", "bobpass")
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"