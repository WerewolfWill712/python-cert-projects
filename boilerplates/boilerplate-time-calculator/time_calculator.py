def add_time(starting_time, addend_time, day_of_week="") -> str:
    start_hours, start_minutes, meridian = (
        int(starting_time.split()[0].split(":")[0]),
        int(starting_time.split()[0].split(":")[1]),
        starting_time.split()[1],
    )
    is_meridian = True if meridian == 'PM' else False
    if is_meridian:
        start_hours +=12
    addend_hours,addend_minutes = (
        int(addend_time.split(":")[0]),
        int(addend_time.split(":")[1])
    )
    is_weekday = True if day_of_week != "" else False
    print(is_weekday)
add_time("2:59 AM", "24:00", "saturDay")
# input: "2:59 AM", "24:00", "saturDay"
# expected output "2:59 AM, Sunday (next day)"
# from datetime import datetime
# from datetime import timedelta
# from datetimeReplacement import addTimeInMinutes,formatMinutes

# def convertToMillitary(time, noonSplit):
#     result = 0
#     rawTime = int("".join(time.split(time[time.find(":")])))

#     return rawTime


# def timeStringtoMinutes(time):
#     hours, minutes = int(time.split(":")[0]), int(time.split(":")[1])
#     return (hours * 60) + minutes


# def add_time(start, duration, dayOfWeek=""):
#     dayNameDict = {
#         "monday":0,
#         'tuesday':1,
#         "wednesday":2,
#         "thursday":3,
#         "friday":4,
#         'satruday':5,
#         'sunday':6
#     }
#     print(formatMinutes(addTimeInMinutes(start.split()[0],duration)))

#     isAmOrPm = False if start.split()[1] == "AM" else True
#     number = start.split()[0]
#     startInMinutes = (
#         timedelta(minutes=timeStringtoMinutes(number))
#         if not isAmOrPm
#         else timedelta(minutes=timeStringtoMinutes(number)) + timedelta(hours=12)
#     )
#     durationInMinutes = timedelta(minutes=timeStringtoMinutes(duration))
#     totalTimeRaw = startInMinutes + durationInMinutes
#     bool(dayOfWeek)
#     # print(5+dayNameDict.get(dayOfWeek.lower(),None))
#     resultAmOrPm = 'AM' if int(str(totalTimeRaw).split(',')[1].split(':')[0].strip())<12 else 'PM'
#     print(((datetime(2022,5,2+dayNameDict.get(dayOfWeek.lower(),None))+totalTimeRaw).weekday()))
# add_time("8:16 PM", "466:02", "tuesday")

# actual = add_time("8:16 PM", "466:02", "tuesday")
# expected = "6:18 AM, Monday (20 days later)"
