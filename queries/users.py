from .client import Queries
from models import User

class UserQueries(Queries):
    DB_NAME = "email_service"
    COLLECTION = "users"
    
    def get_one(self, email):
        user = self.collection.find_one({"email": email})
        if user:
           return User(**user) 
        else:
            return None