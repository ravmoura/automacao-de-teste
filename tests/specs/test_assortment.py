from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver

URL = "https://www.saucedemo.com/"


def realizar_login(driver):
    driver.get(URL)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )


def test_ordenar_produtos_por_preco_crescente(driver):
    """
    Cenário: Ordenar produtos por preço crescente

    Dado que o usuário está na página de produtos
    Quando seleciona ordenar por preço crescente
    Então os produtos devem ser exibidos do menor para o maior preço
    """
    realizar_login(driver)

    driver.find_element(By.CLASS_NAME, "product_sort_container").click()    
    driver.find_element(By.XPATH, "//option[@value='lohi']").click()

    elementos_preco = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_price"
    )

    precos_exibidos = [
        float(elemento.text.replace("$", ""))
        for elemento in elementos_preco
    ]
    assert precos_exibidos == sorted(precos_exibidos)


def test_ordenar_produtos_por_preco_decrescente(driver):
    """
    Cenário: Ordenar produtos por preço decrescente

    Dado que o usuário está na página de produtos
    Quando seleciona ordenar por preço decrescente
    Então os produtos devem ser exibidos do maior para o menor preço
    """

    realizar_login(driver)

    driver.find_element(By.CLASS_NAME, "product_sort_container").click()    
    driver.find_element(By.XPATH, "//option[@value='hilo']").click()

    elementos_preco = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_price"
    )

    precos_exibidos = [
        float(elemento.text.replace("$", ""))
        for elemento in elementos_preco
    ]

    assert precos_exibidos == sorted(
        precos_exibidos,
        reverse=True
    )

def test_ordenar_produtos_por_nome_crescente(driver):
    """
    Cenário: Ordenar produtos por nome

    Dado que o usuário está na página de produtos
    Quando seleciona ordenar por nome de A a Z
    Então os produtos devem ser exibidos em ordem alfabética
    """
    realizar_login(driver)

    driver.find_element(By.CLASS_NAME, "product_sort_container").click()    
    driver.find_element(By.XPATH, "//option[@value='az']").click()    

    elementos_nome = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_name"
    )

    nomes_exibidos = [
        elemento.text
        for elemento in elementos_nome
    ]

    assert nomes_exibidos == sorted(nomes_exibidos)

def test_ordenar_produtos_por_nome_decrescente(driver):
    """
    Cenário: Ordenar produtos por nome decrescente

    Dado que o usuário está na página de produtos
    Quando seleciona ordenar por nome de Z a A
    Então os produtos devem ser exibidos em ordem alfabética inversa
    """
    realizar_login(driver)

    driver.find_element(By.CLASS_NAME, "product_sort_container").click()    
    driver.find_element(By.XPATH, "//option[@value='za']").click()

    elementos_nome = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_name"
    )

    nomes_exibidos = [
        elemento.text
        for elemento in elementos_nome
    ]

    assert nomes_exibidos == sorted(
        nomes_exibidos,
        reverse=True
    )