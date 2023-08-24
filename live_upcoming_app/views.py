from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from django.http.response import JsonResponse
import json, requests
from cleantext import clean
from rest_framework.response import Response
from urllib.request import urlopen
import re
import pandas as pd

@api_view(['GET'])
def InternationalEvent(request):
    st_r = requests.get("https://sports.ndtv.com/cricket/teams/6-india-teamprofile/schedules-fixtures")
    st_soup = BeautifulSoup(st_r.text, 'html.parser')
    st_headings1 = st_soup.findAll("div", {"class":"scr_txt-ony"})

    dates_event = []

    for sth in st_headings1:
        dates_event.append(sth.text)
        
    st_headings2 = st_soup.findAll("div",{'class':'scr_dt-red'})
    date1 = []
    for sth in st_headings2:
        date1.append(sth.text)

    st_headings3 = st_soup.findAll("div",{'class':'scr_tm-wrp'})
    date = []
    for sth in st_headings3:
        date.append(sth.text)

        dic={'date_venue_event':dates_event,'team':date,'time':date1}

    return JsonResponse({'dict':dic}, safe=False) 


@api_view(['GET'])
def live_international(request):
    st_r = requests.get("https://www.icc-cricket.com/live-cricket/mens-results")
    st_soup = BeautifulSoup(st_r.text, 'html.parser')

    st_headings1 = st_soup.findAll("div",{'class':'match-block__summary'})
    overview = []
    for sth in st_headings1:
        overview.append(sth.text)
    cleaned_data1 = [item for item in overview if item.strip()]

    st_headings2 = st_soup.findAll("div",{'class':'match-block__team-content'})
    Teams_and_runs = []
    for sth in st_headings2:
        Teams_and_runs.append(sth.text)
    cleaned_data = [item.replace('\n', '').strip() for item in Teams_and_runs if item.strip()]
    cleaned_data2 = [re.sub(r'\s+', ' ', item.strip()) for item in cleaned_data]

    st_headings3 = st_soup.findAll("div",{'class':'match-block__result'})
    date1 = []
    for sth in st_headings3:
        date1.append(sth.text)

    st_headings4 = st_soup.findAll("div",{'class':'match-block__meta-container-content'})
    date = []
    for sth in st_headings4:
        date.append(sth.text)

    # i_tags = st_soup.find_all("i")
    # flag_links_list = []
    # for i_tag in i_tags:
    #     img_tag = i_tag.find("img")
    #     if img_tag:
    #         flag_link = img_tag.get("src")
    #         if flag_link:
    #             full_flag_link = "https://www.mykhel.com" + flag_link
    #             flag_links_list.append(full_flag_link)


    diction={
        'date':date,
        'overview':cleaned_data1,
        'teams&run':cleaned_data2,
        'result':date1,
    }

    return JsonResponse({'live':diction},safe=False)
    


@api_view(['GET'])
def NewsView6(request):

    url = "https://www.crictracker.com/icc-rankings/batting-test/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)


@api_view(['GET'])
def NewsView7(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/batting-odi/")
  
    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)



@api_view(['GET'])
def NewsView8(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/batting-t20i/")
    
    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)



@api_view(['GET'])
def NewsView9(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/bowling-test/")
  
    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)



@api_view(['GET'])
def NewsView10(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/bowling-odi/")

    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)



@api_view(['GET'])
def NewsView11(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/bowling-t20i/")
   
    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)


#allrounders

@api_view(['GET'])
def NewsView12(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/all-rounder-test/")
   
    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)


@api_view(['GET'])
def NewsView13(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/all-rounder-odi/")

    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)



@api_view(['GET'])
def NewsView14(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/all-rounder-t20i/")
   
    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)


#Women

@api_view(['GET'])
def WomenODIbat(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/women/batting-odi/")
    
    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)


@api_view(['GET'])
def WomenODIbowler(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/women/bowling-odi/")
  
    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)



@api_view(['GET'])
def WomenODIAllrounder(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/women/all-rounder-odi/")
    
    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)   


@api_view(['GET'])
def WomenT20Bat(request):

    response = requests.get("https://www.crictracker.com/icc-rankings/women/batting-t20i/")
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india": json_data}, safe=False)


@api_view(['GET'])
def WomenT20Bowler(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/women/bowling-t20i/")
    
    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)


