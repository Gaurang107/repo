import subprocess
import os

# Get the current user's home directory
user_home = os.path.expanduser("~")

# Change the current working directory to the Desktop
desktop_dir = os.path.join(user_home, "Desktop")
os.chdir(desktop_dir)

# Run the commands as subprocesses
try:
    # Capture an image using the Raspberry Pi Camera
    print("Capturing image...")
    subprocess.run(["raspicam-still", "-o", "test.jpg"], check=True)

    # Record a video using the Raspberry Pi Camera
    print("Recording video...")
    subprocess.run(["libcamera-vid", "--codec", "h264", "vid.h264"], check=True)

    print("Image and video have been saved to your Desktop.")

except subprocess.CalledProcessError as e:
    print(f"An error occurred while running the command: {e}")
