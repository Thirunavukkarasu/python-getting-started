def add_time(start, duration):
    new_time = ""
    start_hour, start_period = start.split(" ")
    ex_hour, ex_minute = start_hour.split(":")
    in_hour, in_minute = duration.split(":")

    cur_minute = int(ex_minute) + int(in_minute)
    add_hours = 0
    if cur_minute > 60:
        add_hours = round(cur_minute / 60)
        cur_minute = cur_minute % 60
    cur_hour = int(ex_hour) + int(in_hour) + add_hours

    print(cur_hour)
    if cur_hour >= 12:
        final_hour = cur_hour - 12 if cur_hour > 12 else cur_hour
        final_period = "AM" if start_period == "PM" else "PM"
    else:
        final_hour = cur_hour
        final_period = start_period

    new_time = f"{final_hour}:{str(cur_minute).rjust(2,'0')} {final_period}"
    return new_time
