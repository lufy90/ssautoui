

mouse_action = [
        'position', 
        'move', 
        'press', 
        'release', 
        'click',
        'scroll'
        ]

keyboard_action = [
        'alt_gr_pressed', 
        'alt_pressed',
        'ctrl_pressed',
        'keyboard_mapping',
        'modifiers',
        'press',
        'pressed',
        'release',
        'shift_pressed',
        'touch',
        'type'
        ]

action1 = ('mouse_press', 'arguments')
action2 = ('key_press', 'arguments')

if __name__ == '__main__':
    import pynput
    kp=pynput.keyboard.Controller()
    mp=pynput.mouse.Controller()
    mp.position=(665, 359)
    mp.press(pynput.mouse.Button.left)
    mp.position=(483, 355)
    mp.release(pynput.mouse.Button.left)
    kp.press(pynput.keyboard.Key.ctrl)
    kp.press('c')
    kp.release('c')
    kp.release(pynput.keyboard.Key.ctrl)
