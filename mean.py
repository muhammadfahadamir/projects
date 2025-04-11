import numpy
from scipy import stats


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)

x = numpy.median(speed)

print(x)


x = stats.mode(speed)

print(x)


speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

print(x)

speed = [32,111,138,28,59,77,97]

x = numpy.std(speed)

print(x)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 60)

print(x)



