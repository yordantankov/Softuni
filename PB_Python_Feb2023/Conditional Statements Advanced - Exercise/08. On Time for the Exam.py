exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

exam_total_minutes = exam_hour * 60 + exam_minute
arrive_total_minutes = arrive_hour * 60 + arrive_minute

if arrive_total_minutes > exam_total_minutes:
    print("Late")
elif exam_total_minutes - arrive_total_minutes <= 30:
    print("On time")
else:
    print("Early")

result = abs(exam_total_minutes - arrive_total_minutes)
if exam_total_minutes - arrive_total_minutes > 0:
    if result < 60:
        print(f"{result} minutes before the start")
    else:
        print(f"{result // 60}:{result % 60:02d} hours before the start")
elif arrive_total_minutes - exam_total_minutes > 0:
    if result < 60:
        print(f"{result} minutes after the start")
    else:
        print(f"{result // 60}:{result % 60:02d} hours after the start")