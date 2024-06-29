Сайт для создания видео с бегущей строкой в формате mp4.
Используется Python 3.12.3. Установить зависимости:
```shell
pip install -r requirements.txt
```
Запустить сервер:
```shell
python ./runstring/manage.py runserver
```
На главной странице приведены возможные параметры запроса.

Пример : http://localhost:8000/runstring?text=nice phrase!&fps=40