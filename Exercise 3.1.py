
###
# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
###

hours = input('Enter Hours:')
rate = input('Enter Rate:')
total_hours = int(hours)
rate = int(rate)

regular_hours = 40
if (total_hours < 40):
    regular_hours = total_hours

pay = regular_hours * rate

if (total_hours > 40):
    ot_hours = total_hours - regular_hours
    rate = rate * 1.5
    pay = pay + (ot_hours * rate)

print("Pay: ", pay)
