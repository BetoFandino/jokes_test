
import requests

import response_codes


def chuknorris_get(num_jokes):
    array_jokes = []
    list_jokes = []
    try:
        url = 'https://api.chucknorris.io/jokes/random'
        while len(list_jokes) < num_jokes:
            list_jokes.append(requests.get(url).json())
            for each in range(len(list_jokes)):
                if list_jokes[each] not in array_jokes:
                    array_jokes.append(list_jokes[each])
        return_code = response_codes.SUCCESS
        return return_code, array_jokes
    except Exception as ex:
        return_code = response_codes.UNEXPECTED_ERROR
    return return_code, array_jokes


def organize_list(list_joke):
    for each in range(len(list_joke)):
        [list_joke[each].pop(key) for key in ['categories', 'created_at', 'icon_url', 'updated_at']]
    return list_joke
