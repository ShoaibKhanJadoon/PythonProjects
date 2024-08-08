import time as t

timeInSec = t.time()
timeinUTC=timeInSec+5*3600
localTime = t.localtime(timeinUTC)

formatedYear = t.strftime("%Y", localTime)
formatedDay = t.strftime("%d", localTime)
formatedMonth = t.strftime("%m", localTime)
formatedHour = t.strftime("%H", localTime)
formatedMinute = t.strftime("%M", localTime)
formatedSecond = t.strftime("%S", localTime)
time=formatedYear, formatedMonth, formatedDay, formatedHour, formatedMinute,formatedSecond


if formatedHour > "12":
  formatedHour=int(formatedHour)-12
  formatedHour=str(formatedHour)
  period="PM"
  time=formatedYear, formatedMonth, formatedDay, formatedHour,           formatedMinute,formatedSecond
  
elif formatedHour=="12":
  period="PM"
elif formatedHour=="0":
  period= "AM"
else:
  period="AM"

print(time)
name=input("Enter Your Name:")
if period == "AM" and "04" <= formatedHour < "12":
  print("Good Morning")
elif period == "PM" and formatedHour >= "01":
  print("Good Afternoon")
elif period == "PM" and formatedHour == "05":
  print("Good Evening")

  


