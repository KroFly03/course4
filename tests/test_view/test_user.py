import pytest

from services.user import UserService


class TestUserView:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao, test_client):
        self.user_service = UserService(dao=user_dao)
        self.test_client = test_client

    # def test_get_one(self):
    #     response = self.test_client.get('/user', follow_redirects=True, method='GET')
    #     assert response.status_code == 200
    #
    # def test_patch(self):
    #     response = self.test_client.get('/user', follow_redirects=True, method='PATCH')
    #     assert response.status_code == 204
    #
    # def test_update_password(self):
    #     response = self.test_client.get('/password', follow_redirects=True, method='PUT')
    #     assert response.status_code == 204
    #