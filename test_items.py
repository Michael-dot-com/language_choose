from selenium import webdriver
import pytest


class TestCase:
    def test_add_to_basket_button(self, browser, language):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)

        button_text = browser.find_by_css_selector(
            '[value="Add to basket"]').text
        assert button_text == "Add to basket"
