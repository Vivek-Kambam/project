from database.models.profiles import Profile
from peewee import *


def get_all_user_profiles():
    user_data =[]
    profile_data = Profile.select().execute()

    for i in profile_data:
        data = {
            'id':i.id,
            'username': i.username,
            'name': i.first_name + i.last_name
        }
        user_data.append(data)



    return user_data