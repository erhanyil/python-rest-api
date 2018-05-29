from DatabaseLibrary import DatabaseLibrary

class UserRepo:
    
    dbl = None

    def __init__(self):
        self.dbl = DatabaseLibrary()
    
    def getAllUsers(self, id):
        if id == "":
            return self.dbl.execute("SELECT * FROM tblusers")
        else:
            return self.dbl.execute("SELECT * FROM tblusers WHERE userID = %s", [id])

    def get_user(self):
        return "get_user"
