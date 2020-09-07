"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

curDate = datetime.now().timetuple()

# If the length of the input contains three separate entities and the second argument is greater than zero but less than 13...
if len(sys.argv) == 3 and 0 < int(sys.argv[1]) < 13:
# then print the calender month using the integer from the first argv and the year from the second argv
    print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))


# Else if the length of the input is equal to 2
elif len(sys.argv) == 2:
#Print the calender month with the current year and use the first argv to show the month
    print(calendar.month(curDate.tm_year, int(sys.argv[1])))

# Else if the length of the input is 1 
elif len(sys.argv) == 1:
# then just display the current year and month
    print(calendar.month(curDate.tm_year, curDate.tm_mon))

else:
# ELse if the input is any other length display instructions on how to format the submission
    print("please launch file with proper [month] [year] format")

