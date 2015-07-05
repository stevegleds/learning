x = "There are %d types of people." % 10 # puts the number 10 in the string
binary = "binary keyword"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # puts strings in

print(x)
print(y)
test = "I said: {!s}" .format('binary')
print(test)
print("I said: {!s}" .format(binary))
#print("I said: %r.") % x # prints whatever format x is
#print("I also said: '%s'.") % y # prints y as string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! " # the parameter is not defined here - it is added later

print(joke_evaluation, "{}" .format(hilarious)) # hilarious is the parameter inserted in %r

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)
