import keyboard

key_down = False

def detectKeyPress():
    global key_down
    if not key_down:
        key_down = True
        print("hello boss")

def detectKeyRelease():
    global key_down
    if key_down:
        key_down = False
        print("Gdbye boss")

keyboard.on_press_key("space", lambda e: detectKeyPress())
keyboard.on_release_key("space", lambda e: detectKeyRelease())

keyboard.wait("esc")                                    