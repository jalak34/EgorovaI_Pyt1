import requests
from settings import LOGIN, PASSWORD, COMPANY_ID

url = "https://ru.yougile.com/api-v2"

# получить токен
payload = {
     "login": LOGIN,
     "password": PASSWORD,
     "companyId": COMPANY_ID
 }
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url + '/auth/keys',
                            json=payload, headers=headers)

print(response.status_code)
print(response.text)



# успешное создание проекта
def test_create_project():
     payload = {
     "title": "Создание проекта",
     "users": {
     "93104406-2242-421b-aa9a-1044a6672af5": "admin",
       }
     }
     headers = {
     "Content-Type": "application/json",
     "Authorization": 
     "Bearer {token}" # подставить актуальный токен
     }
     response = requests.request("POST", url + "/projects", 
                                json=payload, headers=headers)
     assert response.status_code == 201
     
# создание проекта c пустым именем
def test_create_project_negativ():
     payload = {
     "title": "",
     "users": {
     "93104406-2242-421b-aa9a-1044a6672af5": "admin"
       }
     }
     headers = {
     "Content-Type": "application/json",
     "Authorization": 
     "Bearer {token}"  # подставить актуальный токен
     }
     response = requests.request("POST", url + "/projects",
                                 json=payload, headers=headers)
     assert response.status_code == 400

# получить список проектов
def test_company_list():
     headers = {
     "Content-Type": "application/json",
     "Authorization": 
     "Bearer {token}"  # подставить актуальный токен
     }

     response = requests.request("GET", url + "/projects", 
                                headers=headers)
     assert response.status_code == 200
     print(response.text)


# изменение проекта (название проекта)
def test_change_project():
     payload = {
     "deleted": False,
     "title": "Изменение проекта",
     "users": {
        "93104406-2242-421b-aa9a-1044a6672af5": "admin"
      }
     }
     headers = {
     "Content-Type": "application/json",
     "Authorization": "Bearer {token}"  # подставить актуальный токен
     }
     response = requests.request("PUT", 
                                 url + "/projects/3490b906-42ae-4a31-a42e-22d601043e49", 
                                 json=payload, headers=headers)
     assert response.status_code == 200

# изменение несуществующего проекта 
def test_change_project__negative():
     payload = {
     "deleted": False,
     "title": "Изменение проекта",
     "users": {
        "93104406-2242-421b-aa9a-1044a6672af5": "admin"
      }
     }
     headers = {
     "Content-Type": "application/json",
     "Authorization": 
     "Bearer {token}"  # подставить актуальный токен
     }
     response = requests.request("PUT", 
                                 url + "/projects/3490b906-42ae-4a31-a42e-2155555555",
                                 json=payload, headers=headers)
     assert response.status_code == 404

# получение по id
def test_id_project():
     headers = {
     "Content-Type": "application/json",
     "Authorization": 
     "Bearer {token}"  # подставить актуальный токен
     }
     response = requests.request("GET", url + '/projects/3490b906-42ae-4a31-a42e-22d601043e49', 
                                 headers=headers)
     assert response.status_code == 200
  

# получение по id несуществующего проекта
def test_id_project__negative():
     headers = {
     "Content-Type": "application/json",
     "Authorization": "Bearer {token}"  # подставить актуальный токен
     }
     response = requests.request("GET", 
                                 url + '/projects/3490b906-42ae-4a31-a42e-555555555555',
                                 headers=headers)
     assert response.status_code == 404
    
