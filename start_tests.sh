python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

pytest TestsPython/tests/main_menu_page_test.py
pytest TestsPython/tests/game_play_test.py
pytest TestsPython/tests/start_page_test.py
