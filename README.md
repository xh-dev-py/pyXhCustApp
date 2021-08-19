# Chia Log Processor

A library provide functionality process chia plot log.

# Installation

```python_script
pip install pyXhCustApp
```

```python_script
pip3 install pyXhCustApp
```

# Demo

```python_script
from pyXhCustApp import CustApp
CustApp.appDefault("abc_app")
print(app.has_proxy())
app.set_kv('xxx', "xxx")
app.set_kv('xxx', "yyy")
print(app.get_kv('xxx'))
app.rm_kv('xxx')
print(app.has_kv('xxx'))
print(app.home)
```

```shell script
python -m pyXhCustApp {name_space} list #Show all all
python -m pyXhCustApp {name_space} exist {key} #return true if {key} exists
python -m pyXhCustApp {name_space} value {key} #return value of {key} or None
python -m pyXhCustApp {name_space} set {key} {value} #set {value} to {key}
python -m pyXhCustApp {name_space} remove {key} #remove {key}
```
