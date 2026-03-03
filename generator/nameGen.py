from resources import data
import random


def generate_username():
    return random.choice(data.names) + random.choice(data.surnames) + random.choice(data.name_salt)