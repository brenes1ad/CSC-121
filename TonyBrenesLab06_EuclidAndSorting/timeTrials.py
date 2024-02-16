import BetterStopwatch
from random import randint
from math import log2

def gcd(a, b):
    count = 0
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    while b != 0:
        a, b = b, a % b
        count += 1
    return count

timer = BetterStopwatch.BetterStopwatch()
k = 500
averageTimes = []
checkLog = []
print("List sorting:")
print("%7s %10s %20s" % ("k", "averageTime", "averageTime / (k*log2(k))"))
for n in range(12):
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
    print("%7s %10s %20s" % (k, averageTime, averageTime / (k*log2(k))))
    k *= 2


k = 10
averageCounts = []
checkFunction = []
print("GCD:")
print("%15s %10s %15s" % ("k", "averageCount", "(averageCount / log2(k))"))
for n in range(12):
    totalCounts = 0
    for i in range(20):
        totalCounts += gcd(randint(0, k), randint(0, k))
    averageCount = totalCounts // 20
    averageCounts.append(averageCount)
    checkFunction.append(averageCount / log2(k))
    print("%15d %10d %15f" % (k, averageCount, (averageCount / log2(k))))
    k *= 10



