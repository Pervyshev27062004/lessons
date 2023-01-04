import requests
r = requests.get('https://api.github.com/events')
print(r)
print(r.status_code)
print(r.headers)

#print(r.text)
###
def download_file(link, name):
    r = requests.get(link)
    open(name, "wb").write(r.content)

download_file(
https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE
)
