import pytest

from module.custom_password_validator import ExcludeValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class TestExcludeValidator:
    # validate
    def test_correct_password(self):
        exclude_texts = [' ']
        validator = ExcludeValidator(exclude_texts=exclude_texts)
        password = 'ab#09sd90'

        validator.validate(password=password, user=get_user_model())
        assert True

    def test_mono_text(self):
        exclude_texts = ['ecdtxt']
        validator = ExcludeValidator(exclude_texts=exclude_texts)
        password = '2k@ecdtxtBs8fd'

        with pytest.raises(ValidationError):
            validator.validate(password=password, user=get_user_model())

    def test_poly_text(self):
        exclude_texts = [' ', '#']
        validator = ExcludeValidator(exclude_texts=exclude_texts)
        password1 = 'ab#09sd90'
        password2 = 'ka38f*0& '

        with pytest.raises(ValidationError):
            validator.validate(password=password1, user=get_user_model())
        with pytest.raises(ValidationError):
            validator.validate(password=password2, user=get_user_model())

    # get_help_text
    def test_help_text(self):
        exclude_texts = ['a', 'b', 'c']
        validator = ExcludeValidator(exclude_texts=exclude_texts)
        assert validator.get_help_text() == f'비밀번호는 {exclude_texts} 문자들을 포함할 수 없습니다.'