import requests
from http import HTTPStatus

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print ('status Code:',r.status_code)
    if r.status_code == HTTPStatus.OK:
        data = r.json()  
        if data: 
            for d in data:
                print(d['title'])
def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print ('status Code:',r.status_code)
    if r.status_code == HTTPStatus.OK:
        data = r.json()
        print(data)
        if data:
            for d in data:
                


fetch_and_print_posts()
fetch_and_save_posts()