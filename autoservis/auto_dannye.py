from database import Auto, Client, get_session
import random

session = get_session()

clients = session.query(Client).all()

bukva = ['A', 'B', 'C', 'D', 'H', 'F', 'X', 'T', 'K', 'P']
marka = ['AUDI', 'VOLVO', 'FORD', 'LADA', 'BMW', 'LEXUS', 'PORCH', 'LAMBORGHINI', 'HONDA', 'MITSUBISHI']

# auto1 = Auto(number_auto='A001AA', id_client=clients[0].id_client, marka='Ford')
# session.add(auto1)

# auto2 = Auto(number_auto='A002AA', id_client=clients[1].id_client, marka='Lada')
# session.add(auto2)
#
# auto3 = Auto(number_auto='A003AA', id_client=clients[2].id_client, marka='lada')
# session.add(auto3)
# #
# auto4 = Auto(number_auto='A004AA', id_client=clients[3].id_client, marka='BMW')
# session.add(auto4)
# #
# auto5 = Auto(number_auto='A005AA', id_client=clients[4].id_client, marka='AUDI')
# session.add(auto5)
#
# auto6 = Auto(number_auto='A006AA', id_client=clients[5].id_client, marka='INFINITI')
# session.add(auto6)
#
# auto7 = Auto(number_auto='A007AA', id_client=clients[6].id_client, marka='HONDA')
# session.add(auto7)
#
# auto8 = Auto(number_auto='A008AA', id_client=clients[7].id_client, marka='RENAULT')
# session.add(auto8)
#
# auto9 = Auto(number_auto='A009AA', id_client=clients[8].id_client, marka='TOYOTA')
# session.add(auto9)
#
# auto10 = Auto(number_auto='A010AA', id_client=clients[9].id_client, marka='МОСКВИЧ')
# session.add(auto10)

for h in range(10):
    i = random.randint(0, 9)
    j = random.randint(0, 9)
    k = random.randint(0, 9)
    n = random.randint(1, 999)
    session.add(Auto(number_auto=f"{bukva[i]}{n if n > 100 else '0' + str(n) if n > 10 else '00' + str(n)}{bukva[j]}{bukva[k]}", id_client=clients[h].id_client, marka=f"{marka[h]}"))

session.commit()
session.close()
