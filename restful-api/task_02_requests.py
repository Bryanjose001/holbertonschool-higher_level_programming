#!/usr/bin/python3

import requests
import csv
from http import HTTPStatus

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print ('Status Code:',r.status_code)
    if r.status_code == HTTPStatus.OK:
        data = r.json()  
        if data: 
            for d in data:
                print(d['title'])
def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == HTTPStatus.OK:
        data = r.json()
        # Check if Data is not empty
        if data:
            # Iterate through data
            post_list = []
            for post in data:
                # For each row of data, get the id, title and body
                id = post['id']
                title = post['title']
                body = post['body']
                # Store the information inside a dictionary
                post_dict = {
                    'id': id,
                    'title': title,
                    'body': body
                }
                # Add the dictionary to a list
                post_list.append(post_dict) 
            # Define output file path
            filename = "posts.csv"

            # Get the fieldnames (CSV column headers)
            fieldnames = post_list[0].keys()

            # Write to CSV
            with open(filename, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()  # Write column names
                writer.writerows(post_list)  # Write all rows
    


    # use list of dictionaries to print contents inside a CSV file
      
    #     structured_posts = [{'id': post['id'], 'title': post['title'],
    #                         'body': post['body']} for post in posts]

    #     with open('posts.csv', mode='w', newline='',
    #               encoding='utf-8') as csv_file:
    #         fieldnames = ['id', 'title', 'body']
    #         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    #         writer.writeheader()
    #         writer.writerows(structured_posts)
    #     print("Data has benn succesfully written to posts.csv")
    # else:
    #     print(f"Failed to fetch posts. Status code: {r.status_code}")

fetch_and_save_posts()