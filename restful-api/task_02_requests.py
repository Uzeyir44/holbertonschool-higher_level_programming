#!/usr/bin/python3
"""
This module contains fetch_and_print_posts
fetch_and_save_posts
"""
import requests
import csv


def fetch_and_print_posts():
    """
    This function gets posts from api and prints
    the titles
    """
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status code: {res.status_code}")

    if (res.status_code == 200):
        data = res.json()

        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    """
    This function gets posts from api, cleans json file
    and converts it to csv
    """
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    if (res.status_code == 200):
        data = res.json()
        clean_data = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in data
        ]

        with open('posts.csv', mode='w', newline='') as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(clean_data)
