# add the params for an API here

from pydantic import BaseModel

class Telegram(BaseModel):
    channel_name: str
