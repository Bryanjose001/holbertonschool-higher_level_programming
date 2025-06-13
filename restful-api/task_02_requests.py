import requests
import csv
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
    if r.status_code == HTTPStatus.OK:
        data = r.json()
        structured_posts = [{'id': post['id'], 'title': post['title'],
                            'body': post['body']} for post in posts]

        with open('posts.csv', mode='w', newline='',
                  encoding='utf-8') as csv_file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)
        print("Data has benn succesfully written to posts.csv")
    else:
        print(f"Failed to fetch posts. Status code: {r.status_code}")