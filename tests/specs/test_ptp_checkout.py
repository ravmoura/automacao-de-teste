from guara.application import Application
import pytest
from selenium import webdriver
from guara import it
from tests.transactions.login_transaction import LoginWithTransaction
from tests.transactions.add_to_cart_transaction import AddToCartTransaction
from tests.transactions.checkout_transaction import CheckoutTransaction
from tests.transactions.finish_order_transaction import FinishOrderTransaction
from tests.transactions.checkout_with_missing_data_transaction import CheckoutWithoutDataTransaction

from tests.fixtures.driver import driver

@pytest.mark.smoke
def test_checkout_ptp(driver):
    app = Application(driver)
    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")
    
    app.when(AddToCartTransaction).asserts(it.IsEqualTo, 1)
    app.when(CheckoutTransaction,name="Douglas",last="Teste",zip_code="12345"
    ).asserts(it.Contains, "checkout-step-two")

    app.when(FinishOrderTransaction).asserts(it.Contains, "Thank you")

@pytest.mark.regression    
def test_checkout_without_data_ptp(driver):
    app = Application(driver)
    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")

    app.when(AddToCartTransaction).asserts(it.IsEqualTo, 1)
    app.when(CheckoutWithoutDataTransaction,name="",last="",zip_code="").asserts(it.IsEqualTo, "Error: First Name is required")

@pytest.mark.regression   
def test_checkout_with_missing_data_ptp(driver):
    app = Application(driver)
    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")

    app.when(AddToCartTransaction).asserts(it.IsEqualTo, 1)
    app.when(CheckoutWithoutDataTransaction,name="Marluce",last="",zip_code="").asserts(it.IsEqualTo, "Error: Last Name is required")