QUERYRESPONSE_FALSE = 100
QUERYRESPONSE_TRUE = 101

STATUS_SUCCESS = 0
STATUS_INVALID_REQUEST_PARAMETERS = 1
STATUS_NOT_LOGGED_IN = 2
STATUS_UNKNOWN_REQUEST = 3
STATUS_DATABASE_ERROR = 4
STATUS_USERNAME_TOO_SHORT = 5
STATUS_USERNAME_TOO_LONG = 6
STATUS_PASSWORD_TOO_SHORT = 7
STATUS_PASSWORD_TOO_LONG = 8
STATUS_USERNAME_ALREADY_EXISTS = 9
STATUS_USERNAME_NON_ALPHANUMERIC = 10
STATUS_ALREADY_LOGGED_IN = 11
STATUS_INVALID_CREDENTIALS = 12
STATUS_USER_NOT_ONLINE = 13
STATUS_ERROR_EMPTY_MESSAGE = 14
STATUS_RECEIVER_BLOCKED = 15
STATUS_SENDER_BLOCKED = 16
STATUS_FRIEND_REQUEST_ALREADY_SENT = 17
STATUS_FRIEND_REQUEST_ALREADY_RECEIVED = 18
STATUS_ALREADY_FRIENDS = 19
STATUS_NON_EXISTENT_USER = 20
STATUS_NO_FRIEND_REQUEST = 21
STATUS_NO_FRIENDSHIP = 22
STATUS_ALREADY_BLOCKED = 23
STATUS_USER_NOT_BLOCKED = 24
STATUS_INVALID_PASSWORD = 25
STATUS_EMPTY_SONG_NAME = 26
STATUS_INVALID_SONG = 27

status_messages = {
    0: 'STATUS_SUCCESS',
    1: 'STATUS_INVALID_REQUEST_PARAMETERS',
    2: 'STATUS_NOT_LOGGED_IN',
    3: 'STATUS_UNKNOWN_REQUEST',
    4: 'STATUS_DATABASE_ERROR',
    5: 'STATUS_USERNAME_TOO_SHORT',
    6: 'STATUS_USERNAME_TOO_LONG',
    7: 'STATUS_PASSWORD_TOO_SHORT',
    8: 'STATUS_PASSWORD_TOO_LONG',
    9: 'STATUS_USERNAME_ALREADY_EXISTS',
    10: 'STATUS_USERNAME_NON_ALPHANUMERIC',
    11: 'STATUS_ALREADY_LOGGED_IN',
    12: 'STATUS_INVALID_CREDENTIALS',
    13: 'STATUS_USER_NOT_ONLINE',
    14: 'STATUS_ERROR_EMPTY_MESSAGE',
    15: 'STATUS_RECEIVER_BLOCKED',
    16: 'STATUS_SENDER_BLOCKED',
    17: 'STATUS_FRIEND_REQUEST_ALREADY_SENT',
    18: 'STATUS_FRIEND_REQUEST_ALREADY_RECEIVED',
    19: 'STATUS_ALREADY_FRIENDS',
    20: 'STATUS_NON_EXISTENT_USER',
    21: 'STATUS_NO_FRIEND_REQUEST',
    22: 'STATUS_NO_FRIENDSHIP',
    23: 'STATUS_ALREADY_BLOCKED',
    24: 'STATUS_USER_NOT_BLOCKED',
    25: 'STATUS_INVALID_PASSWORD',
    26: 'STATUS_EMPTY_SONG_NAME',
    27: 'STATUS_INVALID_SONG',
    100: 'QUERYRESPONSE_FALSE',
    101: 'QUERYRESPONSE_TRUE'
}
