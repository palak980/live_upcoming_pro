from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from django.http.response import JsonResponse
import json, requests
from cleantext import clean
from rest_framework.response import Response
from urllib.request import urlopen

@api_view(['GET'])
def InternationalEvent(request):
    st_r = requests.get("https://www.mykhel.com/cricket/schedule/")
    st_soup = BeautifulSoup(st_r.text, 'html.parser')
    st_headings1 = st_soup.findAll("td", {"class":"os-textleft"})

    dates_event = []

    for sth in st_headings1:
        dates_event.append(sth.text)
        part1 = dates_event[0::3]

        # Extracting second part
        part2 = dates_event[1::3]

        # Extracting third part
        part3 = dates_event[2::3]

        dic={'date_time_event':part1,'team':part2,'venue':part3}

    return JsonResponse(dic, safe=False) 


@api_view(['GET'])
def live_international(request):
    htmldata = urlopen('https://www.espn.in/cricket/scores')
    soup = BeautifulSoup(htmldata, 'html.parser')
    overview= soup.find_all('div',{"class":"cscore_info-overview"})
    overview_list = []

    for sth in overview:
        overview_list.append(sth.text)

    header= soup.find_all('div',{"class":"scoreEvent__header"})
    header_list = []

    for sth in header:
        header_list.append(sth.text)

    teams= soup.find_all('div',{"class":"cscore_team icon-font-after"})
    teams_list = []

    for sth in teams:
        teams_list.append(sth.text)

    result= soup.find_all('span',{"class":"cscore_notes_game"})
    result_list = []

    for sth in result:
        result_list.append(sth.text)

    images = soup.find_all('div',{'class':'cscore_logo'})
    flag_urls = []
    for image in images:
        img_tag = image.find('img')
        if img_tag:
            flag_url = img_tag['data-src']
            flag_urls.append(flag_url)


    diction={
        'img':flag_urls,
        'overview':overview_list,
        # 'header':header_list,
        'teams&run':teams_list,
        'result':result_list,
        #'venue':venue_list,
    }

    return JsonResponse({'live':diction},safe=False)
    


