from functools import reduce


# 1
# volume = reduce((lambda x, y: x * y), range(1, int(input())+1))
# volume = reduce((lambda x, y: x * y), map(int, input().strip().split()))
# print(f'{volume=}')

# 2 comprehensions
# names = ["John", "Bob", "Andrey", "Tommy", "Alex"]
# names_starts_a = []
# for name in names:
#     if name.startswith('A'):
#         names_starts_a.append(name)
# names_starts_a =[name for name in names if name.startswith('B')]
# print(names_starts_a)

# 3 filter
names = ["John", "Bob", "Andrey", "Tommy", "Alex"]
names_starts_a = filter(lambda name: name.startswith('T'), names)
print(tuple(names_starts_a))

# 4 copy array
numbers = [1,2,3]
another_numbers = numbers[:]

# 5 обратить список
another_numbers = numbers[::-1]

# all/ any вместо сложного if
a = b = c = d = e = True
# if all((a, b, c, d, e)):
if any((a, b, c, d, e)):
    print("All True")

# 6 Тернарный оператор
admin_email = "admin@site.ru" if config.IS_PRODUCTION else "mymail@mail.com"


# 7 Конфигурирование
class User:
    def __init__(self, group: str):
        self.group = group

user = User(group="admin")

# if user.group == "admin":
#     process_admin_request(user, request)
# elif user.group == "manager":
#     process_manager_request(user, request)
# elif user.group == "client":
#     process_client_request(user, request)

# настройка логики
group_to_process_method = {
    "admin": process_admin_request,
    "manager": process_manager_request,
    "client": process_client_request,
}

# Программирование
group_to_process_method[user.group](user, request)