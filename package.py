import sys
import os
import subprocess

def package_mainnet():
    """Packages the Mainnet folder using PyInstaller."""
    project_dir = os.path.dirname(os.path.abspath(__file__))
    executable_name = "mainnet_executable"  # Change this to your desired executable name

    # Construct the PyInstaller command
    pyinstaller_command = [
        "pyinstaller",
        "--onefile",
        "--noconsole",  # Optional: Hide the console window
        f"{project_dir}/mainNet.py"
    ]

    # Run PyInstaller
    try:
        subprocess.run(pyinstaller_command, check=True)
        print("Packaging successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error packaging: {e}")

if __name__ == "__main__":
    package_mainnet()
