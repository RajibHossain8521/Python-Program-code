num = int(input())

for i in range(num):
    string = input()
    char = input()
    length = len(string)
    if length in range(1000):
            totalChar = string.count(char)
            if char in string:
                print('Occurrence of', char, 'in', string, '=', totalChar)
            else:
                print(char, 'is not present')

                # COMPLETE
