from database import Uslugi, get_session
import random

session = get_session()

usl = ['Замена масла и фильтров', 'Установка дополнительного оборудования','Установка сигнализаций и иммобилайзеров','Замена аккумуляторов','Диагностика и ремонт электрооборудования','Компьютерная диагностика','Диагностика и ремонт ходовой части','Диагностика и ремонт трансмиссий','Диагностика и ремонт двигателей','Замена ремня ГРМ','Замена свечей зажигания','Замена тормозных колодок и дисков']

for i in range(10):
    cena = random.randint(500, 10000)
    cena = int(cena / 10) * 10
    idi = random.randint(1000, 9999)
    session.add(Uslugi(id_uslugi=idi, remont=usl[i], cena=cena))

session.commit()

session.close()
