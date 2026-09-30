from guara.application import Application
import pytest
from selenium import webdriver
from guara import it
from tests.fixtures.driver import driver

from tests.transactions.login_transaction import LoginWithTransaction
from tests.transactions.login_error_transaction import LoginErrorTransaction
from tests.transactions.logout_transaction import LogoutTransaction

@pytest.mark.smoke
def test_login_success_ptp(driver):
    app = Application(driver)

    app.when(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")

@pytest.mark.regression
def test_invalid_login_ptp(driver):
    app = Application(driver)

    app.when(
        LoginErrorTransaction,
        url="https://www.saucedemo.com",
        user="usuario_invalido",
        password="senha_invalida"
    ).then(it.Contains,"Username and password do not match any user in this service")

@pytest.mark.regression
def test_locked_login_ptp(driver):
    app = Application(driver)

    app.when(
        LoginErrorTransaction,        
        url="https://www.saucedemo.com",
        user="locked_out_user",
        password="secret_sauce"
    ).then(it.Contains,"Sorry, this user has been locked out.")

@pytest.mark.smoke
def test_logout(driver):
    app = Application(driver)

    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")    

    app.when(LogoutTransaction).then(it.Contains, "saucedemo.com")