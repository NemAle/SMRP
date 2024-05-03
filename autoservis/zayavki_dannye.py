from database import Zayavki, Client, get_session
import random

session = get_session()

clients = session.query(Client).all()

for i in range(10):
    m = random.randint(1, 30)
    n = random.randint(1, 12)
    session.add(Zayavki(data=f"{m if m >= 10 else '0' + str(m)}.{n if n >= 10 else '0' + str(n)}.2024", id_client=clients[i].id_client))

session.commit()

session.close()
