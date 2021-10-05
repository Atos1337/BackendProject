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

# GraphQL
Перейдите по [адресу](http://127.0.0.1:8000/author-stat) и введите пример запроса:
```bash
{
  authorStat(name: "Александр Дюма") {
    totalCount,
    topBooks(limit: 3) {
      name,
      rating
    },
    ratingStat {
      minRating,
      maxRating,
      averageRating
    }
  }
}
```
Ответом будет статистика по автору, в которой есть количество книг, написанных им, рейтинговая статистика его книг и самые топовые книги по рейтингу (можно выбрать топ сколько книг показывать.
