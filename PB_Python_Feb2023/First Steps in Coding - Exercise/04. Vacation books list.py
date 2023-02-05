pages = int (input())
pages_per_hour = int(input())
days_to_read = int(input())

total_time_to_read = pages // pages_per_hour
needed_time_to_read = total_time_to_read // days_to_read

print(needed_time_to_read)
