import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "iloveoksanka",
    database="salary_counter"
)

mycursor = mydb.cursor()

sqlWorker = "INSERT INTO workers (name, date, whole, salary, margin) VALUES (%s,%s, %s, %s, %s); SELECT * FROM workers ORDER BY name"

name = input("Name: ")
date = input("When did you work? ")
# date = datetime.datetime.today()
whole = int(input("How much did you make today?: "))
salary = int(whole * 0.4)

def sal():
    for month_salary in range(1,30):
        month_salary += salary
        return month_salary
        print(month_salary)

margin = int(whole * 0.6)

workers = (name, date, whole, salary, margin)

# sqlDate = "SELECT * FROM workers ORDER BY name"

mycursor.execute(sqlWorker, workers)


# mycursor.execute(sqlDate)
myresult = mycursor.fetchmany()

for r in myresult:
    print(r)









# How can i count salary bu mounths?
#
# 1. Create a dict with id for every month.
# 2. Throw a for on dates column in MySql and split every date to extract month and find its key in the dict.
# 3. Throw for on dates column in MySql and while month == key in dict add all salary together
#
#
#
# SELECT MONTH(date)
#
# curmonth = 0
# wage = 0
# for month in sql date:
#     curmonth = MONTH
#         while MONTH == curmonth:
#             wage += salary



# розрахунок оксаниної зарплати


# Програма із вводом кількості робочих днів.

# def salary():
#     days = int(input("За скільки днів рахуємо зарплату, сонце)? "))
#     amount = 0
#     for n in range(days):
#         a = int(input("Вводь суму: "))
#         b = (40 * a) / 100
#         amount += b
#         print(amount)
#     print ("За %s днів ти заробила %d гривень!" % (days, amount))



# Програма без вводу кількості днів.

# def salary():
#     salary = 0
#     for n in range(0, 100):
#         a = int(input("Вводь суму: "))
#         if a == 0:
#             break
#         else:
#             b = (40 * a) / 100
#             salary += b
#     print ("Ти заробила %d гривень!" % salary)
#
# salary()

mydb.commit()


# Deleting whole table.
# sql = "DROP TABLE IF EXISTS workers"

# Show all workers upsidedown
# sql = "SELECT * FROM workers ORDER BY age DESC"

# Here I can find smeone whose name starts with O
# sql = "select * from workers WHERE name LIKE 'O%'"

# Here I can find name Oksanka and update her age to 21
# sql = "UPDATE workers SET age = 21 WHERE name = 'Oksanka'"

# Here I created mu table for workers
# mycursor.execute("CREATE TABLE workers (id INTEGER(20), name VARCHAR(255), date DATE, whole INTEGER(255), salary INTEGER(255))")


# mycursor.execute("SHOW TABLES")


# myresult = mycursor.fetchall()

# for db in mycursor:
#     print(db)

# sqlFormula = "INSERT INTO workers (id, name, whole, salary) VALUES (%s, %s, %s, %s)"
# workers = [(1, "Oksanka", 2039, 1005),
#             (2, "Oksanka", 2039, 1005),
#             (3, "Oksanka", 2039, 1005),
#             (4, "Oksanka", 2039, 1005),
#             (5, "Oksanka", 2039, 1005)]
#
# mycursor.executemany(sqlFormula, workers)

# this line is saving all the changes
# mydb.commit()

# for tb in mycursor:
#     print(tb)
