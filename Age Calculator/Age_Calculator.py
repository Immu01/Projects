# Age Calculator

import time
from datetime import datetime, date, timedelta
from calendar import isleap

def leap_year(year):
    return isleap(year)

def month_days(month,leap):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2 and leap:
        return 29
    elif month == 2 and (not leap):
        return 28
    return 0

name = input("Enter your name : ")
while True:
    dob_str = input("Enter your date of birth (YYYY-MM-DD) : ")
    try:
        birth_dt = datetime.strptime(dob_str,"%Y-%m-%d")
        break
    except ValueError:
        print("Invalid date format, Please use this format -> YYYY-MM-DD")

current_dt = datetime.now()
current_date = current_dt.date()
calc_date = birth_dt.date()
age_years = 0
age_months = 0
age_days = 0

while True:
    try:
        next_yr_date = calc_date.replace(year=calc_date.year+1)
    except ValueError:
        next_yr_date = date(calc_date.year+1,2,28)
    if next_yr_date <= current_date:
        age_years += 1
        calc_date = next_yr_date
    else:
        break

while True:
    try:
        if calc_date.month == 12:
            next_mo_date = calc_date.replace(year=calc_date.year+1,month=1)
        else:
            next_mo_date = calc_date.replace(month=calc_date.month+1)
    except ValueError:
        if calc_date.month == 12:
            next_mo_date = date(calc_date.year+1,1,1)-timedelta(days=1)
        else:
            next_mo_date = date(calc_date.year,calc_date.month+1,1)-timedelta(days=1)

    if next_mo_date <= current_date:
        age_months += 1
        calc_date = next_mo_date
    else:
        break

age_days = (current_date-calc_date).days
birth_sec_midnight = birth_dt.hour*3600+birth_dt.minute*60+birth_dt.second
curr_sec_midnight = current_dt.hour*3600+current_dt.minute*60+current_dt.second
time_diff_sec = 0

if curr_sec_midnight < birth_sec_midnight:
    age_days -= 1
    time_diff_sec = (24*3600-birth_sec_midnight)+curr_sec_midnight
else:
    time_diff_sec = curr_sec_midnight-birth_sec_midnight
sec = time_diff_sec%60
min = (time_diff_sec//60)%60
hr = (time_diff_sec//3600)%24

if age_days < 0:
    age_months -= 1
    prev_mo_year = calc_date.year
    prev_mo = calc_date.month - 1
    if prev_mo == 0:
        prev_mo = 12
        prev_mo_year -= 1
    age_days += month_days(prev_mo,leap_year(prev_mo_year))

age_years = max(0,age_years)
age_months = max(0,age_months)
age_days = max(0,age_days)
hr = max(0,hr)
min = max(0,min)
sec = max(0,sec)

print(f"\n{name.capitalize()}'s age :")
print(f"\n{age_years} years")
print(f"{age_months} months")
print(f"{age_days} days")
print(f"{hr} hours")
print(f"{min} minutes")
print(f"{sec} seconds")

total_months = age_years * 12 + age_months
total_sec_diff = (current_dt - birth_dt).total_seconds()
total_hours = int(total_sec_diff // 3600)
total_minutes = int(total_sec_diff // 60)

print(f"\nTotal elapsed time of {name.capitalize()} : ")
print(f"\nTotal years = {age_years}")
print(f"Total months = {total_months}")
print(f"Total hours = {total_hours}")
print(f"Total minutes = {total_minutes}")