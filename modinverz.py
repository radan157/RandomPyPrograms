while True:
    start = 1
    a = int(input())
    n = int(input())
    out = 0
    while(out != 1):
        if((start * a) % n == 1):
            print(start)
            input()
        start = start + 1
    input()