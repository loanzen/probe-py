from apiclient.exceptions import ApiException


class FieldEmptyException(ApiException):

    def __init__(self, name):
        super(FieldEmptyException, self).__init__(
            '{} can not be empty'.format(name))


class UnSupportedIDException(ApiException):

    def __init__(self):
        super(UnSupportedIDException, self).__init__(
            'Id is not supported')