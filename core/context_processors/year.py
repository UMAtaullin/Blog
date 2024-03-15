import datetime


def year(request):
    """Добавляем переменную с актуальным годом."""
    now = datetime.datetime.now()
    return {
        'year': now.year
    }
