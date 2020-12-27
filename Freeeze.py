import keyboard

while True:
    if keyboard.is_pressed('q'):
        break

    keyboard.write("You have been hacked")
