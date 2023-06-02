class UserPasswordInfo:
    """
    To store data from Add Password
    """

    def __init__(self, password: str, title: str, url: str, username: str):
        self.password = password
        self.title = title
        self.url = url
        self.username = username


class UserData:
    # TODO: need to also store  passwords  email that user store

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.addedUserPasswordArr = []

    def add_password(self, addedUserPassword: UserPasswordInfo):
        self.addedUserPasswordArr.append(addedUserPassword)
