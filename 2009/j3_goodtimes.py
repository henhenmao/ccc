
def time_function2(time, passed_time):
    hour = time//100
    minute = time%100
    hour += passed_time//60
    minute += passed_time % 60
    hour += minute//60
    minute %= 60 
    hour %= 24
    return hour * 100 + minute


def goodtimes(time):
    print(time_function2(time, 0), "in Ottawa")
    print(time_function2(time, 1260), "in Victoria")
    print(time_function2(time, 1320), "in Edmonton")
    print(time_function2(time, 1380), "in Winnipeg")
    print(time_function2(time, 0), "in Toronto")
    print(time_function2(time, 60), "in Halifax")
    print(time_function2(time, 90), "in St. John's")

times = int(input())
goodtimes(times)