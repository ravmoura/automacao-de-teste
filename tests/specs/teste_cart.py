from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.saucedemo.com/"


def realizar_login(driver):
    driver.get(URL)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )


def test_adicionar_item_ao_carrinho(driver):
    """
    Cenário: Adicionar item ao carrinho
    Dado que o usuário está na página de produtos
    Quando adiciona um produto ao carrinho
    Então o carrinho deve mostrar 1 item
    """

    realizar_login(driver)

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    badge_carrinho = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert badge_carrinho.text == "1"


def test_remover_item_do_carrinho(driver):
    """
    Cenário: Remover item do carrinho
    Dado que o usuário adicionou um item ao carrinho
    Quando remove o item
    Então o carrinho deve estar vazio
    """

    realizar_login(driver)

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    badge_carrinho = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert badge_carrinho.text == "1"

    driver.find_element(
        By.ID,
        "remove-sauce-labs-backpack"
    ).click()

    elementos_badge = driver.find_elements(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert len(elementos_badge) == 0


def test_acessar_carrinho_vazio(driver):
    """
    Cenário: Acessar carrinho vazio
    Dado que o usuário não adicionou itens ao carrinho
    Quando acessa o carrinho
    Então o carrinho deve estar vazio
    """
    realizar_login(driver)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    elementos_badge = driver.find_elements(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert len(elementos_badge) == 0

def test_resetar_carrinho(driver):
    """
    Cenário: Resetar carrinho
    Dado que o usuário adicionou itens ao carrinho
    Quando reseta o carrinho
    Então o carrinho deve estar vazio
    """
    realizar_login(driver)

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    badge_carrinho = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert badge_carrinho.text == "1"

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "reset_sidebar_link"))
    ).click()

    elementos_badge = driver.find_elements(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert len(elementos_badge) == 0

def test_continuar_compras(driver):
    """
    Cenário: Continuar comprando
    Dado que o usuário adicionou itens ao carrinho
    Quando clica em continuar comprando
    Então o usuário deve ser redirecionado para a página de produtos
    """
    realizar_login(driver)

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "continue-shopping"))
    ).click()

    assert "inventory.html" in driver.current_url