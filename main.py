import requests
import json
from generator.emailGen import generate_email
from generator.nameGen import generate_username
from generator.passwordGen import generate_password
from models.user import UserModel


url = "http://127.0.0.1:5000/register"


def main():
    for i in range(10000):
        user = UserModel(generate_username(), generate_email(), generate_password())
        response = requests.post(url, json=user.to_dict())
        print(f"{user.username} [{'CREATED' if response.status_code == 200 else 'FAILED'}] ({response.status_code})")
        if response.status_code == 200:
            with open ("data.json", "a") as f:
                json.dump(user.to_dict(), f, indent=4)
                f.write(",\n")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
