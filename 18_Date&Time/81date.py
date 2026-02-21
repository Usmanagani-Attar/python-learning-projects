import datetime

today=datetime.date.today()

print(today)

target_date=datetime.datetime(2030,1,12)

current_date=datetime.datetime.today()


if target_date > current_date:
    print(f"The Target date {target_date} has not passed yet!")

else:
    print(f"The Target date {target_date} has passed! ")