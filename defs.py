import requests
from bs4 import BeautifulSoup
import time

def get_movie(row,a,b):  # https://stackoverflow.com/questions/41385708/multiprocessing-example-giving-attributeerror
    idx = row[0]
    movie_id = row[1][0]
    lang_id = row[1][1]
    print(f"{idx}. movie_id: {movie_id} lang_id: {lang_id}")
    search_string = f"https://www.cbfcindia.gov.in/main/search-result?movie_id={movie_id}&lang_id={lang_id}"
    response = requests.get(search_string)
    soup = BeautifulSoup(response.content)

    movie_details = [each.text for each in soup.find_all('td')[1:]]
    keys = ['Movie No.'] + movie_details[::2]
    values = [idx] + movie_details[1::2]
    movie_dict = dict(zip(keys, values))    
    return movie_dict