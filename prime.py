start = 1
number = int(input())
while(start < number):
    if(number % start == 0):
        print(start)
    start = start + 1
input()