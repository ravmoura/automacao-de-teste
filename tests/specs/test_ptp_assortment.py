from guara.application import Application
import pytest

from guara import it
from tests.transactions.sort_by_price_ascending_transaction import SortByPriceAscendingTransaction
from tests.transactions.sort_by_price_descending_transaction import SortByPriceDescendingTransaction
from tests.transactions.sort_by_name_ascending_transaction import SortByNameAscendingTransaction
from tests.transactions.sort_by_name_descending_transaction import SortByNameDescendingTransaction
from tests.transactions.login_transaction import LoginWithTransaction
from tests.fixtures.driver import driver

@pytest.mark.regression
def test_sort_by_price_ascending(driver):    
    app = Application(driver)
    
    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")    

    app.when(SortByPriceAscendingTransaction).then(it.IsTrue) 

@pytest.mark.regression                                                   
def test_sort_by_price_descending(driver):
    app = Application(driver)
    
    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory") 

    app.when(SortByPriceDescendingTransaction).then(it.IsTrue)

@pytest.mark.regression
def test_sort_by_name_ascending(driver):
    app = Application(driver)
    
    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")

    app.when(SortByNameAscendingTransaction).then(it.IsTrue)

@pytest.mark.regression
def test_sort_by_name_descending(driver):
    app = Application(driver)
    
    app.given(
        LoginWithTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")   

    app.when(SortByNameDescendingTransaction).then(it.IsTrue)