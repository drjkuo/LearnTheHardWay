name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = 74 * 2.54 #cms
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d cms tall." %height_cm
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %s, %r, and %r I get %d." % (
    age+1, height, weight, age + height + weight)