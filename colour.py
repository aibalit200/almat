from termcolor import colored # Для установки запустите из командной строки pip install termcolor
print(colored("Зеленый текст (без атрибутов)", "green"))
print(colored("Синии текст текст (подчеркивание)", "blue",  attrs=["underline"]))
print(colored("hello world", "orange",  attrs=["underline"]))
