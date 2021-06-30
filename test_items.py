class TestProductPage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def test_button_add_to_basket_only_one_on_page(self, browser):
        browser.get(self.link)

        add_buttons = browser.find_elements_by_css_selector("#add_to_basket_form .btn-add-to-basket")
        assert len(add_buttons) == 1, "Add button is duplicated"

        add_success_messages = browser.find_elements_by_css_selector("#messages .alert-success")
        assert len(add_success_messages) == 0, "Success message is exists"

        add_button = browser.find_element_by_css_selector("#add_to_basket_form .btn-add-to-basket")
        add_button.click()

        add_success_messages = browser.find_elements_by_css_selector("#messages .alert-success")
        assert len(add_success_messages) > 0, "Add button is not working"
