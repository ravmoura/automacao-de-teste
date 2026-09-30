from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver

def test_login_com_sucesso(driver):
    # =========================
    # 1. LOGIN com sucesso
    # =========================

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "inventory_container"))
    )

    # Validação login
    assert "inventory.html" in driver.current_url


def test_login_com_credenciais_invalidas(driver):
    # ===================================
    # 1. LOGIN com credenciais invalidas
    # ===================================

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("senha_invalida")
    driver.find_element(By.ID, "login-button").click()

    mensagem_erro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h3[data-test='error']")
        )
    )

    # Validação mensagem erro
    assert mensagem_erro.is_displayed()
    assert "Username and password do not match" in mensagem_erro.text


def test_usuario_bloqueado(driver):
    # ===================================
    # 1. LOGIN com usuário bloqueado
    # ===================================

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    mensagem_erro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h3[data-test='error']")
        )
    )
        
    # Validação mensagem erro
    assert mensagem_erro.is_displayed()
    assert "Sorry, this user has been locked out." in mensagem_erro.text

def test_deslogar(driver):
    # ===================================
    # 1. LOGIN com sucesso
    # ===================================

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "inventory_container"))
    )

    # Validação login
    assert "inventory.html" in driver.current_url

    # ===================================
    # 2. LOGOUT
    # ===================================

    driver.find_element(By.ID, "react-burger-menu-btn").click()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
    )

    driver.find_element(By.ID, "logout_sidebar_link").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )

    # Validação logout
    assert "saucedemo.com" in driver.current_url    