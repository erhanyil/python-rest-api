from Repos.UserRepo import UserRepo

class userController:

    userRepo = UserRepo()

    def __init__(self):
        print("using userController")
    
    def getAllUsers(self, id = ""):
        return self.userRepo.getAllUsers(id)

    def get_user(self):
        return "get_user"

