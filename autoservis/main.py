from database import Auto, get_session

session = get_session()
autos = session.query(Auto).all()
print(autos)
for auto in autos:
    print(auto)
# auto = session.get(1)
# print(auto)
# auto=session.query(Auto).where(Auto.number_auto == '2').one()
# print(auto)
#
auto=session.query(Auto).where(Auto.number_auto == '3').one()
auto.marka = "porsh"
session.commit()

# new_auto = Auto(number_auto=8,marka="lambo",id_client=5)
# session.add(new_auto)
# print(new_auto)
# session.commit()

session.close()
