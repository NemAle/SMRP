from database import Client, get_session

session = get_session()

client1 = Client(full_name_cl='Петров Иван Алексеевич', telephone='89223489213')
session.add(client1)

client2 = Client(full_name_cl='Иванов Петр Валентинович', telephone='89563215796')
session.add(client2)

client3 = Client(full_name_cl='Сидоров Михаил Егорович', telephone='83569784152')
session.add(client3)

client4 = Client(full_name_cl='Соколов Артем Максимович', telephone='8154879652')
session.add(client4)

client5 = Client(full_name_cl='Романова Олльга Анатольевна', telephone='8569847523')
session.add(client5)

client6 = Client(full_name_cl='Орлов Игорь Тимофеевич', telephone='89562147598')
session.add(client6)

client7 = Client(full_name_cl='Титов Андрей Николаевич', telephone='89651248634')
session.add(client7)

client8 = Client(full_name_cl='Козлова Анна Владимировна', telephone='8956478216')
session.add(client8)

client9 = Client(full_name_cl='Орлов Тимофей Игоревич', telephone='832154896578')
session.add(client9)

client10 = Client(full_name_cl='Волков Николай Степанович', telephone='812546978546')
session.add(client10)

session.commit()

session.close()
