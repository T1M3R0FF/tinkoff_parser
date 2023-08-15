from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.tinkoff.ru/payments/persons/phone/?internal_source=mybank_paybutttons"
driver = webdriver.Chrome()
driver.get(url)


def login():
    number = input('введите номер телефона без +7: ')
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "phoneNumber"))
    )
    phone_input.clear()
    phone_input.send_keys(number)
    phone_input.send_keys(Keys.ENTER)

    verification_code = input("Введите код: ")

    code_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'smsCode'))
    )
    code_input.send_keys(verification_code)
    pwd = input('введите пароль: ')
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password_input.send_keys(pwd)
    password_input.send_keys(Keys.ENTER)

    skip_button = driver.find_element(By.ID, "skip-button")
    skip_button.click()


def parse():
    file = open('tinkoff_users.txt', 'w')
    numbers = ['(995) 184-87-50', '(995) 250-92-49', '(995) 205-77-47', '(995) 424-94-94', '(995) 427-15-36',
               '(995) 123-16-34', '(995) 195-84-09', '(995) 612-19-93', '(995) 963-59-11', '(995) 006-71-60',
               '(995) 549-99-75', '(995) 000-03-52', '(995) 207-47-45', '(993) 210-41-08', '(995) 507-37-55'
               ]
    for number in numbers:
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "phone"))
        )
        input_field.send_keys(Keys.CONTROL + "a")
        input_field.send_keys(Keys.BACKSPACE)
        input_field.send_keys(number)
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.LogoImage__logo_fSW2p[aria-label]'))
            )
            aria_label_value = element.get_attribute('aria-label')
            if aria_label_value == 'Тинькофф банк':
                print(f'{number}: {aria_label_value}')
                file.write(f'{number}')
            else:
                print(f'{number}: нет в тиньке')
        except:
            print(f'{number}: нет в тиньке')


def main():
    login()
    time.sleep(5)
    parse()
    driver.quit()


main()
