from sys import executable
import pytest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Example 1

# class TeatBrowser1(LiveServerTestCase):
#     def test_example(self):
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title

# Example 2

# Here we'll perform the same task as above but in headless mode.
# class TestBrowser2(LiveServerTestCase):
#     def test_example(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title

# Example 3

# Using Pytest and Fixture for Chrome
# @pytest.fixture(scope="class")
# def chrome_driver_unit(request):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     request.cls.driver = chrome_driver
#     yield
#     chrome_driver.close()

# Next we build the test
# @pytest.mark.usefixtures("chrome_driver_unit")
# class Test_Chrome_Url(LiveServerTestCase):
#     def test_url_open(self):
#         self.driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in self.driver.title

# Example 4

# This test will use both browsers Chrome and Firefox for testing.
# @pytest.fixture(params=["chrome", "firefox"], scope="class")
# def driver_init(request):
#     if request.param == "chrome":
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         web_driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
#     if request.param == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.add_argument("--headless")
#         web_driver = webdriver.Firefox(executable_path=r"./geckodriver", options=options)
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()

# Test
@pytest.mark.usefixtures("driver_init")
class Test_Chrome_url:
    def test_url_open(self, live_server):
        self.driver.get(("%s%s" % (live_server.url, "/admin/")))
        assert "Log in | Django site admin" in self.driver.title





