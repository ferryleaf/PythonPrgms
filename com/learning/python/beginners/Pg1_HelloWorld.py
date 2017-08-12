# _ *_ coding : utf-8 _*_

print ("Hello! Abhijit Mohapatra")

my_name="Abhijit Mohapatra"
my_age=30
my_height=5.85  # foot
my_weight= 65 # kgs
my_eyes='Blue'
my_teeth='White'
my_hair='Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d and %d I get %d."%(my_age, my_height, my_weight, my_age + my_height + my_weight))