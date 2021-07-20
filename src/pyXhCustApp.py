import os
import sys
from os.path import isfile, join
from pathlib import Path


def is_win():
    return sys.platform == 'win32'


def is_linux():
    return sys.platform == 'linux'


def separator():
    if is_win():
        return '\\'
    elif is_linux():
        return '/'
    else:
        raise Exception("Unknown separator")


def _has_file(home, name: str) -> bool:
    return len([fileName for fileName in os.listdir(home) if fileName == name and isfile(join(home, fileName))]) == 1


def _get_file_content(home: str, name: str) -> str:
    if _has_file(home, name):
        with open(join(home, name), 'r') as file:
            return file.read()
    else:
        return None

def _rm_file(home:str, name:str):
    os.remove(join(home, name))


def _kv_file_name(key: str) -> str:
    return "%s.kv" % (key)


def _set_kv(home: str, key: str, value: str):
    with open(join(home, _kv_file_name(key)), 'w') as file:
        file.write(value)


def _get_kv(home: str, key: str) -> str:
    if _has_file(home, _kv_file_name(key)):
        with open(join(home, _kv_file_name(key))) as file:
            return file.read()
    else:
        return None

def _rm_kv(home:str,key:str):
    if _has_file(home, _kv_file_name(key)):
        _rm_file(home, _kv_file_name(key))

_PROXY_VAL = "proxy"


class CustApp:
    def __init__(self, home: str, name: str):
        self.separator = separator()
        self.home = "%s%s.custApp%s%s" % (home, self.separator, self.separator, name)
        if os.path.exists(self.home) and os.path.isfile(self.home):
            raise Exception("Home %s is not directory!" % (self.home))
        elif not os.path.exists(self.home):
            os.makedirs(self.home)

        if not os.path.exists(self.home) or os.path.isfile(self.home):
            raise Exception("Home %s is not valid!" % (self.home))

    def has_proxy(self) -> bool:
        return _has_file(self.home, _PROXY_VAL)

    def proxy_value(self):
        return _get_file_content(self.home, _PROXY_VAL)

    def proxy_valid(self) -> bool:
        if self.has_proxy():
            value = self.proxy_value()
            os.path.exists(value) and os.path.isdir(value)
            return True
        else:
            return True

    def set_kv(self, key: str, value: str):
        _set_kv(self.home, key, value)

    def get_kv(self, key: str):
        return _get_kv(self.home, key)

    def rm_kv(self, key:str):
        _rm_file(self.home, _kv_file_name(key))

    def has_kv(self, key:str):
        _has_file(self.home, _kv_file_name(key))

    @staticmethod
    def appDefault(name: str):
        return CustApp(Path.home(), name)


if __name__ == '__main__':
    # app = CustApp(home, "abc")
    app = CustApp.appDefault("abc")
    print(app.has_proxy())
    app.set_kv('xxx', "xxx")
    app.set_kv('xxx', "yyy")
    print(app.get_kv('xxx'))
    app.rm_kv('xxx')
    print(app.has_kv('xxx'))
    print(app.home)