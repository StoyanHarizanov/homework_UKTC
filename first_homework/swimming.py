minutes = int(input())
seconds = int(input())
distance_of_swimming = float(input())
seconds_100_meters = int(input())

total_seconds = (minutes * 60) + seconds
time_minus = (distance_of_swimming / 120) * 2.5

swimming_time = (distance_of_swimming / 100) * seconds_100_meters
swimming_time -= time_minus

if total_seconds > swimming_time:
    print(f"Petar won an Olimpic quota! His time is {swimming_time:.3f} ")
else:
    time_diff = swimming_time - total_seconds
    print(f"Petar failed! He was {time_diff:.3f} seconds behind.")


