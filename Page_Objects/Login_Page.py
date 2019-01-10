"""
This class contains all Page Objects for the Login page.
"""
from Page_Objects.BasePage import Header

class Login_Page(Header):
    email_input = "email"
    password_input = "passwd"
    sign_in_button = "SubmitLogin"