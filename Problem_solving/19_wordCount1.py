num = int(input())
for i in range(num):
    str = input()
    count = 1
    for x in str:
        if x == " ":
            count = count + 1
    print(count)

        # COMPLETE