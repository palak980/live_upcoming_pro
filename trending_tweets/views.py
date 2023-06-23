import requests
from bs4 import BeautifulSoup
import csv
import random
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

user_agents_list = {
    "agent1": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    },
    "agent2": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    },
}


  
@api_view(["GET"])
def Tweets_news(request):

    url="https://tweethunter.io/trending/cricket"

            # getting list of keys
    agents_keys = list((user_agents_list.keys()))
    HEADERS = user_agents_list[random.choice(agents_keys)]

    webpage = requests.get(url, headers=HEADERS)
    job_soup = BeautifulSoup(webpage.content, 'html.parser')



        # response = requests.get(url)
        # soup = BeautifulSoup(response.content, "html.parser")

    find_name=job_soup.find_all("div", {"class": "css-1hxmsc9"})
    print(find_name)

    names = []

    for i in find_name:
        names.append(i.text)

    # Create your views here.

    return JsonResponse({'dic':names},safe=True)