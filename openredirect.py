import requests
import re

with open('urls.txt') as fp:
    urls = fp.readlines()

f = open("output.txt", "w")

params = ['next=', 'url=', 'target=', 'rurl=', 'dest=', 'destination=', 'redir=', 'redirect_uri=', 'redirect_url=', 'redirect=', 'out=', 'view=', 'to=', 'image_url=', 'go=', 'return=', 'returnTo=', 'return_to=', 'checkout_url=', 'continue=', 'return_path=']

for url in urls:
    for param in params:
        if param in url:
            new_url = url.replace(param, param + 'https://google.com/')
            r = requests.get(new_url)
            f.write(str(r.status_code) + ' ' + r.url + '\n')

f.close()
