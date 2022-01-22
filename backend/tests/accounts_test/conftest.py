import pytest

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass

@pytest.fixture(scope='function')
def mock_create_user_form():
    return {
        'username': 'username',
        'password': 'wefk5*%sle$',
        'passwordConfirmation': 'wefk5*%sle$'
    }


@pytest.fixture(scope='class')
@pytest.mark.django_db
def mock_test_user():
    User = get_user_model()
    test_user = User.objects.create(username='testuser', password='password')
    refresh = RefreshToken.for_user(test_user)
    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return {
        'user': test_user,
        'token': token
    }

# class MockLogin:
#     @pytest.fixture(scope='class')
#     @pytest.mark.django_db
#     def __init__(self):
#         User = get_user_model()
#         self.test_user = User.objects.create(username='testuser', password='password')
#         self.refresh = RefreshToken.for_user(self.test_user)

#     @pytest.fixture(scope='function')
#     def mock_test_user(self):
#         return self.test_user

#     @pytest.fixture(scope='function')
#     def mock_test_token(self):
#         return {
#             'refresh': str(self.refresh),
#             'access': str(self.refresh.access_token),
#         }