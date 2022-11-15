#pytest test_abs_project.py

#pip freeze > requirements.txt #сохраняем все версии пакетов

#pip install -r requirements.txt #устанавливаем все пакеты одной командой

#pytest scripts/selenium_scripts
# найти все тесты в директории scripts/selenium_scripts

#pytest test_user_interface.py
# найти и выполнить все тесты в файле

# pytest scripts/drafts.py::test_register_new_user_parametrized
# найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить

# Если запустить PyTest с параметром -v (verbose, то есть подробный),
# то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения:

# PyTest не требует написания дополнительных специфических конструкций в тестах, как того требует unittest.
