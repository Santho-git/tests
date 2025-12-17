from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------- SETUP ----------
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.iamdave.ai/")
    wait = WebDriverWait(driver, 10)
    return driver, wait

# ---------- TEARDOWN ----------
def teardown(driver):
    driver.quit()

# ---------- TEST CASE 1 ----------
def test_logo_presence(driver, wait):
    print("\nRunning Test Case 1: Verify Logo Presence")
    logo = driver.find_element(
        By.CSS_SELECTOR,
        "section.vamtam-sticky-header:first-of-type div.elementor-widget-container a img"
    )
    if logo.is_displayed():
        print("Logo is visible")
    else:
        print("Logo is not visible")

# ---------- TEST CASE 2 ----------
def test_navigation_flow(driver, wait):
    print("\nRunning Test Case 2: Navigation Flow - LET'S TALK")
    initial_url = driver.current_url
    buttons = driver.find_elements(By.CSS_SELECTOR, "span.elementor-button-text")
    for btn in buttons:
        text = btn.text.strip()
        if "talk" in text.lower() and btn.is_displayed():
            parent_button = btn.find_element(By.XPATH, "../..")
            parent_button.click()
            break
    wait.until(lambda d: d.current_url != initial_url)
    new_url = driver.current_url
    if new_url.startswith("https://www.iamdave.ai/"):
        print("Navigation successful:", new_url)
    else:
        print("Navigation failed:", new_url)

# ---------- TEST CASE 3 ----------
def test_form_submission(driver, wait):
    print("\nRunning Test Case 3: Form Input Test")

    # --- Helper functions ---
    def fill_input(by, value, text):
        """Normal inputs: Name, Email, Phone"""
        element = wait.until(EC.element_to_be_clickable((by, value)))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'}); arguments[0].focus();", element)
        element.clear()
        element.send_keys(text)

    def fill_input_js(by, value, text):
        """JS-heavy inputs: Company, Message"""
        element = wait.until(EC.presence_of_element_located((by, value)))
        driver.execute_script("""
            arguments[0].scrollIntoView({block:'center'});
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, element, text)

    # --- Fill the form ---
    # Name
    fill_input(By.NAME, "form_fields[name_free_audit]", "Santhoshi")
    time.sleep(0.5)
    
    # Email
    fill_input(By.NAME, "form_fields[email]", "santhoshi@test.com")
    time.sleep(0.5)
    
    # Company (JS injection)
    fill_input_js(By.NAME, "form_fields[field_93bc8cc]", "MyCompany")
    time.sleep(0.5)
    
    # Wait for dropdown to be clickable after JS injection
    dropdown_element = wait.until(EC.element_to_be_clickable((By.NAME, "form_fields[field_21d99c4]")))
    Select(dropdown_element).select_by_visible_text("AI Virtual Avatar")
    time.sleep(0.5)
    
    # Phone
    phone = wait.until(EC.element_to_be_clickable((By.NAME, "form_fields[field_597bd0b]")))
    phone.clear()
    phone.send_keys("9876543210")
    time.sleep(0.5)
    
    # Message (JS injection)
    fill_input_js(By.NAME, "form_fields[message]", "Selenium assignment test")
    time.sleep(0.5)
    
# ---------- MAIN EXECUTION ----------
if __name__ == "__main__":
    driver, wait = setup()

    try:
        test_logo_presence(driver, wait)
        test_navigation_flow(driver, wait)
        test_form_submission(driver, wait)
        print("\nAll test cases executed successfully!")
    finally:
        teardown(driver)
