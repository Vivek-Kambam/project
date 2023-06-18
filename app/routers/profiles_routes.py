from fastapi import APIRouter

from database.interactions.get_all_user_profiles import get_all_user_profiles
from database.interactions.create_user import create_user_profile
from routers.profile_params import *

profile_router = APIRouter()


@profile_router.get('/get_all_profiles')
def get_all_profiles():
    return get_all_user_profiles()

@profile_router.post('/create_user')
def create_user(user_data: UserProfile):
    return create_user_profile(user_data)
