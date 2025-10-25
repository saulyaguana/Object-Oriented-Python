# pygame demo 9 - 3-button test with callbacks

# 1 - Import packages
import pygame
from pygame.locals import *
from SimpleButton import *
import sys
from pathlib import Path

# 2 - Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30
PATH = Path(__file__).resolve().parent

# Define a function to be used as a "callback"
def myCallbackFunction():
    print("User pressed Button B, called myCallbackFunction")
    
# Define a class with a method to be used as a "callback"
class CallBackTest():
    def __init__(self):
        pass
    
    def my_method(self):
        print("User passed ButtonC, called my_method of the CallBackTest object")
        
# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.

# 5 - Initialize variables
callback_test = CallBackTest()
# Create instances of SimpleButton
# No call back
buttonA = SimpleButton(window, (25, 30), PATH / "images/buttonAUP.png", PATH / "images/buttonADOWN.png")

# Specifying a function to call back
buttonB = SimpleButton(
    window,
    (150, 30),
    PATH / "images/buttonBUP.png",
    PATH / "images/buttonBDOWN.png",
    callback=myCallbackFunction,
)

# Specifying a method of an object to call back
buttonC = SimpleButton(
    window,
    (275, 30),
    PATH / "images/buttonCUp.png",
    PATH / "images/buttonCDOWN.png",
    callback=callback_test.my_method,
)

counter = 0

# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Pass the event to the button, see if it has been clicked on
        if buttonA.handle_event(event):
            print("User passed button A, handled in the main loop")
            
        # buttonB and buttonC have callbacks,
        # no need to check results of these calls
        buttonB.handle_event(event)
        buttonC.handle_event(event)
        
    # 8 - Do any "per frame" actions
    counter += 1
    
    # 9 - Clear the window
    window.fill(GRAY)
    
    # 10 - Draw all window elements
    buttonA.draw()
    buttonB.draw()
    buttonC.draw()
    
    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)