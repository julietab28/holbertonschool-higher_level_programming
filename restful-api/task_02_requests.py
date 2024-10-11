#!/usr/bin/python3

import requests, json, csv

def fetch_and_print_posts():
    resp = requests.get('https://jsonplaceholder.typicode.com/posts')

    print("Status Code: {}".format(resp.status_code))

    if resp.status_code == 200:
        dic = resp.json()
        for i in dic:
            print(i["title"])

def fetch_and_save_posts():
    resp = requests.get('https://jsonplaceholder.typicode.com/posts')

    if resp.status_code == 200:
        dic = resp.json()

        with open('posts.csv', 'w', encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i in dic:
                writer.writerow({'id': i["id"], 'title' : i["title"], 'body' : i["body"]})