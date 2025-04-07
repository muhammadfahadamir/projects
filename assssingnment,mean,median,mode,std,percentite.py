import numpy
from scipy import stats

#1
marks = [72, 88, 91, 75, 89, 90, 72, 85, 84, 88, 75]

new_marks_for_mean=numpy.mean(marks)

print(new_marks_for_mean)

new_marks_for_median=numpy.median(marks)

print(new_marks_for_median)

new_marks_for_mode=stats.mode(marks)

print(new_marks_for_mode)

#2
speeds = [12.3, 13.1, 11.8, 12.7, 13.3, 13.1, 12.0, 12.8]

new_speed_for_mean=numpy.mean(speeds)

print(new_speed_for_mean)

new_speed_for_median=numpy.median(speeds)

print(new_speed_for_median)

new_speed_for_mode=stats.mode(speeds)

print(new_speed_for_mode)

new_speed_for_std=numpy.std(speeds)

print(new_speed_for_std)

#3
salaries = [45, 48, 52, 49, 47, 50, 120, 51, 49, 46, 52]

new_salaries_for_mean=numpy.mean(salaries)

print(new_salaries_for_mean)

new_salaries_for_median=numpy.median(salaries)

print(new_salaries_for_median)

new_salaries_for_mode=stats.mode(salaries)

print(new_salaries_for_mode)

new_salaries_for_std=numpy.std(salaries)

print(new_salaries_for_std)

#4
temps = [28, 30, 29, 31, 32, 30, 29, 28, 27, 31, 32, 33, 30, 29]

new_temps_for_mean=numpy.mean(temps)

print(new_temps_for_mean)

new_temps_for_median=numpy.median(temps)

print(new_temps_for_median)

new_temps_for_mode=stats.mode(temps)

print(new_temps_for_mode)

new_temps_for_percentile=numpy.percentile(temps, 75)

print(new_temps_for_percentile)

#5
ages = [3, 5, 4, 6, 7, 3, 2, 5, 4, 6, 5, 3, 2]

new_ages_for_mean=numpy.mean(ages)

print(new_ages_for_mean)

new_ages_for_median=numpy.median(ages)

print(new_ages_for_median)

new_ages_for_mode=stats.mode(ages)

print(new_ages_for_mode)

new_ages_for_percentile=numpy.percentile(ages, 75)

print(new_ages_for_percentile)