@api_view(['GET'])
def NewsView6(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings9 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings9 = st_headings9[:10]

    st_news9 = []

    for sth in st_headings9:
        st_news9.append(sth.text)
        tit_list=(clean(text=st_news9,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list}, safe=False)


@api_view(['GET'])
def NewsView7(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings10 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings10 = st_headings10[10:20]

    st_news10 = []

    for sth in st_headings10:
        st_news10.append(sth.text)
        tit_list=(clean(text=st_news10,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list},safe=False)



@api_view(['GET'])
def NewsView8(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings11 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings11 = st_headings11[20:30]

    st_news11 = []

    for sth in st_headings11:
        st_news11.append(sth.text)
        tit_list=(clean(text=st_news11,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list},safe=False)



@api_view(['GET'])
def NewsView9(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/bowling")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings12 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings12 = st_headings12[:10]

    st_news12 = []

    for sth in st_headings12:
        st_news12.append(sth.text)
        tit_list=(clean(text=st_news12,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list},safe=False)



@api_view(['GET'])
def NewsView10(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/bowling")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings13 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings13 = st_headings13[10:20]

    st_news13 = []

    for sth in st_headings13:
        st_news13.append(sth.text)
        tit_list=(clean(text=st_news13,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list},safe=False)



@api_view(['GET'])
def NewsView11(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/bowling")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings14 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings14 = st_headings14[20:30]

    st_news14 = []

    for sth in st_headings14:
        st_news14.append(sth.text)
        tit_list=(clean(text=st_news14,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list},safe=False)


#allrounders

@api_view(['GET'])
def NewsView12(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/all-rounder")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings15 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings15 = st_headings15[:10]

    st_news15 = []

    for sth in st_headings15:
        st_news15.append(sth.text)
        tit_list=(clean(text=st_news15,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list},safe=False)


@api_view(['GET'])
def NewsView13(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/all-rounder")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings16 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings16 = st_headings16[10:20]

    st_news16 = []

    for sth in st_headings16:
        st_news16.append(sth.text)
        tit_list=(clean(text=st_news16,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list},safe=False)



@api_view(['GET'])
def NewsView14(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/all-rounder")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings17 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings17 = st_headings17[20:30]

    st_news17 = []

    for sth in st_headings17:
        st_news17.append(sth.text)
        tit_list=(clean(text=st_news17,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list},safe=False)


#Women

@api_view(['GET'])
def WomenODIbat(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/women/batting")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings21 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings21 = st_headings21[:10]

    st_news21 = []

    for sth in st_headings21:
        st_news21.append(sth.text)
        tit_list=(clean(text=st_news21,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse(
        {"news from times of india":tit_list},
        safe=False)


@api_view(['GET'])
def WomenODIbowler(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/women/bowling")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings22 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings22 = st_headings22[:10]

    st_news22 = []

    for sth in st_headings22:
        st_news22.append(sth.text)
        tit_list=(clean(text=st_news22,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list},safe=False)



@api_view(['GET'])
def WomenODIAllrounder(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/women/all-rounder")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings22 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings22 = st_headings22[:10]

    st_news22 = []

    for sth in st_headings22:
        st_news22.append(sth.text)
        
    return JsonResponse({"news from times of india":clean(text=st_news22,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                )},safe=False)    


@api_view(['GET'])
def WomenT20Bat(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/women/batting")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings22 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings22 = st_headings22[10:20]

    st_news22 = []

    for sth in st_headings22:
        st_news22.append(sth.text)
        tit_list=(clean(text=st_news22,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list},safe=False)


@api_view(['GET'])
def WomenT20Bowler(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/women/bowling")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings22 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings22 = st_headings22[10:20]

    st_news22 = []

    for sth in st_headings22:
        st_news22.append(sth.text)
        tit_list=(clean(text=st_news22,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list},safe=False)


@api_view(['GET'])
def WomenT20Allrounder(request):

    st_r = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/women/all-rounder")
    st_soup = BeautifulSoup(st_r.text, 'lxml')
    st_headings22 = st_soup.findAll("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})

    st_headings22 = st_headings22[10:20]

    st_news22 = []

    for sth in st_headings22:
        st_news22.append(sth.text)
        tit_list=(clean(text=st_news22,
                fix_unicode=True,
                to_ascii=True,
                lower=True,
                no_line_breaks=True,
                no_urls=False,
                no_emails=False,
                no_phone_numbers=False,
                no_numbers=False,
                no_digits=False,
                no_currency_symbols=False,
                no_punct=False,
                replace_with_punct="",
                replace_with_url="This is a URL",
                replace_with_email="Email",
                #replace_with_phone_number="",
                replace_with_number="123",
                replace_with_digit="0",
                replace_with_currency_symbol="$",
                lang="en"
                ))
        tit_list = tit_list.strip('[]').split(', ')
        tit_list = [d.strip("'") for d in tit_list]


    return JsonResponse({"news from times of india":tit_list},safe=False)


@api_view(['GET'])
def WomenT20Teams(request):

    st_r = requests.get("https://www.timesofsports.com/cricket/icc-rankings/womens-t20i-team/")
    st_soup = BeautifulSoup(st_r.text, 'html.parser')
    st_headings1 = st_soup.find("tbody")
    rows = st_headings1.find_all('tr')

    data = []
    for row in rows:
        cells = row.find_all('td')
        row_data = [cell.text for cell in cells]
        data.append(row_data)

    # Create a dictionary representing the table data
    table_data = {
        'data': data
    }


    # Print the JSON data
    return JsonResponse(table_data,safe=False)

@api_view(['GET'])
def WomenODITeams(request):

    st_r = requests.get("https://www.timesofsports.com/cricket/icc-rankings/womens-odi-team/")
    st_soup = BeautifulSoup(st_r.text, 'html.parser')
    st_headings1 = st_soup.find("tbody")
    rows = st_headings1.find_all('tr')

    data = []
    for row in rows:
        cells = row.find_all('td')
        row_data = [cell.text for cell in cells]
        data.append(row_data)

    # Create a dictionary representing the table data
    table_data = {
        'data': data
    }


    # Print the JSON data
    return JsonResponse(table_data,safe=False)


#MenTEamRanking

@api_view(['GET'])
def MenTestTeams(request):

    url = 'https://www.mykhel.com/cricket/icc-test-rankings/'
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the data
    table = soup.find('table')
    tbody = table.find('tbody')

    # Extract the table headers
    headers = [header.text for header in tbody.find_all('th')]

    # Extract the table rows
    rows = tbody.find_all('tr')
    data = []

    # Iterate over the rows and extract the values for each column
    for row in rows:
        values = [value.text for value in row.find_all('td')]
        data.append(dict(zip(headers, values)))

    # Convert the data to JSON format
    json_data = json.dumps(data, indent=4)


    return Response({"news from times of india":json_data})


@api_view(['GET'])
def MenODITeams(request):

    url = 'https://www.mykhel.com/cricket/icc-odi-rankings/'
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the data
    table = soup.find('table')
    tbody = table.find('tbody')

    # Extract the table headers
    headers = [header.text for header in tbody.find_all('th')]

    # Extract the table rows
    rows = tbody.find_all('tr')
    data = []

    # Iterate over the rows and extract the values for each column
    for row in rows:
        values = [value.text for value in row.find_all('td')]
        data.append(dict(zip(headers, values)))

    # Convert the data to JSON format
    json_data = json.dumps(data, indent=4)


    return JsonResponse({"news from times of india":json_data},safe=False)


@api_view(['GET'])
def MenT20Teams(request):

    url = 'https://www.mykhel.com/cricket/icc-t20-rankings/'
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the data
    table = soup.find('table')
    tbody = table.find('tbody')

    # Extract the table headers
    headers = [header.text for header in tbody.find_all('th')]

    # Extract the table rows
    rows = tbody.find_all('tr')
    data = []

    # Iterate over the rows and extract the values for each column
    for row in rows:
        values = [value.text for value in row.find_all('td')]
        data.append(dict(zip(headers, values)))

    # Convert the data to JSON format
    json_data = json.dumps(data, indent=4)


    return JsonResponse({"news from times of india":json_data},safe=False)


# @api_view(['GET'])
# def commentry(request):
#     url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/41881/comm"
#     headers = { "X-RapidAPI-Key": "08341a5204mshbec004e335e3ed3p1ed96bjsn69e646d19029", "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"} 
#     response = requests.request("GET", url, headers=headers)
#     data=response.text
#     parsed_data = json.loads(data)

#     return Response (parsed_data)



# @api_view(['GET'])
# def overs(request):
#     url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/41881/overs"
#     headers = { "X-RapidAPI-Key": "08341a5204mshbec004e335e3ed3p1ed96bjsn69e646d19029", "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"} 
#     response = requests.request("GET", url, headers=headers) 
#     data=response.text
#     parsed_data = json.loads(data)

#     return Response (parsed_data)


@api_view(['GET'])
def scorecard(request):
    def get_data(url, api_keys):
        headers = {
            "X-RapidAPI-Key": api_keys[0],
            "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 429: # Quota exceeded
            api_keys.append(api_keys.pop(0)) # Cycle to next key
            headers["X-RapidAPI-Key"] = api_keys[0]
            response = requests.get(url, headers=headers)
        return response.json()

    api_keys = ["08341a5204mshbec004e335e3ed3p1ed96bjsn69e646d19029",
                "87ed0357acmsh559e7b0badab14fp1cd6aajsn0c83b2e243db"]
    url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/40381/scard"

    data = get_data(url, api_keys)

    return Response(data)