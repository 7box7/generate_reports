# Добавление нового отчета

Чтобы добавить новый отчет в систему, следуйте этим шагам:

## 1. Создайте функцию обработки в `reports.py`

Напишите функцию, которая принимает `data` (список словарей из CSV) и возвращает список кортежей для отчета.

Пример:
```python
def new_report_function(data):
    # Логика обработки данных
    # Возвращает list of tuples, например [(item1, value1), (item2, value2)]
    return processed_data
```

Функция должна быть добавлена в конец файла `reports.py`.

## 2. Обновите `main.py`

### Добавьте отчет в словарь REPORTS
```python
REPORTS = {
    'median-coffee': median_coffee_report,
    'new-report': new_report_function,  # Добавьте эту строку
}
```

### Добавьте требуемые столбцы в REQUIRED_HEADERS
Укажите, какие столбцы нужны для отчета. Если нужны все столбцы, укажите `None`.
```python
REQUIRED_HEADERS = {
    'median-coffee': ['student', 'coffee_spent'],
    'new-report': ['column1', 'column2'],  # Или None для всех столбцов
}
```

### Добавьте заголовки таблицы в HEADERS
```python
HEADERS = {
    'median-coffee': ['Студент', 'Медиана трат на кофе'],
    'new-report': ['Заголовок1', 'Заголовок2'],  # Добавьте эту строку
}
```

## 3. Тестирование

Запустите скрипт с новым отчетом:
```
python main.py --files file.csv --report new-report
```

Убедитесь, что отчет выводится корректно в виде таблицы.