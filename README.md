
## quick install guide

#### install python 3.6
```bash
$ pip install python
```
#### install Django 2.0
```bash
$ pip install Django
```

verify
```bash
$ python --version
Python 3.6
$ python
Python 3.6.4 |Anaconda custom (64-bit)| (default, Jan 16 2018, 12:04:33)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
```


###  start django development server
```bash
$ python manage.py runserver
```

you will see following output
```bash
Performing system checks...

System check identified some issues:

WARNINGS:
?: (urls.W005) URL namespace 'userandadmin' isn't unique. You may not be able to reverse all URLs in this namespace

System check identified 1 issue (0 silenced).
October 13, 2018 - 13:20:26
Django version 2.0.5, using settings 'COMP9900.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
it means that the server is running at IP 8000, you can visit the web server with your web browser.





