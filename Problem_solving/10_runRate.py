# first find the each over current run rate
# second find the asking current run rate

num = int(input())

for i in range(num):
    if num in range(0, 100):
        firstRun = int(input())
        secondRun = int(input())
        ball = int(input())
        if firstRun in range(0, 1000):
            if secondRun in range(0, firstRun):
                if ball in range(0, 300):
                    ballPlayed = 300 - ball
                    currentRunRate = (secondRun / ballPlayed) * 6
                    difference = (firstRun + 1) - secondRun
                    askingRunRate = (difference / ball) * 6
                    print('%.2f' % currentRunRate)
                    print('%.2f' % askingRunRate)

