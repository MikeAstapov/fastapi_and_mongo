# Приложение FastAPI с методами CRUD для управления студентами

### Описание приложения:
- Данная презентация предназначена для приложения FastAPI, которое предоставляет методы CRUD (Create, Read, Update, Delete) для управления информацией о студентах.  
- Приложение развертывается с помощью docker-compose с использованием двух контейнеров: контейнера приложения и контейнера базы данных.   Для управления моделями данных используется библиотека Pydantic, для взаимодействия с MongoDB - библиотека PyMongo, а для запуска сервера FastAPI - библиотека Uvicorn.

### Функциональность:
- **Создание студента (Create)**
     - URL: /students
     - Метод: POST
     - Описание: Создает новую запись о студенте с заданными параметрами.
     - Параметры:
     - id (int, обязательный) - уникальный идентификатор студента.
     - first_name (str, обязательный) - имя студента.
     - last_name (str, обязательный) - фамилия студента.
     - course (int, обязательный) - курс, на котором учится студент.
     - average_grade (float, обязательный) - средний балл студента.
- **Получение информации о студенте (Read)**  
     - URL: /students/{id}
     - Метод: GET
     - Описание: Возвращает информацию о студенте с заданным идентификатором.
     - Параметры:
     - id (int, обязательный) - идентификатор студента.
- **Обновление информации о студенте (Update)**
     - URL: /students/{id}
     - Метод: PUT**
     - Описание: Обновляет информацию о студенте с заданным идентификатором.
     - Параметры:
     - id (int, обязательный) - идентификатор студента.
     - first_name (str, необязательный) - новое имя студента.
     - last_name (str, необязательный) - новая фамилия студента.
     - course (int, необязательный) - новый курс, на котором учится студент.
     - average_grade (float, необязательный) - новый средний балл студента.
- **Удаление студента (Delete)**
     - URL: /students/{id}
     - Метод: DELETE
     - Описание: Удаляет информацию о студенте с заданным идентификатором.
     - Параметры:
     - id (int, обязательный) - идентификатор студента.
## Для запуска приложения:  
1. git clone https://github.com/MikeAstapov/fastapi_and_mongo.git
2. cd fastapi_and_mongo
3. docker-compose up  
Далее можно использовать встроенный SWAGER , доступный по адресу localhost:8000/docs или другую альтернативу, например PostMan
