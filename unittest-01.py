import unittest
from typing import Dict, Union, Any


class Authentication:
    USERS = [{"username": "user1", "password": "pwd1"}]

    def login(self, username: str, password: str) -> Union[Dict[str, str], Any]:

        user = self.fetch_user(username)
        if not user or user["password"] != password:
            return None
        return user

    def fetch_user(self, username: str) -> Union[Dict[str, str], Any]:
        for user in self.USERS:
            if user["username"] == username:
                return user
            return None
        return None


class Authorization:
    PERMISSIONS = [{"user": "user1", "permissions": {"create", "edit", "delete"}}]

    def can(self, user: Dict[str, str], action: str) -> bool:
        for u in self.PERMISSIONS:
            if u["user"] == user["username"]:
                return action in u["permissions"]
            return False
        return False


class TestAuthentication(unittest.TestCase):
    def test_login(self):
        auth = Authentication()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]
        resp = auth.login("testuser", "testpass")
        assert resp == {"username": "testuser", "password": "testpass"}


class TestAuthorization(unittest.TestCase):
    def test_can(self):
        authz = Authorization()
        authz.PERMISSIONS = [{"user": "testuser", "permissions": {"create"}}]
        resp = authz.can({"username": "testuser"}, "create")
        assert resp is True


class TestAuthorizeAuthenticatedUser(unittest.TestCase):
    def test_auth(self):
        auth = Authentication()
        authz = Authorization()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]
        authz.PERMISSIONS = [{"user": "testuser", "permissions": {"create"}}]
        u = auth.login("testuser", "testpass")
        resp = authz.can(u, "create")
        assert resp is True


if __name__ == "__main__":
    unittest.main()
