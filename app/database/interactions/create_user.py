from database.models.profiles import Profile

def create_user_profile(user_data):
    profile_data = {
        "username": user_data.username,
        "about": user_data.about,
        "first_name": user_data.first_name,
        "last_name": user_data.last_name
    }
    create = Profile.create(**profile_data)
    return {"user created with id" : create.id}
