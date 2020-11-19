from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver') 

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

user_message_input = chrome_browser.find_element_by_id('user-message')
user_message_input.send_keys('Heeeeeey, I wiil FUCK the WORLD!')

show_message_button = chrome_browser.find_element_by_css_selector('#get-input > .btn')
show_message_button.click()

assert 'Show Message' in show_message_button.get_attribute('innerHTML')

output_message = chrome_browser.find_element_by_id('display')

assert 'Heeeeeey, I wiil FUCK the WORLD!' in output_message.text

chrome_browser.quit()