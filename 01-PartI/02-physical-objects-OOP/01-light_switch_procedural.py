# Procedural light switch

def turn_on():
    global switch_is_on
    # turn the light on
    switch_is_on = True
    
def turn_off():
    global switch_is_on
    # turn the light off
    switch_is_on = False
    
# Main code
switch_is_on = False

# Test code
print(switch_is_on)
turn_on()
print(switch_is_on)
turn_off()
print(switch_is_on)
turn_on()
print(switch_is_on)