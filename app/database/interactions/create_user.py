from database.models.profiles import Profile

def create_user_profile(user_data):
    profile_data = {
        "username": user_data.username,
        "about": user_data.about,
        "first_name": user_data.first_name,
        "last_name": user_data.last_name,
        "email_address" : user_data.email_address,
        "mobile_number" : user_data.mobile_number,
        "country_code" : user_data.country_code,
        "address" : user_data.address
    }
    create = Profile.create(**profile_data)
    return {"user created with id" : create.id}
