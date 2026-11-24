
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_login():

    # Chrome brauzer sozlamalari
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        # 1. Saytni ochish
        driver.get(
            "https://nodirshukurov209-ux.github.io/selenium-login-test-/"
        )

        wait = WebDriverWait(driver, 15)

        # 2. Login ma'lumotlarini kiritish
        username = wait.until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        username.send_keys("student")

        password = driver.find_element(By.ID, "password")
        password.send_keys("12345")

        # 3. Login tugmasini bosish
        login_button = driver.find_element(By.ID, "loginBtn")
        login_button.click()

        # 4. Muvaffaqiyat xabarini tekshirish
        success = wait.until(
            EC.visibility_of_element_located((By.ID, "successMessage"))
        )

        assert "Login muvaffaqiyatli" in success.text

        # 5. Dashboard ochilganini tekshirish
        dashboard = driver.find_element(By.ID, "dashboard")
        assert dashboard.is_displayed()

        # 6. URL manzilni tekshirish
        assert "#dashboard" in driver.current_url

        print("TEST PASSED: Login muvaffaqiyatli!")

    finally:
        # Brauzerni yopish
        driver.quit()
