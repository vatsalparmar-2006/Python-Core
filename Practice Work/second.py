import time

# time = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))  #System time

hour = int(input("Enter hour : "))

print(hour)

if(hour>0 and hour<12):
    print("Good Morning")
elif(hour>=12 and hour<17):
    print("Good Afternoon")
else:
    print("Good Nignt")