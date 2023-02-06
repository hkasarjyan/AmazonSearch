from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    return webdriver.Chrome('../chromedriver/chromedriver.exe')


@pytest.fixture()
def url():
    return "https://amazon.com"
