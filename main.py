import requests
from bs4 import BeautifulSoup

find_date = '01112564'

page = requests.get(f"https://news.sanook.com/lotto/check//{find_date}")  #https://news.sanook.com/lotto/check/01112564/
soup = BeautifulSoup(page.content, 'html.parser')


def first_reward():
    number = []
    s = soup.findAll('strong', {'class':'lotto__number'})
    for a in s:
        for b in a:
            number.append(b)
    
    reward = {
        'first_reward': number[0],
        'front_three': (number[1], number[2]),
        'last_three': (number[3],number[4]),
        'last_two': number[5],
        'close_reward': (number[6],number[7])
    }

    return reward


all_number = []
s = soup.findAll('span', {'class':'lotto__number'})
for a in s:
    for b in a:
        all_number.append(b)


def second_reward():

    second = []
    for a in range(0, 4):
        second.append(all_number[a])

    return second
    

def third_reward():
    third = []
    for b in range(5, 15):
        third.append(all_number[b])

    return third


def fourth_reward():
    fourth = []
    for c in range(15, 65):
        fourth.append(all_number[c])

    return fourth


def fifth_reward():
    fifth = []
    for d in range(65, 165):
        fifth.append(all_number[d])

    return fifth


lottery = {

    'first_reward': first_reward()['first_reward'],
    'front_three': first_reward()['front_three'],
    'last_three': first_reward()['last_three'],
    'last_two': first_reward()['last_two'],
    'close_reward': first_reward()['close_reward'],
    'second_reward': second_reward(),
    'third_reward': third_reward(),
    'fourth_reward': fourth_reward(),
    'fifth_reward': fifth_reward()
    
}
# print(lottery.values())