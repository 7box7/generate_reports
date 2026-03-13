import pytest
import tempfile
import csv
from unittest.mock import patch
from utils import read_csv_files
from reports import median_coffee_report

def test_median_coffee_report() -> None:
    data = [
        {'student': 'Алексей Смирнов', 'coffee_spent': '450'},
        {'student': 'Алексей Смирнов', 'coffee_spent': '500'},
        {'student': 'Алексей Смирнов', 'coffee_spent': '550'},
        {'student': 'Дарья Петрова', 'coffee_spent': '200'},
        {'student': 'Дарья Петрова', 'coffee_spent': '250'},
    ]
    result = median_coffee_report(data)
    
    expected = [
        ('Алексей Смирнов', 500.0),
        ('Дарья Петрова', 225.0)
    ]
    
    assert result == expected

def test_read_csv_files() -> None:
    data = [
        {'student': 'Test', 'date': '2024-01-01', 'coffee_spent': '100', 'sleep_hours': '8', 'study_hours': '5', 'mood': 'good', 'exam': 'Math'}
    ]
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        temp_file = f.name

    result = read_csv_files([temp_file])
    assert len(result) == 1
    assert result[0]['student'] == 'Test'
    assert result[0]['coffee_spent'] == '100'

    import os
    os.unlink(temp_file)

def test_read_csv_files_with_headers() -> None:
    data = [
        {'student': 'Test', 'coffee_spent': '100'}
    ]
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['student', 'coffee_spent'])
        writer.writeheader()
        writer.writerows(data)
        temp_file = f.name

    result = read_csv_files([temp_file], headers=['student', 'coffee_spent'])
    assert len(result) == 1
    assert result[0]['student'] == 'Test'
    assert result[0]['coffee_spent'] == '100'

    import os
    os.unlink(temp_file)

def test_read_csv_files_file_not_found() -> None:
    with pytest.raises(SystemExit):
        read_csv_files(['nonexistent.csv'])

def test_integration_math_csv() -> None:
    data = read_csv_files(['math.csv'], headers=['student', 'coffee_spent'])
    result = median_coffee_report(data)

    expected = [
        ('Иван Кузнецов', 650.0),
        ('Дмитрий Морозов', 570.0),
        ('Михаил Павлов', 550.0),
        ('Никита Соловьев', 530.0),
        ('Алексей Смирнов', 500.0),
        ('Сергей Козлов', 440.0),
        ('Павел Новиков', 420.0),
        ('Артем Григорьев', 390.0),
        ('Елена Волкова', 310.0),
        ('Дарья Петрова', 250.0),
        ('Татьяна Васильева', 250.0),
        ('Анна Белова', 190.0),
        ('Ольга Новикова', 180.0),
        ('Виктория Федорова', 140.0),
        ('Мария Соколова', 120.0)
    ]

    assert result == expected

def test_integration_physics_csv() -> None:
    data = read_csv_files(['physics.csv'], headers=['student', 'coffee_spent'])
    result = median_coffee_report(data)

    expected = [
        ('Иван Кузнецов', 700.0),
        ('Дмитрий Морозов', 610.0),
        ('Михаил Павлов', 590.0),
        ('Никита Соловьев', 560.0),
        ('Алексей Смирнов', 530.0),
        ('Сергей Козлов', 480.0),
        ('Павел Новиков', 450.0),
        ('Артем Григорьев', 420.0),
        ('Елена Волкова', 330.0),
        ('Дарья Петрова', 310.0),
        ('Татьяна Васильева', 270.0),
        ('Анна Белова', 210.0),
        ('Ольга Новикова', 200.0),
        ('Виктория Федорова', 150.0),
        ('Мария Соколова', 140.0)
    ]

    assert result == expected

def test_integration_programming_csv() -> None:
    data = read_csv_files(['programming.csv'], headers=['student', 'coffee_spent'])
    result = median_coffee_report(data)
    
    expected = [
        ('Иван Кузнецов', 780.0),
        ('Дмитрий Морозов', 670.0),
        ('Михаил Павлов', 650.0),
        ('Никита Соловьев', 610.0),
        ('Алексей Смирнов', 580.0),
        ('Сергей Козлов', 520.0),
        ('Павел Новиков', 500.0),
        ('Артем Григорьев', 470.0),
        ('Елена Волкова', 380.0),
        ('Дарья Петрова', 360.0),
        ('Татьяна Васильева', 300.0),
        ('Анна Белова', 220.0),
        ('Ольга Новикова', 220.0),
        ('Мария Соколова', 160.0),
        ('Виктория Федорова', 160.0)
    ]
    
    assert result == expected

def test_combined_reports() -> None:
    data = read_csv_files(['math.csv', 'physics.csv', 'programming.csv'], headers=['student', 'coffee_spent'])
    result = median_coffee_report(data)

    assert isinstance(result, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

    medians = [item[1] for item in result]
    
    assert medians == sorted(medians, reverse=True)

def test_main_function(capsys) -> None:
    data = [
        {'student': 'Test', 'coffee_spent': '100'}
    ]
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['student', 'coffee_spent'])
        writer.writeheader()
        writer.writerows(data)
        temp_file = f.name

    with patch('sys.argv', ['main.py', '--files', temp_file, '--report', 'median-coffee']):
        from main import main
        main()

    captured = capsys.readouterr()
    assert 'Test' in captured.out
    assert '100' in captured.out

    import os
    os.unlink(temp_file)

def test_main_unknown_report(capsys) -> None:
    with patch('sys.argv', ['main.py', '--files', 'unknown.csv', '--report', 'unknown']):
        from main import main
        with pytest.raises(SystemExit) as excinfo:
            main()
        assert excinfo.value.code == 1

    captured = capsys.readouterr()
    assert "Ошибка: неизвестный отчет 'unknown'" in captured.err

def test_median_coffee_report_invalid_spend() -> None:
    data = [
        {'student': 'A', 'coffee_spent': '100'},
        {'student': 'A', 'coffee_spent': '////'},
        {'student': 'A', 'coffee_spent': '200'},
    ]
    result = median_coffee_report(data)
    
    expected = [
        ('A', 150.0)
    ]
    
    assert result == expected
