from dotenv import load_dotenv
from YouGileApi import YouGileApi
import os

load_dotenv()

LOGIN = os.getenv("YOUGILE_LOGIN")
PASSWORD = os.getenv("YOUGILE_PASSWORD")
COMPANY_NAME = os.getenv("YOUGILE_COMPANY_NAME")
TOKEN = os.getenv("YOUGILE_TOKEN")
USER_ID = os.getenv("YOUGILE_USER_ID")

api = YouGileApi(LOGIN, PASSWORD, COMPANY_NAME, TOKEN, USER_ID)


# def test_get_company_id():
#     company_id = api.get_company_id()

#     assert company_id is not None
#     assert isinstance(company_id, str) and len(company_id) > 0


# def test_get_projects():
#     projects = api.get_projects()

#     assert isinstance(projects, list), "Ответ сервера должен быть списком"

#     for project in projects:
#         assert "id" in project, "У проекта должен быть id"
#         assert "title" in project, "У проекта должно быть title"


def test_create_project_positive():
    # Создаём проект
    project_id = api.create_project("Test Project")

    assert project_id is not None
    assert isinstance(project_id, str)
    assert len(project_id) > 0

    project = api.get_project(project_id)
    assert project["title"] == "Test Project"


def test_create_project_negative():
    # Негативный тест: создание проекта без названия
    try:
        api.create_project("")
        assert False, "Ожидалось исключение, но проект создался"
    except Exception as e:
        assert "Не удалось создать проект" in str(e)


def test_update_project_positive():
    # Создаём проект
    project_id = api.create_project("Project for Update")

    # Обновляем его
    result = api.update_project(project_id, new_title="Updated Project")
    # Проверяем, что обновление прошло успешно
    assert "id" in result or result.get("status") == "ok"

    # Получаем проект по ID и проверяем название
    project = api.get_project(project_id)
    assert project["title"] == "Updated Project"


def test_update_project_negative():
    # Негативный тест: обновление несуществующего проекта
    result = api.update_project("non-existent-id", new_title="New")

    assert "error" in result or "id" not in result


def test_get_project_positive():
    # Создаём проект
    project_id = api.create_project("Project for Get")

    # Получаем его по ID
    project = api.get_project(project_id)

    assert project["id"] == project_id
    assert project["title"] == "Project for Get"


def test_get_project_negative():
    # Негативный тест: получение несуществующего проекта
    result = api.get_project("non-existent-id")

    assert "error" in result or "id" not in result
