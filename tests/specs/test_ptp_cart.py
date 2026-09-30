from guara.application import Application
import pytest

from guara import it
from tests.transactions.access_cart_empty_transaction import AccessCartEmptyTransaction
from tests.transactions.login_transaction import LoginWithTransaction
from tests.transactions.add_to_cart_transaction import AddToCartTransaction
from tests.transactions.remove_from_cart_transaction import RemoveFromCartTransaction
from tests.transactions.reset_application_transaction import ResetApplicationTransaction
from tests.transactions.continue_cart_transaction import ContinueCartTransaction

from tests.fixtures.driver import driver

@pytest.mark.e2e
def test_add_to_cart_ptp(driver):
    app = Application(driver)
    
    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")    

    app.when(AddToCartTransaction).asserts(it.IsEqualTo, 1)


@pytest.mark.regression
def test_remove_from_cart_ptp(driver):
    app = Application(driver)
    
    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")
    
    app.when(RemoveFromCartTransaction).asserts(it.IsEqualTo, 0)


@pytest.mark.smoke
def test_access_cart_empty_ptp(driver):
    app = Application(driver)
    
    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")
    
    app.when(AccessCartEmptyTransaction).asserts(it.IsEqualTo, 0)

@pytest.mark.regression
def test_reset_cart_ptp(driver):
    app = Application(driver)
    
    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")
    
    app.when(AddToCartTransaction).asserts(it.IsEqualTo, 1)
    app.when(ResetApplicationTransaction).asserts(it.IsEqualTo, 0)    

def test_continue_shopping_ptp(driver):
    app = Application(driver)
    
    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")
    
    app.when(ContinueCartTransaction).then(it.Contains, "inventory")
