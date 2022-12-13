import os
import random

import faker
import psycopg2
import uuid

from time import sleep


def main():
    if os.getenv("RUNTIME_ENVIRONMENT") == "DOCKER":
        postgres_host = "postgres"
    else:
        postgres_host = "localhost"
    conn = psycopg2.connect(
        host=postgres_host, database="postgres", user="postgres", password="postgres"
    )
    cur = conn.cursor()

    fake = faker.Faker()

    while True:
        user_id = str(uuid.uuid4())
        cur.execute(
            f"INSERT INTO public.user (id, name, email, address) VALUES ('{user_id}','{fake.name()}','{fake.email()}','{fake.address()}');"
        )

        for i in range(random.randint(5, 15)):
            cur.execute(
                f"INSERT INTO public.payment (id, user_id, amount) VALUES ('{uuid.uuid4().hex}','{user_id}','{random.randint(1, 100)}');"
            )
            sleep(1)
        conn.commit()
        sleep(2)


if __name__ == "__main__":
    sleep(10)  # wait for db
    main()
