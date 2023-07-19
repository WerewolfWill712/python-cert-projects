def addTimeInMinutes(time,duration):
  Thours,Tminutes = int(time.split(':')[0]),int(time.split(':')[1])
  Dhours,Dminutes = int(duration.split(':')[0]),int(duration.split(':')[1])
  return ((Thours*60)+Tminutes)+((Dhours*60)+Dminutes)
# print(addTimeInMinutes('8:16','246:48'))
def formatMinutes(minutes):
  isDays = minutes>1440
  # isHours = minutes>60
  print(minutes)
  hours = int(minutes/60)
  remainingHours = hours%24
  hours+=remainingHours
  days = int(hours/24) if isDays else 0
  remainingMin = minutes%60
  return {"days":days,'hours':remainingHours,'minutes':remainingMin}


def generate_weeks(days,shift) -> list:
  arr = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  arr2 = list()
  for a in arr:
    arr2.append(a.lower())
  print(arr2)
  weekdays = shift_array(len(arr)-shift,arr)
  print(len(weekdays) - weekdays.index('saturDay'))

  if days <= 7:
    return weekdays[days-1:]

def shift_array(key, array):
    return array[-key:] + array[:-key]
print(generate_weeks(20,0))

"""pseudo code breakdown

input: "2:59 AM", "24:00", "saturDay" 
expected output "2:59 AM, Sunday (next day)"

parse inputs 
1. starting time 
2. time addend
3. optional starting day of the week


fn "base" arguements :string:starting_time, string:addend_time, string:day_of_week default is empty string
parse 1 into hours and minutes and meridian boolian
integer start_hours
integer start_minutes
boolean is_meridian
string meridian
if is_meridian start_hours + 12
parse 2 into hours and minutes
integer addend_hours
integer addend_minutes
parse 3 handle optional status verify capitalisation
bool is_weekday if day_of_week is not empty string
integer result_in_minutes => call add_time_in_minutes("parsed raw start hours start minutes addend hours addend minutes")
string result_time_raw => call convert_minutes_into_time(result_in_minutes)
if is_weekday 
  integer parse result_time_raw(result_days,result_hours,result_minutes)
  string result_weekday => call determine_weekday(result_days,day_of_week)
if is_meridian
  result_hours - 12
return result_hours + ":" + result_minutes + meridan + result_weekday if is_weekday else result_days + "days later"

fn "add_time_in_minutes" arguements :start_hours,start_minutes, addend_hours, addend_minutes
convert starting time and addend time into minutes 
return add together integer

fn "convert_mintues_into_time" arguements : result in minutes
parse into hours
determine if hours is greater than 24
if True parse into days 
determine remainders for hours (if days) and minutes
return string "days:hours:minutes"

fn "determine_weekdays" arguements : string:start_weekday, interger:day_duration
if day_duration is not truthy
  return start_weekday
parse start_weekday into lowercase
array of weekdays
if start_weekday is not existing in array of weekdays
  return None

integer remainder of day_duration divided by 7
determine weekdays index of start_weekday
add remainder to index
return weekday name from array
"""