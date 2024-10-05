  
Pereval Rest API
-
 #### Проект виртуальной стажировки SkillFactory
***
#### Описание проекта
ФСТР заказала студентам SkillFactory разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет.
В данном проекте мы разработали REST API, которое будет обслуживать мобильное приложение;
***
 #### Внесение информации
Для отправки данных пользователь должен заполнить информацию о себе (регистрация не требуется):
* Фамилия
* Имя
* Отчество
* Электронная почта
* Номер телефона

Также нужно внести информацию о горном перевале:
* Название горного перевала
* Альтернативное название горного перевала
* Произвольный текст (описание) 
* Координаты горного перевала
* Сложность восхождения (в зависимости от времени года)
***
#### Обработка информации
Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.
***
#### Реализация проекта
[![My Skills](https://skillicons.dev/icons?i=py,django,postgres)](https://skillicons.dev)
* Проект написан с использованием языка программирования Python.
* Был задействован фреймворк Django.
* В качестве БД был выбран PostgeSQL
***
#### Описание методов
<b>GET /submitdata/</b>\
Получаем все записи о перевалах.

<b>POST /submitdata/</b>\
Принимает JSON в теле запроса с информацией о перевале. Пример JSON-a:
```commandline
{
  "beauty_title": "string",
  "title": "string",
  "other_titles": "string",
  "connect": "string",
  "user": {
    "email": "user@example.com",
    "fam": "string",
    "name": "string",
    "otc": "string",
    "phone": "string"
  },
  "coords": {
    "latitude": "string",
    "longitude": "string",
    "height": "string"
  },
  "level": {
    "winter": "1А",
    "spring": "1А",
    "summer": "1А",
    "autumn": "1А"
  },
  "images": [
    {
      "data": "string",
      "title": "string"
    }
  ]
}
```
Результат метода: JSON
* status — код HTTP, целое число:\
500 — ошибка при выполнении операции;\
400 — Bad Request (при нехватке полей);\
200 — успех.
* message — строка:\
Причина ошибки (если она была);

<b>GET /submitdata/id</b>\
Получаем одну запись (перевал) по её id с выведением всей информацию о перевале, в том числе статус модерации.

<b>PATCH /submitdata/id</b>\
Позволяет отредактировать существующую запись (замена), при условии что она в статусе "new".

При этом редактировать можно все поля, кроме тех, что содержат ФИО, адрес почты и номер телефона. В качестве результата изменения приходит ответ содержащий следующие данные:

* state:\
1 — удалось отредактировать запись в базе данных.\
0 — отредактировать запись не удалось.
* message:\
сообщение о причине неудачного обновления записи.

<b>GET /submitdata/?user__email=email</b>\
Позволяет получить данные всех объектов, отправленных на сервер пользователем с почтой.

Используется фильтрация по адресу электронной почты пользователя с помощью пакета django-filter. 
***
#### Документация сгенерирована с помощью пакета drf-yasg

Документация swagger:<u>https://127.0.0.1:8000/swagger</u><br>
Документация redoc: <u>http://127.0.0.1:8000/redoc/</u>
***
#### Отчет о покрытии тестами
![](https://github.com/jforsety/perevalAPI/coverage.png?raw=true)




