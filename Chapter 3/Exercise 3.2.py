###
# Exercise 2: Rewrite your pay program using try and except 
# so that your program handles non-numeric input gracefully 
# by printing a message and exiting the program. The following
# shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input
###


try:
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
except:
    print('Error, please enter numeric input')




