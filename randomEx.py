import random
import string


def generate_random_username_email(domain=None, prefix=None):

    if not domain:
        domain = "randomtest.com"
    if not prefix:
        prefix = "testuser"

    random_string = "".join(random.choices(string.ascii_lowercase, k=10))
    username = prefix + "." + random_string
    email = prefix + "_" + random_string + "@" + domain

    random_info = {'username': username, 'email': email}

    return random_info

rnd = generate_random_username_email()
print(rnd)

print(random.randint(1, 100))
