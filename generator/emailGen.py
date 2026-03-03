from resources import data
import random


def generate_email():
    return random.choice(data.email_name)+ random.choice(data.name_salt) + random.choice(data.email_salt) + "@" + random.choice(data.email_name_ext)