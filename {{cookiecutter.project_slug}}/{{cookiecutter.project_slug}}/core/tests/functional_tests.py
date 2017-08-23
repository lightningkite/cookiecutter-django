import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver


class FunctionalTests(StaticLiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=options)

    def tearDown(self):
        self.driver.quit()

    def test_get_home_page(self):
        self.driver.get('{0}'.format(self.live_server_url))
        self.assertIn('{{cookiecutter.project_name}}', self.driver.title)
