print 'Hello, what is your first name?'
name = str(raw_input('>>'))
print ""

print 'Nice!'
print ""

print 'So %s, I will now quess your age!!' % name
print ""

print 'But I need to ask some questions:'
print ""

print 'What is the first number of your age?'
first_number = int(raw_input('>>')) 
print ""

number1 = first_number*5
print 'Okay, %s, I will multiply that by 5 = %s' % (str(name), str(number1))
print ""

number2 = number1+3
print 'Next, I will add 3 to the number = ', number2
print ""

number3 = number2*2
print 'Next, I will double that number = ', number3
print ""

print 'Now I will need the second number of your age!!'
second_number = int(raw_input('>>'))
print ""

number4 = number3 + second_number
print 'Thanx! I will add that number to our running total %s + %s =  %s' % \
      (str(number3),str(second_number),str(number4))
print ""

your_age = number4 - 6
print 'And the last thing I will do is subtract 6 [ %s - 6 ] = %s' % \
      (str(number4),str(your_age))
print ""

print 'WOW!!!, So %s your AGE IS = %s' % (str(name), str(your_age))
print ""

