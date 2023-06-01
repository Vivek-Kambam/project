from database.models.profiles import Profile
from peewee import *
import pandas as pd


def get_all_user_profiles():
    user_data =[]
    profile_data = Profile.select().execute()

    for i in profile_data:
        data = {
            'id':i.id,
            'username': i.username,
            'name': i.first_name + ' ' + i.last_name
        }
        user_data.append(data)

    df = pd.DataFrame.from_dict(user_data)

    print (df)

    df.to_excel('profile.xlsx')



    return user_data