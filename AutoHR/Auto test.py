import pyautogui

# Threshold for mouse movement in pixels
movement_threshold = 10

# Flag to indicate if the script should stop
stop_script = False

# Function to check if mouse has moved beyond the threshold
def check_mouse_movement():
    global stop_script
    
    # Get the initial mouse position
    initial_pos = pyautogui.position()
    
    while not stop_script:
        # Get the current mouse position
        current_pos = pyautogui.position()
        
        # Calculate the distance moved by the mouse
        distance = abs(current_pos[0] - initial_pos[0]) + abs(current_pos[1] - initial_pos[1])
        
        # Check if the mouse has moved beyond the threshold
        if distance > movement_threshold:
            # Stop the script
            stop_script = True
            print('Script stopped due to mouse movement.')
            break

# Your AutoGUI script
def autogui_script():
    try:
        # Your AutoGUI code here
        pyautogui.moveTo(100, 100, duration=1)
        pyautogui.click()
        pyautogui.typewrite('Hello, World!')
        
    except KeyboardInterrupt:
        # This block will be executed on Ctrl+C
        print('Script stopped.')

# Start checking for mouse movement
check_mouse_movement()

# Start the AutoGUI script
autogui_script()