vexcode_brain_precision = 0
vexcode_console_precision = 0
myVariable = 0

def when_started1():
    global myVariable, vexcode_brain_precision, vexcode_console_precision
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("REMOTE")
    brain.screen.set_cursor(2, 1)
    brain.screen.print("ACTIVATED")
    wait(5, SECONDS)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 8)
    brain.screen.print("VEX")

when_started1()