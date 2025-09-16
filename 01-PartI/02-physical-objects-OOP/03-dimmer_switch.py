# DimmerSwitch class

class DimmerSwitch():
    def __init__(self):
        self.switch_is_on = False
        self.brightness = 0
        
    def turn_on(self):
        self.switch_is_on = True
        
    def turn_off(self):
        self.switch_is_on = False
        
    def raise_level(self):
        if self.brightness < 10:
            self.brightness += 1
            
    def lower_level(self):
        if self.brightness > 0:
            self.brightness -= 1
            
    # Extra method for debugging
    def show(self):
        print(f"Switch is on?: {self.switch_is_on}")
        print(f"Brightness is: {self.brightness}")
        
# Main code
dimmer = DimmerSwitch()

# Turn switch on, and raise the level 5 times
dimmer.turn_on()
for _ in range(5):
    dimmer.raise_level()
dimmer.show()

# Lowe the level 2 times, and turn switch off
for _ in range(2):
    dimmer.lower_level()
dimmer.turn_off()
dimmer.show()

# Turn switch on, and raise the level 3 times
dimmer.turn_on()
for _ in range(3):
    dimmer.raise_level()
dimmer.show()