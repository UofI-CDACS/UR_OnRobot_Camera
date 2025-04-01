# UR_OnRobot_Camera

This project is an automation script for capturing images from the Universal Robot (UR5e) camera. The script interacts with the UR5e robot's web interface and captures images from the camera, which can be used for various applications like quality inspection, and real-time monitoring. The script automates browser actions and Python for processing and saving images.

---

## Table of Contents

1. [Usage](#usage)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Project Structure](#project-structure)
5. [How to Build](#how-to-build)

<!-- 6. [Contributing](#contributing)
7. [License](#license) -->

---

## Usage

### Overview

This automation script captures images from the OnRobot Eyes that is connected Universal Robot (UR5e), interacting with its web interface. It performs a various of actions like logging into the robot’s control interface (via the OnRobot Compute Box web interrface), navigating to the camera section, and capturing images of the robot’s workspace.

### How to Use

1. **Power on the Robot**:

   - Ensure the Universal Robot (UR5e) and the OnRobot Compute Box are powered on and connected to the network.
2. **Clone the Repository**:

   - ```
         git clone https://github.com/UofI-CDACS/UR_OnRobot_Camera
     ```
3. **Install the Dependencies**:

   - ```
         pip install -r requirements.txt
     ```
4. **Edit the Script Configuration**:

   - Open the `main.py` file and replace the IP address of the UR robot.
     - Example:
       ```python
       driver.get("http://192.168.1.100")
       ```
5. **Run the Script**:

   - Execute the script to start capturing images:
     ```bash
     python capture_images.py
     ```
6. **Image Output**:

   - The captured images will be saved in the `images/` directory, with filenames indicating the type of image captured (e.g., `Image_1.png`, `Image_2.png`).

---

## Features

- **Automated Image Capture**:

  - Captures images from the UR5e camera automatically through the web interface.
- **Smooth Navigation**:

  - Uses Selenium for web automation to navigate through the robot’s interface and interact with buttons, tabs, and other elements.
- **Screenshot Saving**:

  - Saves screenshots of the full page and specific regions of interest (e.g., the camera output).
- **Error Handling**:

  - In case of any issues (e.g., login failure, element not found), the script saves an error screenshot for debugging purposes.

---

## Requirements

### Software

- Python 3.10
- Selenium
- Chrome WebDriver (compatible with the version of Google Chrome that you have installed)
- pyautogui (for additional screenshot handling, for capturing)

### Hardware

- Universal Robot UR5e
- OnRobot RG2 Gripper
- Compute Box
- OnRobot Eyes

---

## Project Structure

### 1. **src**

Contains the main script (`capture_images.py`) for capturing images from the UR robot's web interface.

### 2. **images**

Directory to store all the captured images:

- `Image_1.png`: Screenshot of the full page.
- `Image_2.png`: Screenshot of a specific region (e.g., camera output).

### 3. **docs**

Includes documentation and references for understanding the project setup.

### 4. **tests**

Contains test scripts for ensuring the proper functionality of the automation, including:

- `test_login.py`: Verifies that the script can log into the UR robot’s interface.
- `test_capture.py`: Ensures that images are correctly captured and saved.

---

## How to Build

### Step 1: Install Dependencies

1. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
