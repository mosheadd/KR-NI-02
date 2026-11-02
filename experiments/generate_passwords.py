import random
import string
from pathlib import Path


filepath = "experiments/input_data/passwords.txt"


def create_folder_and_file():
    file_path = Path(filepath)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    file_path.touch(exist_ok=True)

def generate():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    generate_one = lambda length: ''.join(random.choice(characters) for i in range(length))

    passwords = [generate_one(random.randint(8, 20)) for _ in range(1000)]

    with open(filepath, "w") as f:
        for password in passwords:
            f.write(f"{password}\n")



if __name__ == "__main__":
    create_folder_and_file()
    generate()
    print("Passwords generated and written in a file successfully")