@api_view(['GET'])
def WomenT20Allrounder(request):

    url = requests.get("https://www.crictracker.com/icc-rankings/women/all-rounder-t20i/")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', class_='numbered undefined undefined text-center font-semi text-nowrap table')

    data_list = []

    rows = table.find_all('tr')[1:]  # Exclude the header row

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player_rank = columns[0].get_text(strip=True)
            player_name = columns[1].get_text(strip=True)
            player_team = columns[2].get_text(strip=True)
            player_rating = columns[3].get_text(strip=True)
            
            player_data = {
                'Rank': player_rank,
                'Name': player_name,
                'Team': player_team,
                'Rating': player_rating
            }
            data_list.append(player_data)

    # Convert the data_list into JSON format
    json_data = json.dumps(data_list)
    return JsonResponse({"news from times of india":json_data}, safe=False)


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

def scrape_icc_rankings(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the page. Error code: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")

    headers = [th.text.strip() for th in table.find_all("th")]
    rows = []
    for tr in table.find_all("tr"):
        row = [td.text.strip() for td in tr.find_all(["td", "a"])]
        rows.append(row)

    data = [dict(zip(headers, row)) for row in rows[1:]]  # Skip the header row
    return data

@api_view(['GET'])
def MenTestTeams(request):
    url = "https://www.crictracker.com/icc-rankings/teams-test/"
    icc_rankings_data = scrape_icc_rankings(url)
    icc_rankings_json = json.dumps(icc_rankings_data, indent=4)

    return JsonResponse({'data': icc_rankings_json}, safe=False)


def scrape_icc_rankings(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the page. Error code: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")

    headers = [th.text.strip() for th in table.find_all("th")]
    rows = []
    for tr in table.find_all("tr"):
        row = [td.text.strip() for td in tr.find_all(["td", "a"])]
        rows.append(row)

    data = [dict(zip(headers, row)) for row in rows[1:]]  # Skip the header row
    return data

@api_view(['GET'])
def MenODITeams(request):
    url = "https://www.crictracker.com/icc-rankings/teams-odi/"
    icc_rankings_data = scrape_icc_rankings(url)
    icc_rankings_json = json.dumps(icc_rankings_data, indent=4)

    return Response(icc_rankings_json)


def scrape_icc_rankings(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the page. Error code: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")

    headers = [th.text.strip() for th in table.find_all("th")]
    rows = []
    for tr in table.find_all("tr"):
        row = [td.text.strip() for td in tr.find_all(["td", "a"])]
        rows.append(row)

    data = [dict(zip(headers, row)) for row in rows[1:]]  # Skip the header row
    return data

@api_view(['GET'])
def MenT20Teams(request):
    url = "https://www.crictracker.com/icc-rankings/teams-t20i/"
    icc_rankings_data = scrape_icc_rankings(url)
    icc_rankings_json = json.dumps(icc_rankings_data, indent=4)

    return Response(icc_rankings_json)


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


# @api_view(['GET'])
# def scorecard(request):
#     def get_data(url, api_keys):
#         headers = {
#             "X-RapidAPI-Key": api_keys[0],
#             "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
#         }
#         response = requests.get(url, headers=headers)
#         if response.status_code == 429: # Quota exceeded
#             api_keys.append(api_keys.pop(0)) # Cycle to next key
#             headers["X-RapidAPI-Key"] = api_keys[0]
#             response = requests.get(url, headers=headers)
#         return response.json()

#     api_keys = ["08341a5204mshbec004e335e3ed3p1ed96bjsn69e646d19029",
#                 "87ed0357acmsh559e7b0badab14fp1cd6aajsn0c83b2e243db"]
#     url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/40381/scard"

#     data = get_data(url, api_keys)

#     return Response(data)


@api_view(['GET'])
def scorecard(request):
    url = "https://www.icc-cricket.com/live-cricket/mens-results"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    match_buttons = soup.find_all("div", class_="match-block__buttons")

    match_center_links = []
    for match_button in match_buttons:
        link_element = match_button.find("a", class_="btn")
        if link_element and link_element.get("href"):
            match_center_links.append("https://www.icc-cricket.com" + link_element.get("href"))

    all_matches_data = []

    for link in match_center_links:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all scorecard tables on the page
        scorecard_tables = soup.find_all('table', {'class': 'table'})

        match_data = []

        # Iterate through each scorecard table
        for table in scorecard_tables:
            headers = [th.get_text(strip=True) for th in table.find_all('th')]

            rows = []
            for row in table.find_all('tr')[1:]:
                row_data = [td.get_text(strip=True, separator='\n') for td in row.find_all(['td', 'th'])]
                rows.append(row_data)

            df = pd.DataFrame(rows, columns=headers)

            # Convert DataFrame to JSON
            df_json = df.to_dict(orient='records')
            match_data.append(df_json)
        
        all_matches_data.append(match_data)

    return Response(all_matches_data)