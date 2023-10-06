#!/usr/bin/python3

import requests
import re
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

MAIN = "https://www.mixesdb.com"
SRCH = "/w/Category:"
ARTS = "Motor_City_Drum_Ensemble"
#ARTS = "Laurent_Garnier"


def extract_mixes_from_url(URL):
    
    response = requests.get(URL, verify=False, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all the anchor tags with URLs
    all_links = soup.find_all('a', href=True)

    # Regular expression pattern to match YYYY-MM-DD or YYYY-MM date format in URLs
    date_pattern = re.compile(r'(\d{4}-\d{2}-\d{2}|\d{4}-\d{2})')

    # Filter the links to get the ones that have the date pattern and are likely to represent mixes
    # and exclude links pointing to images
    mixes_urls = [link['href'] for link in all_links if date_pattern.search(link['href']) and not link['href'].startswith('/w/File:')]

    return mixes_urls

def extract_tracks_from_url(URL):
    response = requests.get(URL, verify=False, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div with class 'mw-body-content'
    mw_body_content_div = soup.find('div', class_='mw-body-content')
    
    # Check if mw_body_content_div exists and raise an error if not
    if mw_body_content_div is None:
        raise ValueError(f"Could not find <div class='mw-body-content'> in the content of URL: {URL}")

    # Find the ordered list (ol) within this div
    tracklist_ol = mw_body_content_div.find('ol')
    
    # Check if tracklist_ol exists and raise an error if not
    if tracklist_ol is None:
        all_li_elements = soup.find_all('li')
        
        # Extracting text from each li element
        li_texts = [li.get_text(strip=True) for li in all_li_elements]
        
        # Filtering out track-like patterns from the list items
        tracks = [li_text for li_text in li_texts if re.match(r'(\[\d{1,3}\]|\[\?\?\]).+', li_text)]
    else:   
        # Extract the tracks
        tracks = [li.get_text(strip=True) for li in tracklist_ol.find_all('li')]
 
    return tracks

def clean_track(track):
    gtrack=""
    dtrack={}
    if ('[' in track):
        if (']' in track):
            track = track.split(']')[1]
            if ("?" not in track and not track.isalpha()):
                gtrack = track
        
    else : gtrack = track
    dtrack={}
    try:
        dtrack["title"]=gtrack.split('-')[1]
        dtrack["artist"]=gtrack.split('-')[0]
        return dtrack
    except:
        pass
    


if __name__ == "__main__":
    ltrack=[]
    URLMIX = MAIN + SRCH + ARTS
    mixes = extract_mixes_from_url(URLMIX)

    URLTRACK = MAIN + mixes[5]
    print(URLTRACK)
    tracks = extract_tracks_from_url(URLTRACK)
    for track in tracks:
        t= clean_track(track)
        if t:
            ltrack.append(clean_track(track))
    print(ltrack)



        
        

