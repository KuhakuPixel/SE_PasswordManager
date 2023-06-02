


class AddedUserPassword:
    """
        To store data from Add Password
    """

    def __init__(self, password:str, title:str, url:str, username:str):
        self.password = password
        self.title = title
        self.url = url
        self.username = username


class UserData:
    # TODO: need to also store  passwords  email that user store
    addedUserPasswordArr = []
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def add_password(self, addedUserPassword:AddedUserPassword):
        self.addedUserPasswordArr.append(addedUserPassword)

