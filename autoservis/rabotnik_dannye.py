from database import Rabotnik, Uslugi, Zayavki, get_session
import random

post = ['Электрик', 'Ходовщик', 'Моторист', 'Диагност', 'Автослесарь', 'Автомеханик']
name = ['Павлинин Ян Олегович', 'Бажуков Евгений Леонидович', 'Анферов Вадим Георгиевич', 'Волк Дмитрий Анатольевич','Костолом Олег Александрович','Реаниматов Ренат Радомирович','Васильев Артур Александрович','Айба Александр Николаевич','Новорожденнов Валентин Андреевич','Бонько Ян Евгеньевив']

session = get_session()
zayavki = session.query(Zayavki).all()
uslugi = session.query(Uslugi).all()

for i in range(10):
    j = random.randint(0, 5)
    session.add(Rabotnik(id_uslugi=uslugi[i].id_uslugi, id_zayavki=zayavki[i].id_zayavki, full_name_rab=name[i], post=post[j]))

session.commit()

session.close()
