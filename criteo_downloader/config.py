"""Configures access to the Criteo API"""

class CriteoAccount:
    """A Criteo account"""

    def __init__(self, account_name: str, username: str, password: str, token: str):
        self.account_name = account_name
        self.username = username
        self.password = password
        self.token = token
        self.platform = account_name.lower().replace(' ', '.')
        self.channel = 'retargeting'
        self.partner = 'criteo'

    def __repr__(self) -> str:
        """A self representation of the account"""
        return '<{accountname} {username} {password} {token}>'.format(accountname=self.account_name,
                                                                      username=self.username,
                                                                      password=self.password,
                                                                      token=self.token)

    def __str__(self) -> str:
        """A human-readable representation of the account"""
        return 'CriteoAccount: ' + self.account_name

    @property
    def normalized_name(self) -> str:
        """The normalized name of the Criteo account
            e.g "MY Account DE" => "my_account_de"

        Returns: A lower cased name with underscores between words

        """
        return self.account_name.lower().replace(' ', '_')


def data_dir() -> str:
    """The directory where result data is written to"""
    return '/tmp/criteo'


def first_date() -> str:
    """The first day for which data is downloaded"""
    return '2015-01-01'


def accounts() -> [CriteoAccount]:
    """A list of Criteo accounts provided by <accountname username password token> Accepts multiple accounts"""
    return [CriteoAccount('accountname', 'username', 'password', 'token')]


def retry_attempts() -> int:
    """How many times retry to download an account before giving up"""
    return 5


def retry_timeout() -> int:
    """How many seconds to wait before retrying to download an account"""
    return 30


def redownload_window() -> int:
    """The number of days for which the performance data will be redownloaded"""
    return 30
