Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={"mon","tue","wed"}
type(s)
<class 'set'>
s.add("thru")
s
{'tue', 'wed', 'mon', 'thru'}
s.update("fri")
s
{'tue', 'wed', 'r', 'thru', 'f', 'i', 'mon'}
s.discard("tue")
s
{'wed', 'r', 'thru', 'f', 'i', 'mon'}
s.discard("tue")
s.remove("tue")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.remove("tue")
KeyError: 'tue'
s
{'wed', 'r', 'thru', 'f', 'i', 'mon'}


D={}
type(D)
<class 'dict'>
>>> D={"101":"Civil","102":"ME", "105":"CSE"}
>>> D
{'101': 'Civil', '102': 'ME', '105': 'CSE'}
>>> D={101:"CE",102:"ME",105:"CSE"}
>>> D
{101: 'CE', 102: 'ME', 105: 'CSE'}
>>> D.keys()
dict_keys([101, 102, 105])
>>> D.values()
dict_values(['CE', 'ME', 'CSE'])
>>> D[105]
'CSE'
>>> D
{101: 'CE', 102: 'ME', 105: 'CSE'}
>>> 
>>> D[105]="CSE(IOT)"
>>> D
{101: 'CE', 102: 'ME', 105: 'CSE(IOT)'}
>>> D.pop(105)
'CSE(IOT)'
>>> D
{101: 'CE', 102: 'ME'}
>>> D.items()
dict_items([(101, 'CE'), (102, 'ME')])
>>> D.update({105:["CSE","CSE(IOT)"]})
>>> D
{101: 'CE', 102: 'ME', 105: ['CSE', 'CSE(IOT)']}
>>> D.update({105:["CSE","CSE(IOT)"]})
>>> D
{101: 'CE', 102: 'ME', 105: ['CSE', 'CSE(IOT)']}
>>> D={101: 'CE', 102: 'ME', 105: ['CSE', 'CSE(IOT)']}
>>> D[105{1}]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> D=[105][1]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    D=[105][1]
IndexError: list index out of range
>>> D[105][1]
'CSE(IOT)'
