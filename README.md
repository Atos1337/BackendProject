# BackendProject
Чтобы запустить приложение:
```bash
uvicorn main:app --reload
```

Далее можно перейти к сгенерированной Swagger-документации по [ссылке](http://127.0.0.1:8000/docs)

# Тесты
Для запуска юнит-тестов выполните эту команду из корневой директории:
```bash
python -m unittest discover -s tests/unit/
```
Для запуска интеграционных:
```bash
python -m unittest discover -s tests/integrate/
```
Для запуска всех:
```bash
python -m unittest discover -s tests/
```
