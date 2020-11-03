>>> a = {}
>>> def foo():
...     a = {"a": 1}
...     print(a)
...
>>> foo()
{'a': 1}
>>> print(a)
{}
########################
>>> b = {}
>>> def foo():
...     global b
...     b = {"b": 2}
...     print(b)
...
>>> foo()
{'b': 2}
>>> print(b)
{'b': 2}
###################
>>> c = {}
>>> def foo():
...     nonlocal c
...     c = {"c": 3}
...     print(c)
...
  File "<stdin>", line 2
SyntaxError: no binding for nonlocal 'c' found
>>>
###########################################
>>> def foo():
...     d = {}
...     def bar():
...             d = {"d": 4}
...             print(d)
...     bar()
...     print(d)
...
>>> foo()
{'d': 4}
{}
>>> print(d)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>>
######################################
>>> def foo():
...     f = {}
...     def bar():
...             global f
...             f = {"f": 5}
...             print(f)
...     bar()
...     print(f)
...
>>> foo()
{'f': 5}
{}
>>> print(f)
{'f': 5}
>>>
########################
>>> def foo():
...     g = {}
...     def bar():
...             nonlocal g
...             g = {"g": 6}
...             print(g)
...     bar()
...     print(g)
...
>>> foo()
{'g': 6}
{'g': 6}
>>> print(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'g' is not defined
>>>