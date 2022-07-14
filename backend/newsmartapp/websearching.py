from django import forms
from django.forms import fields
from time import sleep
from celery import shared_task
from .models import WebSearching
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from celery import current_app
from celery import current_task
import celery
from celery.app import default_app


def parse_results(query):
    output = []
    print("Crawling data and creating objects in database ..")
    # query = input('Enter string to search: ')
    session = HTMLSession()
    response = session.get("https://www.google.com/search?q=" + query)
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"

    results = response.html.find(css_identifier_result)

    for result in results:
        title = (result.find(css_identifier_title, first=True).text,)
        link = (result.find(css_identifier_link, first=True).attrs["href"],)
        text = result.find(css_identifier_text, first=True).text
        print(title)

        WebSearching.objects.create(title=title, link=link, text=text)

        item = {"title": title, "link": link, "text": text}

        output.append(item)

    print(output)
    return output


def update_results(input):
    output = []
    print("Updating data...")
    # input = input('Enter string to search: ')
    query = urllib.parse.quote_plus(input)

    session = HTMLSession()
    response = session.get("https://www.google.com/search?q=" + query)
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"

    results = response.html.find(css_identifier_result)

    for result in results:
        title = (result.find(css_identifier_title, first=True).text,)
        link = (result.find(css_identifier_link, first=True).attrs["href"],)
        # text = result.find(css_identifier_text, first=True).text

        # "text": result.find(css_identifier_text, first=True).text,
        # AttributeError: 'NoneType' object has no attribute 'text'

        # print('Updating data1...')
        s = WebSearching(title=title, link=link)
        print("Updating data1...")

        s.save()

        item = {"title": title, "link": link}

        output.append(item)

    print(output)
    return output


def searchingwebinput(input_string):

    output = []
    if not WebSearching.objects.all():
        # print("MKC")
        print("Inside parse_results()")
        output = parse_results(input_string)
        # print(output)

    # print("MKC1")
    output = update_results(input_string)
    # print(output)

    print(output)
    return output


# user_input = input("")
# output = searchingwebinput(user_input)
