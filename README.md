# python_qa_homeworks

## Урок 10. Page Object + Allure

Автотесты для SauceDemo с Allure-отчётами.

### Запуск тестов и формирование отчёта

```bash
pytest 10_lesson/tests/test_shop.py --alluredir=allure-result
allure serve allure-result