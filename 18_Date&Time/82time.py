import datetime

now = datetime.datetime.now()

print(now)



target_time=datetime.datetime(2030,1,12,9,25)

current_time=datetime.datetime.now()


if target_time > current_time:
    print(f"The Target time {target_time} has not passed yet!")

else:
    print(f"The Target time {target_time} has passed! ")