import requests
import json


def checkModel(mark, usermodel):
    mark = mark.replace(" ", "")
    usermodel = usermodel.replace(" ", "")
    base_url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{}?format=json".format(mark.lower())
    response = requests.get(base_url)
    data_cars = response.text
    data = json.loads(data_cars)
    for model in data['Results']:
        model = model["Model_Name"].replace(" ", "")
        if model.lower() == usermodel.lower():
            return 1


def checkTitle(title):
    datamovie = []
    propertitle = title.replace(" ", "+")
    base_url = "https://www.omdbapi.com/?i=tt3896198&apikey=4a785286&t={})".format(propertitle)
    response = requests.get(base_url)
    data_movies = response.text
    data = json.loads(data_movies)
    datamovie.append(data['Title'])
    datamovie.append(data['Runtime'])
    datamovie.append(data['Poster'])

    print(datamovie[1])
    print(datamovie[2])

    return datamovie

checkTitle("James Bond")