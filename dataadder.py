from pymongo import MongoClient
import requests

MONGO_DB_URI = "mongodb+srv://root:di3duiETPM6DOE5l@iteam.gnwucnl.mongodb.net/iteam?retryWrites=true&w=majority"
client = MongoClient(MONGO_DB_URI)

my_database = client["aadrila"]
collection = my_database["movies"]

URL = "http://www.omdbapi.com/?apikey=288f0d3e&"

years = ["2014","2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
counter = 0

for letter in alphabets:
    for year in years:
        result = requests.get(URL + "y={}&t={}".format(year, letter))
        print("Adding data for..", URL + "y={}&t={}".format(year, letter))
        collection.insert_one(result.json())