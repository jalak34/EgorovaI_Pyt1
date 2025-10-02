# Проект автоматизации тестирования интернет-магазина
## Описание проекта
Проект содержит набор автоматизированных тестов для интернет-магазина книг "Читай-город". 
Тесты охватывают функциональность API и UI, тестирование функциональности поиска товара.

## Установка необходимых компонентов
1)	Проверить установлен ли  _Python_, введя в командной строке  команду **python –version**
2)	Проверить установлен ли _pytest_, выполнив команду pytest –version. В случае если, pytest не установлен,  выполнить команду **pip install -U pytest**.
3)	Установить веб-драйвер _Selenium_, выполнив команду **pip3 install selenium**.
4)	Установить браузер (Mozilla Firefox, Chrome) и соответствующий ему драйвер.
5)	Открыть терминал и перейти к рабочей директории (lesson9).
6)	Подключить _Allure_, выполнив команду **pip install allure-pytest**.

## Получение токена
Необходимо зайти на сайт Читай-город (https://www.chitai-gorod.ru/), с помощью инструмента разработчика DevTools во вкладке Application в разделе Cookies перейти в _https://www.chitai-gorod.ru/_ и найти access-tokenб скопировать и применить в token в  файле _test_api.py_ 

## Запуск тестов
### Запуск тестов с помощью pytest
Запуск тестов API
Чтобы запустить тесты API, использовать команду: **pytest test_api.py** или **python -m pytest test_api.py** 

Запуск тестов UI
Чтобы запустить тесты UI, использовать команду: **pytest test_ui.py** или **python -m pytest test_ui.py**

Запуск всех тестов
Чтобы запустить все тесты в проекте, использовать команду: **pytest** или **python -m pytest** 
	
### Запуск всех тестов с помощью allure
1)	Запустить тесты и указать путь к каталогу результатов тестирования: **pytest --alluredir allure-result** или **python -m pytest --alluredir allure-result**
2)	В директории с тестами появится папка _allure-result_, в которой сохранятся отчеты о тестах.
   
#### Генерация отчетов  с помощью allure
1)	Установить _Allure Report_, запустив в терминале VS Code команду **Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression**
2)	Запустить в терминале VS Code команду **scoop install allure** ((Windows) или **brew install allure** (Mac).
3)	Для генерации отчета о тестах запустить команду **allure serve allure-result**, после чего отчет откроется на локальном сервере в окне вашего браузера. 




