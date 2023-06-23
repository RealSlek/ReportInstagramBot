# coding=utf-8
#!/usr/bin/env python3

from libs.animation import colorText

logo = '''

[[black-bright-background]][[yellow]] ██▓ [[yellow]]███▄    █  [[yellow]] ██████ [[yellow]]▄▄▄█████▓ [[yellow]]▄▄▄         [[yellow]] ██▀███  [[yellow]]▓█████ [[yellow]] ██▓███   [[yellow]]▒█████   [[yellow]]██▀███  [[yellow]]▄▄▄█████▓[[reset]]
[[black-bright-background]][[yellow]]▓██▒ [[yellow]]██ ▀█   █ ▒[[yellow]]██    ▒ [[yellow]]▓  ██▒ ▓▒▒[[yellow]]████▄       [[yellow]]▓██ ▒ ██▒[[yellow]]▓█   ▀ [[yellow]]▓██░  ██▒▒[[yellow]]██▒  ██▒▓[[yellow]]██ ▒ ██▒[[yellow]]▓  ██▒ ▓▒[[reset]]
[[black-bright-background]][[yellow]]▒██▒▓[[yellow]]██  ▀█ ██▒░[[yellow]] ▓██▄   [[yellow]]▒ ▓██░ ▒░▒[[yellow]]██  ▀█▄     [[yellow]]▓██ ░▄█ ▒[[yellow]]▒███   [[yellow]]▓██░ ██▓▒▒[[yellow]]██░  ██▒▓[[yellow]]██ ░▄█ ▒[[yellow]]▒ ▓██░ ▒░[[reset]]
[[black-bright-background]][[yellow]]░██░▓[[yellow]]██▒  ▐▌██▒ [[yellow]] ▒   ██▒[[yellow]]░ ▓██▓ ░ ░[[yellow]]██▄▄▄▄██    [[yellow]]▒██▀▀█▄  [[yellow]]▒▓█  ▄ [[yellow]]▒██▄█▓▒ ▒▒[[yellow]]██   ██░▒[[yellow]]██▀▀█▄  [[yellow]]░ ▓██▓ ░ [[reset]]
[[black-bright-background]][[yellow]]░██░▒[[yellow]]██░   ▓██░▒[[yellow]]██████▒▒[[yellow]]  ▒██▒ ░  [[yellow]]▓█   ▓██▒   [[yellow]]░██▓ ▒██▒[[yellow]]░▒████▒[[yellow]]▒██▒ ░  ░░[[yellow]] ████▓▒░░[[yellow]]██▓ ▒██▒[[yellow]]  ▒██▒ ░ [[reset]]
[[black-bright-background]][[yellow]]░▓  ░[[yellow]] ▒░   ▒ ▒ ▒[[yellow]] ▒▓▒ ▒ ░[[yellow]]  ▒ ░░    [[yellow]]▒▒   ▓▒█░   [[yellow]]░ ▒▓ ░▒▓░[[yellow]]░░ ▒░ ░[[yellow]]▒▓▒░ ░  ░░[[yellow]] ▒░▒░▒░ ░[[yellow]] ▒▓ ░▒▓░[[yellow]]  ▒ ░░   [[reset]]
[[black-bright-background]][[yellow]] ▒ ░░[[yellow]] ░░   ░ ▒░░[[yellow]] ░▒  ░ ░[[yellow]]    ░     [[yellow]] ▒   ▒▒ ░   [[yellow]]  ░▒ ░ ▒░[[yellow]] ░ ░  ░[[yellow]]░▒ ░      [[yellow]] ░ ▒ ▒░  [[yellow]] ░▒ ░ ▒░[[yellow]]    ░    [[reset]]
[[black-bright-background]][[yellow]] ▒ ░ [[yellow]]  ░   ░ ░ ░[[yellow]]  ░  ░  [[yellow]]  ░       [[yellow]] ░   ▒      [[yellow]]  ░░   ░ [[yellow]]   ░   [[yellow]]░░       ░[[yellow]] ░ ░ ▒   [[yellow]] ░░   ░ [[yellow]]  ░      [[reset]]
[[black-bright-background]][[yellow]] ░   [[yellow]]        ░  [[yellow]]     ░  [[yellow]]          [[yellow]]     ░  ░   [[yellow]]   ░     [[yellow]]   ░  ░[[yellow]]          [[yellow]]   ░ ░   [[yellow]]  ░     [[yellow]]         [[reset]]
                                                                                                  

                                           
'''

def print_logo():
    print(colorText(logo))