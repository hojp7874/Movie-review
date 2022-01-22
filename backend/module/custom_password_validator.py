from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class ExcludeValidator(object):
    """
    비밀번호에 제외대상 문자들이 포함되었는지 확인합니다.
    """
    def __init__(self, exclude_texts=[' ']):
        self.exclude_texts = exclude_texts

    def validate(self, password, user=None):
        for exclude_text in self.exclude_texts:
            if exclude_text in password:
                raise ValidationError(
                    _(f"비밀번호에 잘못된 문자가 포함되어있습니다. '{exclude_text}' 문자를 제외해야 합니다."),
                    code='password_excluded_text',
                )

    def get_help_text(self):
        return _(f"비밀번호는 {self.exclude_texts} 문자들을 포함할 수 없습니다.")
