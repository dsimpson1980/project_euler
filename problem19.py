"""Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?"""

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_forward = [d % 7 for d in days_in_month]

day_of_week = 1 + 365 % 7
sunday_first = 0
for year in range(1901, 2001):
    for month, day_forward in enumerate(days_forward):
        print year, month, day_of_week
        if day_of_week == 0:
            sunday_first += 1
        if month == 1 and year % 4 == 0 and year != 2000:
            day_forward += 1
        day_of_week = (day_of_week + day_forward) % 7
print 'Number of months starting with Sunday %s' % sunday_first
