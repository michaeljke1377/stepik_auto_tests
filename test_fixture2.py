import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


test_results = []

@pytest.mark.parametrize("link", [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1",
])


def test_guest_should_see_login_link(browser, link):
    browser.get(link)

    # Ожидание и клик по кнопке входа
    login_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    )
    login_button.click()

    # Ожидание появления полей логина
    login_field = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.ID, "id_login_email"))
    )
    login_field.send_keys("mipo_01@mail.ru")

    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("1234567890ь")


    # Клик по кнопке "Войти"
    submit_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-form__btn"))
    )
    submit_button.click()

    time.sleep(3)

    try:
        retest_button = WebDriverWait(browser, timeout=5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn.white"))
        )
        print("\nНайдена кнопка 'Решить заново' - нажимаю...")
        retest_button.click()
        time.sleep(2)

    except TimeoutException:
        print("\nКнопки 'Решить заново' нет - это первая попытка")


    field_write_answer = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="ember-text-area ember-view textarea string-quiz__textarea"]'))
    )
    field_write_answer.click()

    answer = math.log(int(time.time()))
    answer_str = str(answer)
    field_write_answer.send_keys(answer_str)

    time.sleep(3)

    # Кнопка "Отправить"
    button_send = WebDriverWait(browser, timeout=30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="submit-submission"]'))
    )
    button_send.click()

    # Получить текст из подсказки
    hint_element = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
    )
    hint_text = hint_element.text

    # Проверить, правильный ли ответ
    passed = "Correct!" in hint_text

    # СОХРАНИТЬ РЕЗУЛЬТАТ В СПИСОК
    test_results.append({
        'link': link,
        'hint_text': hint_text,
        'passed': passed
    })

    # Вывести результат текущего теста
    print(f"\n{'=' * 60}")
    print(f"Ссылка: {link}")
    print(f"Текст ответа: '{hint_text}'")
    print(f"{'=' * 60}")

    # Тест упадет, если не "Correct!"
    assert passed, f"Ожидался 'Correct!', получили: '{hint_text}'"




