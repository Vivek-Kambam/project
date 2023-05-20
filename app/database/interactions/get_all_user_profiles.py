from database.models.profiles import Profile


def get_all_user_profiles():
    profile_data = Profile.select().execute()

    return profile_data