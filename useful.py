from pprint import pprint
import csv


# users = [{
#     "name": "Вася",
#     "phone": "123",
#     "email": "vasya@gmail.com",
#     "department": "Красауцы"
# },{
#     "name": "Петя",
#     "phone": "123"
# }]
# pprint(users)

# with open("file.txt", "w") as f:
#     f.write("Привеееет!")

# with open("file.txt", "r") as f:
#     content = f.read()
#
# print(content)

# with open("users.csv", "w", encoding="cp1251") as f:
with open("users.csv", "w") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(["Леша", "lesha@mail.ru"])
    writer.writerow(["Вася", "vasya@gmail.com"])
    writer.writerow(["Петр", "petr@ya.ru"])""