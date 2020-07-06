from bs4 import BeautifulSoup
import requests
import re
import sys

def welcome_screen():
    print("")
    print("*" * 160)
    print(("*"*69)+"Welcome To Dog Scraper"+ ("*"*69))
    print("*" * 160)

def create_soup(state):
    print(f"Showing results for {state}")
    if(state == 'AUST & NZ'):
        url = f'https://www.dogzonline.com.au/breeds/puppies.asp'
    else:
        url = f'https://www.dogzonline.com.au/breeds/puppies.asp?state={state}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_state():
    states = {
        '1' : 'QLD',
        '2' : 'NSW',
        '3' : 'ACT',
        '4' : 'VIC',
        '5' : 'TAS',
        '6' : 'SA',
        '7' : 'WA',
        '8' : 'NT',
        '9' : 'NZ',
        '10' : 'AUST & NZ'
    }
    print("What state ?")
    for key,value in states.items(): 
        print(f"{key}. {value}")
    state = str(input())
    return states[state]
    
def get_breeds():
    breeds_arr = []
    print("How many breeds ?")
    num = int(input())
    for item in range(num):
        print("Type breed name ? ")
        breeds_arr.append(input())
    return breeds_arr

def get_number(string):
    try:
        return re.search(r"\(([^)]+)\)",string).group().replace(")", "").replace("(","")
    except AttributeError:
        return 0


def find_breed(breeds,soup):
    breeds_arr = []
    breeds_dict = {}
    for breed in breeds:
        el = soup.find("a",string=breed, href=True)
        url = f"https://www.dogzonline.com.au{el.get('href')}"
        breeds_dict['breed'] = breed
        breeds_dict['num'] = get_number(str(el.find_parent('li')))
        breeds_dict['url'] = url
        breeds_arr.append(breeds_dict.copy())
    return breeds_arr

def print_dog_info(breeds):
    print(breeds)
    for item in breeds:
        print(f"{item.get('breed')} has {item.get('num')} listings.")
        print(item.get('url'))
        print("")

def main():
    welcome_screen()
    state = get_state()
    arr = get_breeds()
    soup = create_soup(state)
    breeds_dict = find_breed(arr,soup)
    print_dog_info(breeds_dict)

main()

