import datetime
from datetime import date
birthday=input("When is your birthday ['yyyy-mm-dd' format] : ")
birthday=datetime.datetime.strptime(birthday,"%Y-%m-%d").date()
today = datetime.date.today()
age = (birthday-today)
print("There are" + " " +str(age.days)+" " + "days until your next birthday")

