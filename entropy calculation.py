import math

def make_group_len3(worker_list):  # Создаем группы из 4 worker
	group = worker_list[:4]
	worker_list = worker_list[4:]
	return worker_list, group

def found_goals(group): # Вычисляем общие цели
	group_purposes = []
	for i in group:
		#print(i['цель'])
		group_purposes.append(i['цели'])  # m - общее кол-во целей
	m = group_purposes
	n = len(group_purposes) - len(set(group_purposes)) # n - Кол-во общих целей
	return m, n



worker1 = {'name': 'Alex', 'work': 'operator', 'задачи': 'Управление станком', 
			'цели': 'Выпуск продукции', 'ресурсы': None }
worker2 = {'name': 'Bob', 'work': 'operator', 'задачи': 'Управление станком', 
			'цели': 'Выпуск продукции' , 'ресурсы': 'R' }
worker3 = {'name': 'Den', 'work': 'gruzchik', 'задачи': 'Подсобные работы' , 
			'цели': 'Выполнение поставленых задач', 'ресурсы': None}
worker4 = {'name': 'Viktor', 'work': 'gruzchik', 'задачи': 'Подсобные работы', 
			'цели': 'Выполнение поставленых задач', 'ресурсы': None}
worker5 = {'name': 'Katy', 'work': 'otk', 'задачи': 'Контроль качества' , 
			'цели': 'Выпуск продукции' , 'ресурсы': None}
worker6 = {'name': 'Peter', 'work': 'kladovschik', 'задачи': 'Складские работы' , 
			'цели': 'Учет продукции' , 'ресурсы': None}
worker7 = {'name': 'Sergey', 'work': 'gruzchik', 'задачи': 'Подсобные работы' , 
			'цели': 'Выполнение поставленых задач', 'ресурсы': None}
worker8 = {'name': 'Anton', 'work': 'naladchik', 'задачи': 'Наладка оборудования', 
			'цели': 'Исправность оборудования', 'ресурсы': None}
worker9 = {'name': 'Mike', 'work': 'manager', 'задачи': 'Поиск клиентов', 
			'цели': 'Заключение договора', 'ресурсы': None}
worker10 = {'name': 'Ivan', 'work': 'manager', 'задачи': 'Поиск клиентов', 
			'цели': 'Заключение договора', 'ресурсы': None}
worker11 = {'name': 'Semen', 'work': 'tehnolog', 'задачи': 'Создание УП', 
			'цели': 'Разработка ТП', 'ресурсы': None}
worker11 = {'name': 'John', 'work': 'tehnolog', 'задачи': 'Создание УП', 
			'цели': 'Разработка ТП', 'ресурсы': None}

worker_list = (worker1, worker2, worker3, worker4, worker5, worker6, worker7, worker8, worker9, worker10, worker11,)
group_1 ={}
group_2 ={}
group_3 ={}
worker_list, group_1 = make_group_len3(worker_list)
worker_list, group_2 = make_group_len3(worker_list)
worker_list, group_3 = make_group_len3(worker_list)
m_1, n_1 = found_goals(group_1)  
""" m - Кол-во целей группы, n- Кол -во общих целей"""
m_2, n_2  = found_goals(group_2)
m_3, n_3  = found_goals(group_3)
print(f'Кол-во целей группы {len(m_1)}')
print(f'Кол-во общих целей группы {n_1}')

p = len(m_1) - n_1
print(p)
#e = math.log2(p) * p
#print(e)