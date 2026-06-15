import requests


class YouGileApi:
    def __init__(self, login, password, company_name, token, user_id):
        self.login = login
        self.password = password
        self.company_name = company_name
        self.base_url = "https://ru.yougile.com/api-v2"
        self.token = token
        self.user_id = user_id
        self.company_id = self.get_company_id()

    def get_company_id(self):
        url = f"{self.base_url}/auth/companies"
        payload = {
            "login": self.login,
            "password": self.password,
            "name": self.company_name
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        for company in data["content"]:
            if company["name"] == self.company_name:
                return company["id"]

        raise Exception(f"Компания {self.company_name} не найдена")

    def get_projects(self):
        """Получает список проектов, используя токен из .env"""
        url = f"{self.base_url}/projects"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(url, headers=headers)
        data = response.json()
        return data.get("content", [])

    def create_project(self, title, description=None):
        url = f"{self.base_url}/projects"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        payload = {
            "title": title,
            "users": {
                self.user_id: "admin"
            }
        }
        if description:
            payload["description"] = description

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        if "id" not in data:
            raise Exception(f"Не удалось создать проект: {data}")

        return data["id"]

    def update_project(self, project_id, new_title=None, new_description=None):
        """Обновляет проект по ID"""
        url = f"{self.base_url}/projects/{project_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        payload = {}
        if new_title:
            payload["title"] = new_title
        if new_description:
            payload["description"] = new_description

        response = requests.put(url, json=payload, headers=headers)
        return response.json()

    def get_project(self, project_id):
        """Получает проект по ID"""
        url = f"{self.base_url}/projects/{project_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(url, headers=headers)
        return response.json()
