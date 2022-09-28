hours = input('Enter Hours:')
hours = int(hours)
rate = input('Enter Rate:')
rate = int(rate)
if hours <= 40 :
    pay = hours * rate
else :
    overtime = (hours- 40) * (rate * 1.5)
    pay = ((40 * rate) + overtime)
print('Pay:', pay)

# if hours <= 40, pay the regular rate for all hours
# if hours > 40, pay the regular rate up until 40 hours, then pay 1.5x for succeeding hours