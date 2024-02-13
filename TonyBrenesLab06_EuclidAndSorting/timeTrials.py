import BetterStopwatch
from random import randint
from math import log2

timer = BetterStopwatch.BetterStopwatch()
k = 500
averageTimes = []
checkLog = []
for n in range(12):
    k *= 2
    totalTime = 0
    for i in range(20):
        list = [randint(1, 100) for i in range(k)]
        timer.startNS()
        list.sort()
        time = timer.stopNS()
        totalTime += time
    averageTime = totalTime / 20
    averageTimes.append(averageTime)
    checkLog.append(averageTime / (k*log2(k)))
print(averageTimes)
print(checkLog)






