from bs4 import BeautifulSoup
import requests
import re

def welcome_screen():
    print("")
    print("*" * 160)
    print(("*"*69)+"Welcome To Dog Scraper"+ ("*"*69))
    print("*" * 160)

def create_soup(state):
    print(state)
    response = requests.get(f'https://www.dogzonline.com.au/breeds/puppies.asp?state={state}')
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_state():
    print("What state ?")
    state = str(input())
    return state

def get_breeds():
    breeds_arr = []
    print("How many breeds ?")
    num = int(input())
    for item in range(num):
        print("Type breed name ? ")
        breeds_arr.append(input())
    return breeds_arr

def get_number(string):
    return re.search(r"\(([^)]+)\)",string).group().replace(")", "").replace("(","")


def find_breed(breeds,soup):
    breeds_dict = {}
    for breed in breeds:
        el = str(soup.find("a",string=breed).find_parent('li'))
        breeds_dict[breed] = get_number(el)
    return breeds_dict

def print_dog_info(breeds):
    for dog,num in breeds.items():
        print(f"{dog} has {num} listings.")

def main():
    welcome_screen()
    state = get_state()
    arr = get_breeds()
    soup = create_soup(state)
    breeds_dict = find_breed(arr,soup)
    print_dog_info(breeds_dict)

main()

