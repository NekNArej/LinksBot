from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int

@dataclass
class Client:
    api_id: int
    api_hash: str
@dataclass
class Settings:
    bots: Bots
    client: Client


def get_settings(path: str):
    env=Env()
    env.read_env(path)
    return Settings(
        bots= Bots(
            bot_token=env.str("TOKEN"),
            admin_id=env.int("ADMIN_ID")
        ),
        client= Client(
            api_id=env.int("API_ID"),
            api_hash=env.str("API_HASH")
        ) 
    )

settings=get_settings('linkschack.env')












