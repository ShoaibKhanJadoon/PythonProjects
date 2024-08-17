import time


def drinkwater(minute=0, hour=0):
  minute = minute * 60
  hour = hour * 60 * 60
  interval = minute + hour
  while True:
    print("Drink Water")
    timeinUTC = time.time() + 5 * 3600
    localTime = time.localtime(timeinUTC)
    formatedHour = time.strftime("%H", localTime)
    formatedMinute = time.strftime("%M", localTime)
    formatedSecond = time.strftime("%S", localTime)
    print(f"{formatedHour}:{formatedMinute}:{formatedSecond}")
    time.sleep(interval)


timehour = int(input("Enter interval in hour: "))
timeminute = int(input("Enter interval in minute: "))

drinkwater(timeminute, timehour)
