from requests import get
a = get('https://stepic.org/favicon.ico').headers['Server']
print(a)