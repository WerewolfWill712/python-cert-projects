def add_time_in_minutes(start_hours,start_minutes,addend_hours,addend_minutes):
    return (start_hours*60)+start_minutes+(addend_hours*60)+addend_minutes

def convert_minutes_into_time(result_in_minutes):
    hours = int(result_in_minutes/60)
    is_days = hours>=24
    remaining_hours = int(hours%24) if is_days else hours
    hours_string = f'{hours if hours>10 else f"0{hours}"}' if not is_days else f'{remaining_hours if remaining_hours>10 else f"0{remaining_hours}"}'
    days = int(hours/24) if is_days else 0
    days_string = f'{days if days>10 else f"0{days}"}'
    minutes = int(result_in_minutes%60)
    minutes_string = f'{minutes if minutes>10 else f"0{minutes}"}'
    return f'{days_string}:{hours_string}:{minutes_string}'


def determine_weekdays(start_weekday,day_duration):
    if not day_duration:
        return(start_weekday.capitalize())
    start_weekday = start_weekday.lower()
    weekdays = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    if start_weekday.lower() not in weekdays:
        return None
    if int(day_duration)>7:
        day_duration = int(day_duration%7)
    return weekdays[weekdays.index(start_weekday)+int(day_duration)].capitalize()
def add_time(starting_time, addend_time, day_of_week="") -> str:
    start_hours, start_minutes, meridian = (
        int(starting_time.split()[0].split(":")[0]),
        int(starting_time.split()[0].split(":")[1]),
        starting_time.split()[1],
    )
    is_meridian = meridian == 'PM'
    if is_meridian:
        start_hours +=12
    addend_hours,addend_minutes = (
        int(addend_time.split(":")[0]),
        int(addend_time.split(":")[1])
    )
    is_weekday = True if day_of_week != "" else False
    result_in_minutes = add_time_in_minutes(start_hours,start_minutes,addend_hours,addend_minutes)
    result_days,result_hours,result_minutes = (
        convert_minutes_into_time(result_in_minutes).split(':')[0],
        convert_minutes_into_time(result_in_minutes).split(':')[1],
        convert_minutes_into_time(result_in_minutes).split(':')[2]
    )
    if is_weekday:
        result_weekday = determine_weekdays(day_of_week,result_days)
    if is_meridian:
        result_hours -= 12
    return f"{result_hours}:{result_minutes} {meridian}, {result_weekday}"
print(add_time("2:59 AM", "24:00", "saturDay"))


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
