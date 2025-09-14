# OOP LightSwitch

class LightSwitch():
    def __init__(self):
        self.switch_is_on = False
    def turn_on(self):
        # turn the switch on
        self.switch_is_on = True
    def turn_off(self):
        self.switch_is_on = False
    def show(self):  # added for testing
        print(self.switch_is_on)
        
# Main code
light_switch = LightSwitch()

# Calls to methods
light_switch.show()
light_switch.turn_on()
light_switch.show()
light_switch.turn_off()
light_switch.show()
light_switch.turn_on()
light_switch.show()