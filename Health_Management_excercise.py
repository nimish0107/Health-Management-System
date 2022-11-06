logreadadd=int(input("Enter 1 to log the data,\n2 to read the data,\n3 to add a new client:"))
if logreadadd!=3:
    food_or_excercise=int(input("Enter 1 for excercise data and enter 2 for food data:"))
print("Registered clients are:")
with open("clients_list.txt") as p:
    cont=p.read()
    print(cont)
clients=str(input("Enter client's name:"))
clients=clients.capitalize()
food_file=clients+"Food.txt"
excercise_file=clients+"Excercise.txt"
def add():
    with open(food_file, "w") as f:
        c=f.write("This is a log of ")
        c=f.write(clients)
        c=f.write("\'s food\n")
    with open(excercise_file, "w") as e:
        c=e.write("This is a log of ")
        c=e.write(clients)
        c=e.write("\'s excercise\n")
    with open("clients_list.txt","a") as g:
        c=g.write(clients)
        c=g.write("\n")
    print("This client is now registered with us")
def getdate():
    import datetime
    return datetime.datetime.now()
date_time=str(getdate())
L=[]
x=L.append(date_time)
Date_Time=str(L)
def log():
    stats=input("Enter the stats you want to input:")
    if food_or_excercise==2:
        with open(food_file, "a") as f:
            f.write(Date_Time)
            f.write(stats)
            f.write("\n")
    elif food_or_excercise==1:
        with open(excercise_file, "a") as f:
            f.write(Date_Time)
            f.write(stats)
            f.write("\n")
def read():
    if food_or_excercise==2:
        with open(food_file) as f:
            content=f.read()
            print(content)
    elif food_or_excercise==1:
        with open(excercise_file) as f:
            content = f.read()
            print(content)
if logreadadd==3:
    add()
elif logreadadd==1:
        log()
elif logreadadd==2:
        read()
else:
        print("not a valid argument according to demand")



# The one made before but then i thought of the above one


# Health Management system
# >>>we are a physical trainer and we have to create a log of their diet and excercise
# 3 clients>>>Harry,Rohan,Hammad
# 3 files to create a log for their food and 3 file for excercise
# write a function that when executed takes as input client name
"""
use this function to take time and input
def getdate():
    import datetime
    return datetime.datetime.now()
"""
# #one more function to retrieve excercise or food offered
# log_or_read=int(input("Enter 1 to log the data and enter 2 to read the data:"))
# food_or_excercise=int(input("Enter 1 for excercise data and enter 2 for food data:"))
# clients=int(input("Enter 1 for Harry,\nEnter 2 for Rohan,\nor Enter 3 for Hammad:\n"))
# # # code used to make files
# # with open("HarryExcercise.txt","w") as HarryExcercise:
# #     c=HarryExcercise.write("This is a Log of Haary's excercise\n")
# # with open("HarryFood.txt","w") as HarryFood:
# #     d=HarryFood.write("This is a Log of Haary's food\n")
# # with open("RohanExcercise.txt","w") as RohanExcercise:
# #     e=RohanExcercise.write("This is a Log of Rohan's excercise\n")
# # with open("RohanFood.txt","w") as RohanFood:
# #     f=RohanFood.write("This is a Log of Rohan's food\n")
# # with open("HammadExcercise.txt","w") as HammadExcercise:
# #     g=HammadExcercise.write("This is a Log of Hammad's excercise\n")
# # with open("HammadFood.txt","w") as HammadFood:
# #     h=HammadFood.write("This is a Log of Hammad's food\n")
# def getdate():
#     import datetime
#     return datetime.datetime.now()
# if log_or_read==1:
#     date_time = str(getdate())
#     L=[]
#     x=L.append(date_time)
#     y=str(L)
#     if food_or_excercise==1:
#         excercise_stats=input("Enter your excercise stats:")
#         if clients==1:
#             with open("HarryExcercise.txt","a") as HarryExcercise1:
#                 HarryExcercise1.write(y)
#                 HarryExcercise1.write(excercise_stats)
#                 HarryExcercise1.write("\n")
#         elif clients == 2:
#             with open("RohanExcercise.txt", "a") as RohanExcercise1:
#                 RohanExcercise1.write(y)
#                 RohanExcercise1.write(excercise_stats)
#                 RohanExcercise1.write("\n")
#         elif clients == 3:
#             with open("HammadExcercise.txt", "a") as HammadExcercise1:
#                 HammadExcercise1.write(y)
#                 HammadExcercise1.write(excercise_stats)
#                 HammadExcercise1.write("\n")
#         else:
#             print("Not a valid client")
#     elif food_or_excercise==2:
#         food_stats=input("Enter your food stats:")
#         if clients==1:
#             with open("HarryFood.txt","a") as HarryFood1:
#                 HarryFood1.write(y)
#                 HarryFood1.write(food_stats)
#                 HarryFood1.write("\n")
#         elif clients == 2:
#             with open("RohanFood.txt", "a") as RohanFood1:
#                 RohanFood1.write(y)
#                 RohanFood1.write(food_stats)
#                 RohanFood1.write("\n")
#         elif clients == 3:
#             with open("HammadFood.txt", "a") as HammadFood1:
#                 HammadFood1.write(y)
#                 HammadFood1.write(food_stats)
#                 HammadFood1.write("\n")
#         else:
#             print("Not a valid client")
#     else:
#         print("please choose a valid food or excercise option")
# elif log_or_read==2:
#     if food_or_excercise==1:
#         if clients==1:
#             with open("HarryExcercise.txt") as HarryExcercise2:
#                 content=HarryExcercise2.read()
#                 print(content)
#         elif clients==2:
#             with open("RohanExcercise.txt") as RohanExcercise2:
#                 content=RohanExcercise2.read()
#                 print(content)
#         elif clients==3:
#             with open("HammadExcercise.txt") as HammadExcercise2:
#                 content=HammadExcercise2.read()
#                 print(content)
#         else:
#             print("Not a valid client")
#     elif food_or_excercise==2:
#         if clients==1:
#             with open("HarryFood.txt") as HarryFood2:
#                 content=HarryFood2.read()
#                 print(content)
#         elif clients==2:
#             with open("RohanFood.txt") as RohanFood2:
#                 content=RohanFood2.read()
#                 print(content)
#         elif clients==3:
#             with open("HammadFood.txt") as HammadFood2:
#                 content=HammadFood2.read()
#                 print(content)
#         else:
#             print("Not a valid client")
#     else:
#         print("please choose valid food or excercise option")
# else:
#     print("please choose a valid log or read stats")