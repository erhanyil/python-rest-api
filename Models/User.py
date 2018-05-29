from DatabaseLibrary import DatabaseLibrary

class User:
    userID = None
    userName = None
    userFirstName = None
    userLastName = None
    password = None
    userEmail = None

    def __init__(self, id = 0):
        return DatabaseLibrary().set(self, id)