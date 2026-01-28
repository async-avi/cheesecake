import keyboard

def on_press(key):
    print(key)

keyboard.on_press(on_press)        
keyboard.wait("space")