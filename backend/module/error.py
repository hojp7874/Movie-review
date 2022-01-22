class ConfirmError(Exception):
    def __init__(self):
        super().__init__('패스워드가 일치하지 않습니다.')