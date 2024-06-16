my_bat.write('''@echo off
echo Loading...
ping -n 6 127.0.0.1 > nul
python main.py
pause
''')

my_bat.close()