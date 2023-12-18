import random

from faker import Faker

fake = Faker()

fileWrite = open("data.txt", "w")

# systum hang
for i in range(10000):
    id = i
    fname = fake.first_name()
    lname = fake.last_name()
    gender = random.choice(["male", "female"])
    email = fake.email()

    fileWrite.write(
        f"INSERT INTO user_data (id, fname, lname, gender, email) VALUES ({id}, '{fname}', '{lname}', '{gender}', '{email}');\n"
    )

fileWrite.close()
