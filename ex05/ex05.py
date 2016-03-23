name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height_cm = 74 # inches
cm_to_inch = 1.0/2.54
my_height_inch = my_height_cm * cm_to_inch
my_weight = 180.5 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
#place holder
print "Let's talk about %s." % name
print "He's %g centimeters tall." % my_height_cm
print "He's %d inches tall." % my_height_inch
print "He's %g pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)