#pip install pytest-rerunfailures
#Чтобы указать количество перезапусков для каждого из упавших тестов, нужно добавить в командную строку параметр:

# "--reruns n", где n — это количество перезапусков. Если при повторных запусках тесты пройдут успешно, то и прогон
# тестов будет считаться успешным. Количество перезапусков отображается в отчёте, благодаря чему можно позже анализировать
# проблемные тесты.
# Дополнительно мы указали параметр "--tb=line", чтобы сократить лог с результатами теста. Можете почитать подробнее про
# настройку вывода в документации PyTest: