def average(*numbers) :
    sum = 0
    for i in numbers:
        sum += i
    print('Avg :',sum/len(numbers))

average(5,6,4,5)