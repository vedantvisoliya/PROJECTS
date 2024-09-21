import time

# 12 hour clock

time_object = time.localtime()
time_hours = int(time.strftime("%I",time_object))
time_AM_PM = time.strftime("%p",time_object)

if (time_AM_PM == 'PM'):
    if((time_hours == 12) or (1<=time_hours<4)):
        print(time.strftime('%A, %B %d, %Y\n%I:%M %p',time_object))
        print("GOOD AFTERNOON!")
    elif((4<=time_hours<7)):
        print(time.strftime('%A, %B %d, %Y\n%I:%M %p',time_object))
        print("GOOD EVENING!")
    else:
        print(time.strftime('%A, %B %d, %Y\n%I:%M %p',time_object))
        print("GOOD NIGHT!")
else:
    print(time.strftime('%A, %B %d, %Y\n%I:%M %p',time_object))
    print("GOOD MORNING PINEAPPLE LOOKING VERY GOOD VERY NICE!!!")

# 24 hour clock

# time_hours = int(time.strftime("%H",time_object))

# if (0<=time_hours<12):
#     print(time.strftime('%A, %B %d, %Y\n%H:%M %p',time_object))
#     print("GOOD MORNING PINEAPPLE LOOKING VERY GOOD VERY NICE!!!")
# elif(12<=time_hours<16):
#     print(time.strftime('%A, %B %d, %Y\n%H:%M %p',time_object))
#     print("GOOD AFTERNOON!")
# elif(16<=time_hours<19):
#     print(time.strftime('%A, %B %d, %Y\n%H:%M %p',time_object))
#     print("GOOD EVENING!")
# else:
#     print(time.strftime('%A, %B %d, %Y\n%H:%M %p',time_object))
#     print("GOOD NIGHT!")