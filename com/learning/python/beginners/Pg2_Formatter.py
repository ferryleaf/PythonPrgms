#!/usr/bin/python
# _ *_ coding : utf-8 _*_

#__author__='Abhijit Mohapatra'
#__version__=1.0.1


# Trying out with different format specifiers.
my_name="Abhijit Mohapatra"
my_age=30
my_height=5.85  # foot
my_weight= 65 # kgs
my_eyes='Blue'
my_teeth='White'
my_hair='Brown'

gender='F'



# Printing String
print("Let's talk about %s." % my_name)

# Printing decimal truncating fraction part.
print("He's %d inches tall." % my_height)

# Printing in floating values.
print("He's %f inches tall." % my_height)
print("He's %F inches tall." % my_height)

# Rounding off the numbers
print("Rounding off:%f" %round(my_height,ndigits=1))

# Printing in floating value in exponential format(lowercase).
print("He's %e inches tall." % my_height)

# Printing in floating value in exponential format(uppercase).
print("He's %E inches tall." % my_height)

# Printing integers
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")

# Printing representation formatter which tries to convert any object to String
print("Let's talk about %r." % my_weight)

# Printing a single character
print("Gender:%c" % gender)

# Printing multiple params of string.
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# Trying to add the values and then display in the same print statement.
print("If I add %d, %d and %d I get %d."%(my_age, my_height, my_weight, my_age + my_height + my_weight))

#Error need to specify formatter.
#print("%" %my_weight)

# Printing weight in octal format
print("He's %o pounds heavy." % my_weight)

# Printing weight in hexadecimal format lowercase
print("He's %x pounds heavy in octal representation." % my_weight)

# Printing weight in hexadecimal format uppercase
print("He's %X pounds heavy in hexadecimal representation." % my_weight)