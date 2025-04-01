import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestURCameraAutomation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize WebDriver before tests."""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        service = Service("chromedriver")
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.driver.get("http://129.101.98.233")

    def test_login(self):
        """Test login functionality."""
        driver = self.driver
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

        # TO verify login success done by checking content of page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h5[text()='Eyes']"))
        )
        self.assertIn("Eyes", driver.page_source, "Login failed!")

    def test_navigation_to_landmark(self):
        """Test navigation to the Landmark tab."""
        driver = self.driver
        landmark_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "landmark-tab"))
        )
        landmark_tab.click()

        # Verify success navigation
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'CHECK DETEC')]"))
        )
        self.assertIn("CHECK DETEC", driver.page_source, "Failed to navigate to Landmark tab!")

    def test_screenshot_capture(self):
        """Test screenshot saving functionality."""
        driver = self.driver
        driver.save_screenshot("../images/test_screenshot.png")

        # Ensure that the screenshot is saved to right dir
        self.assertTrue(os.path.exists("../images/test_screenshot.png"), "Screenshot was not saved!")

    @classmethod
    def tearDownClass(cls):
        """Close WebDriver after tests."""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
