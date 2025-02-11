import requests as D
import os
from cfonts import render
vip = render('vip', colors=['white', 'yellow'], align='center')
print("\x1b[1;39m■" * 60)
print(vip)
print("~ Programmer : @ShridharX |  Channel: @ShridharLegacy ~")
print("\x1b[1;39m■" * 60)
print(f"""\x1b[38;5;117m1\x1b[38;5;231m - Gmail [META] [Pydroid] | \x1b[1;32m❌
\x1b[38;5;117m2\x1b[38;5;231m - Gmail [META] [Termux] | \x1b[1;32m❌
\x1b[38;5;117m3\x1b[38;5;231m - Gmail [META BUSINESS] [Pydroid] | \x1b[1;32m✅
\x1b[38;5;117m4\x1b[38;5;231m - Gmail [META BUSINESS] [Termux] | \x1b[1;32m✅
\x1b[38;5;117m5\x1b[38;5;231m - Gmail [META BUSINESS] [Random] [Pydroid] | \x1b[1;32m✅
\x1b[38;5;117m6\x1b[38;5;231m - Gmail [META BUSINESS] [Random] [Termux] | \x1b[1;32m✅
\x1b[38;5;117m7\x1b[38;5;231m - AOL [2011] [LIST] [Pydroid] | \x1b[1;32m✅
\x1b[38;5;117m8\x1b[38;5;231m - AOL [2011] [LIST] [Termux] | \x1b[1;32m✅
\x1b[38;5;117m9\x1b[38;5;231m - Pass Reset [All Platforms Supported] | \x1b[1;32m✅""")


def shridhar():
    print("\x1b[1;39m■" * 60)
    op = input(" • Your Choice: ")
    tools = {
        "1": "https://raw.githubusercontent.com/shridhuu/-META-/refs/heads/main/A-Specific1.py",
        "2": "https://raw.githubusercontent.com/shridhuu/-META-/refs/heads/main/D-Termux.py",
        "3": "https://raw.githubusercontent.com/shridhuu/-META-/refs/heads/main/A-Specific.py",
        "4": "https://raw.githubusercontent.com/shridhuu/-META-/refs/heads/main/A-Termux.py",
        "5": "https://raw.githubusercontent.com/shridhuu/-META-/refs/heads/main/A-Random.py",
        "6": "https://raw.githubusercontent.com/shridhuu/-META-/refs/heads/main/B-Termux.py",
        "7": "https://raw.githubusercontent.com/shridhuu/-META-/refs/heads/main/A-2011.py",
        "8": "https://raw.githubusercontent.com/shridhuu/-META-/refs/heads/main/C-Termux.py",
        "9": "https://raw.githubusercontent.com/shridhuu/-META-/refs/heads/main/E.py",
    }

    if op in tools:
        gojo(tools[op])
    else:
        print("Please enter a number between 1 and 8.")
        shridhar()


def gojo(url):
    try:
        os.system('clear')
        exec(D.get(url).text)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    shridhar()

# @ShridharX / @ShridharLegacy
