# Telegram-бот для игры в крестики-нолики

## Финальный проект AAA.Python Advanced

Устанавливаем менеджер зависимостей, зависимости, активируем

1. python -m pip install pdm
2. pdm install
3. eval $(pdm venv activate)

Запуск бота

4. make start или python ./src/main.py

Запуск тестов

5. make test или cd src && python -m pytest ../tests && cd ..

### Модуль src
- config.py: 

класс config, чтобы достать нужные секреты из .env и переменных среды
- consts.py

константы с полями, значениями ходов и т. п.

- game.py

бизнес логика: старт, обработка сообщений, условий победы, окончания игры

- main.py

создание application, добавление хэндлеров, запуск бота

- utils.py

вспомогательные функции

### Модуль tests

- test_game.py

Тестирование функции game, корректной логики

- test_win.py

Тестрование функции won, корректной обработки условий победы