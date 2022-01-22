import json
import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
@pytest.mark.urls('accounts.urls')
class TestUserList:
    User = get_user_model()

    # sign up
    def test_signup_valid(self, client, mock_create_user_form):
        client.post('/users/', mock_create_user_form)
        assert len(self.User.objects.all()) == 1

    def test_signup_username_max_length(self, client, mock_create_user_form):
        mock_create_user_form['username'] = 'u' * 21
        assert client.post('/users/', mock_create_user_form).status_code == 400
    
    def test_signup_username_min_length(self, client, mock_create_user_form):
        mock_create_user_form['username'] = 'u' * 2
        assert client.post('/users/', mock_create_user_form).status_code == 400
    
    def test_signup_username_contain_blank(self, client, mock_create_user_form):
        mock_create_user_form['username'] = 'user name'
        assert client.post('/users/', mock_create_user_form).status_code == 400
    
    def test_signup_password_min_length(self, client, mock_create_user_form):
        mock_create_user_form['password'] = 'p' * 7
        mock_create_user_form['passwordConfirmation'] = 'p' * 7
        assert client.post('/users/', mock_create_user_form).status_code == 400
        with pytest.raises(self.User.DoesNotExist):
            self.User.objects.get(username=mock_create_user_form['username'])
    
    def test_signup_password_contain_blank(self, client, mock_create_user_form):
        mock_create_user_form['password'] = 'sj4* @knt'
        mock_create_user_form['passwordConfirmation'] = 'sj4* @knt'
        assert client.post('/users/', mock_create_user_form).status_code == 400
        
    def test_signup_password_confirmation_different(self, client, mock_create_user_form):
        mock_create_user_form['passwordConfirmation'] = 'different'
        assert client.post('/users/', mock_create_user_form).status_code == 400

    # get user list
    def test_get_user_list(self, client):
        self.User.objects.create(username='username', password='wefk5*%sle$')
        assert json.loads(client.get('/users/').content)[0]['username'] == 'username'
    

@pytest.mark.django_db
@pytest.mark.urls('accounts.urls')
class TestUserDetail:
    User = get_user_model()
    
    # profile
    def test_profile(self, client):
        self.User.objects.create(username='testuser', password='testpassword')
        assert client.get('/users/testuser/').status_code == 200

    def test_profile_not_exist(self, client):
        assert client.get('/users/undefined/').status_code == 404


    # update
    def test_update_password(self, client, mock_test_user):
        body = {
            'password': 'testpassword',
            'newPassword': 'aweku398*&',
            'newPasswordConfirmation': 'aweku398*&',
        }
        assert client.patch(f'/users/{mock_test_user["user"].username}/', body, headers={'Authorization': mock_test_user["token"]}).status_code == 200

    def test_update_password_contain_blank(self, client):
        body = {
            'password': 'testpassword',
            'newPassword': 'awek u398*&'
        }
        assert client.patch('/users/testuser/', body).content == 400