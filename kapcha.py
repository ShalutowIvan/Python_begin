# # -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# import unittest, time, re


# class UntitledTestCase(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(executable_path=r'')
#         self.driver.implicitly_wait(30)
#         self.base_url = "https://www.google.com/"
#         self.verificationErrors = []
#         self.accept_next_alert = True

#     def test_untitled_test_case(self):
#         driver = self.driver
#         driver.get("https://vk.com/ishalutov")
#         driver.find_element_by_xpath("//li[@id='l_pr']/a/span").click()
#         driver.find_element_by_xpath("//li[@id='l_msg']/a/span").click()
#         driver.get("https://vk.com/im")
#         driver.find_element_by_xpath("//li[@id='l_fr']/a/span").click()
#         driver.get("https://vk.com/friends")
#         driver.find_element_by_xpath("//li[@id='l_gr']/a/span").click()
#         driver.get("https://vk.com/groups")
#         driver.find_element_by_xpath("//li[@id='l_aud']/a/span").click()

#     def is_element_present(self, how, what):
#         try:
#             self.driver.find_element(by=how, value=what)
#         except NoSuchElementException as e:
#             return False
#         return True

#     def is_alert_present(self):
#         try:
#             self.driver.switch_to_alert()
#         except NoAlertPresentException as e:
#             return False
#         return True

#     def close_alert_and_get_its_text(self):
#         try:
#             alert = self.driver.switch_to_alert()
#             alert_text = alert.text
#             if self.accept_next_alert:
#                 alert.accept()
#             else:
#                 alert.dismiss()
#             return alert_text
#         finally:
#             self.accept_next_alert = True

#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)


# if __name__ == "__main__":
#     unittest.main()


# # TensorFlow and tf.keras
# import tensorflow as tf

# # Helper libraries
# import numpy as np
# import matplotlib.pyplot as plt

# print(tf.__version__)




