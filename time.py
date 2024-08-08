import time as t

timeInSec = t.time()
timeinUTC = timeInSec + 5 * 3600
localTime = t.localtime(timeinUTC)

formatedYear = t.strftime("%Y", localTime)
formatedDay = t.strftime("%d", localTime)
formatedMonth = t.strftime("%m", localTime)
formatedHour = t.strftime("%H", localTime)
formatedMinute = t.strftime("%M", localTime)
formatedSecond = t.strftime("%S", localTime)
time=formatedYear,formatedMonth,formatedDay,formatedHour, formatedMinute,formatedSecond

if formatedHour > "12":
  formatedHour = int(formatedHour) - 12
  formatedHour = str(formatedHour)
  period = "PM"
  time=formatedYear,formatedMonth,formatedDay, formatedHour,formatedMinute,formatedSecond

elif formatedHour == "12":
  period = "PM"
elif formatedHour == "0":
  period = "AM"
else:
  period = "AM"
print(time, period)
name = input("Enter your name: ")
formatedHour = int(formatedHour)
if period == "AM" and 4 <= formatedHour < 12:
  print("Good Morning " + name)
elif period == "PM" and 1 <= formatedHour < 5:
  print("Good Afternoon " + name)
elif period == "PM" and 5 <= formatedHour < 7:
  print("Good Evening " + name)
elif period == "PM" and 7 <= formatedHour < 12:
  print("Good Night " + name)
