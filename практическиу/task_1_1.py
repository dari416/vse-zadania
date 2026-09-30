import sys

print('Версия Python:', sys.version.split()[0])
print('Интерпретатор:', sys.executable)

print('количество путей поиска:', len(sys.path))
for p in sys.path[:4]:
    print(' ', p)
     
import math, random

print('math.pi =', math.pi)
print('random.random() =', random.random())

mods = sorted(sys.modules)
print('всего загруженно модулей:', len(mods))
print('пример:', mods[:5])

public = [n for n in dir(math) if not n.startswith('__')]
print('публичных имен в math:', len(public))
print('первые 8:', public[:8])

print('мой __name__=', __name__)
print('мой __file__=', __file__)


