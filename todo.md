Создать базовый шаблон layout.html с навигационной панелью и одной ссылкой на домашнюю страничку+

Обновить view.home:
- сделать запрос к классу Publisher и извлечь все объекты / пример qs = MyModel.objects.all() / получешь QuerySet+
- в функции render в качестве параметра добавить словарь с одним элементом - результатом запроса+

Обновить шаблон home для отображения списка Издателей (Publisher):+
- извлечь из переданного функцие рендер словаря результат запроса+
- пройти по нему циклом извлекая поле 'name'+
На странице Publisher где перечень книг


URL
[      ]
Submit


1  www.dkfj.com
2  www.dkldflasdf.com    

py -3 -m venv .venv
.venv\scripts\activate

python manage.py makemigrations
python manage.py migrate

$ python manage.py createsuperuser

<!-- -->
