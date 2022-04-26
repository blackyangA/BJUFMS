import csv
from pprint import pprint

import requests


# 139.224.192.64


def document_add():
    url = "http://localhost:5903/api/document/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU1MzA3NDEzLCJpYXQiOjE2NTA5ODc0MTMsImp0aSI6IjU5NTRjYzU5YTk4NjQ4MTFhOGNlZjAzZTU5NjM3OGFkIiwidXNlcl9pZCI6MX0.fIagI364mUddD-Vh640fP_9L0xWAhOJ1UtwnHEWg7RU"
    }
    data = {
        'text': '原文',
        'file_no': '案卷级档号',
        'title': '题名',
        'all_sovereign': 1,
        'ecn': '实体分类号',
        'catalogue_no': 1,
        'case_file_no': 1,
        'start_dt': '2022-01-01',
        'end_dt': '2022-04-26',
        'total_pages': 1,
        'poc': '保管期限',
    }

    response = requests.post(url=url, headers=headers, json=data)
    print(f"status_code:{response.status_code}")
    print(response.json())


def test_login():
    # http://139.224.192.64/
    # url = "http://139.224.192.64:5903/api/token/"
    url = "http://localhost:5903/api/token/"
    # headers = {
    #     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    # }
    data = {
        "username": "admin",
        "password": "123456",
    }
    response = requests.post(url=url, data=data)
    print(response.status_code)
    pprint(response.json())


if __name__ == '__main__':
    # test_login()
    document_add()
