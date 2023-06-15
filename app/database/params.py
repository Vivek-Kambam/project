# add the params for an API here
# import pydantic
from pydantic import BaseModel
# import Basemodel

class UserProfile(BaseModel):
    username : str
    about : str = None
    first_name :str  
    last_name :str
    email_address : str = None
    mobile_number : int = None
    country_code : str = None
    address : str = None

    # def __init__(self, usename, about, first_name, last_name) -> None:
    #     username = self.username
    #     about = self.about
    #     first_name = self.first_name
    #     last_name = self.last_name
    #     pass