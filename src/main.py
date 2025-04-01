''' 
Version: 1.0
Author: Davis Onyeoguzoro
Date: 24th March, 2025

Project: Assembly Line - Automated Image Capture from Universal Robot Camera

Description: This project automates the process of capturing images from the Universal Robot (UR5e). 
The script logs into the robot's web interface, selects the camera module, and captures images for inspection and analysis.  

Robots used: Universal Robot (UR5e)

End-Effector: OnRobot RG2 Gripper

Purpose:  
- Automate image capture from the UR5e camera  
- Enable real-time quality control and inspection  
- Integrate with vision-based analysis systems  
'''

# Libraries required
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Strt web driver
service = Service('chromedriver') 
driver = webdriver.Chrome(service=service, options=chrome_options)


# Take note of the ip of the compute box, and you have to be in the same network
try:
    # Ip of device (which should be the device connected to the UR)
    driver.get("http://129.101.98.233")
    
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='username']"))
    )
    username_field.send_keys("admin")
    
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='password']"))
    )
    password_field.send_keys("12345678")
    
    signin_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'on-std-button') and contains(text(), 'Sign in')]"))
    )
    signin_button.click()
    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//h5[text()='Eyes']"))
    )
    
    # use css page inspect to get elements here
    eyes_select_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, 
            "//div[contains(@class, 'card-body')][.//h5[text()='Eyes']]//button[contains(@class, 'on-card-button')]"))
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", eyes_select_button)
    time.sleep(0.5) 
    eyes_select_button.click()
    
    print("Successfully selected Eyes!")
    
    #landmark
    landmark_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "landmark-tab"))
    )
    
    # Smoth scroll
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", landmark_tab)
    time.sleep(0.5)
    
    landmark_tab.click()
    print("Successfully clicked on Landmark tab!")

    # check_det
    check_det = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'on-std-button') and contains(text(), 'CHECK DETEC')]"))
    )
    check_det.click()

    print("Successfully clicked on CHECK DETEC!")

    time.sleep(3)

    driver.save_screenshot("images/Image_3.png")
    print("Full page screenshot saved as images/Image_1.png")

    # Container
    canvas_container = driver.find_element(By.ID, "canvasContainer")
    
    # Take screenshot of just this element
    canvas_container.screenshot("images/Image_4.png")
    print("Successfully saved camera output screenshot!")

    # Specific region screenshot
    # element = driver.find_element(By.ID, "some-element-id") 
    # element.screenshot("images/screenshot_element.png")

    # screenshot = pyautogui.screenshot()
    # screenshot.save("/images/Image1.png")
    
    # # Specifec region
    # screenshot_region = pyautogui.screenshot(region=(0, 0, 300, 400)) # x, y, width, height
    # screenshot_region.save("/images/Image2.png")

    # # inspect
    # inspect_tab = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, 
    #                                     "//div[contains(@id, 'inspection-tab)]"))
    # )    
    
except Exception as e:
    print(f"Error occurred: {e}")
    driver.save_screenshot("error_screenshot.png")
    print("Screenshot saved as error_screenshot.png")

finally:
    input("Press Enter to close the browser...")
    driver.quit()