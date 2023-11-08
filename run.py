from pymongo import MongoClient
import pandas as pd

# Basic Init Variables
MONGO_DB_URI = "mongodb+srv://root:di3duiETPM6DOE5l@iteam.gnwucnl.mongodb.net/iteam?retryWrites=true&w=majority"
client = MongoClient(MONGO_DB_URI)

my_database = client["aadrila"]
collection = my_database["movies"]
ch = -1

def search_movie(key, keyword, page_number):
    result = collection.find({key: {'$regex' : keyword , "$options" : 'i'}}).limit(10).skip((page_number-1) * 10)
    return list(result)

#.*{}.*'.format(keyword)

def show_dataframe(mongo_cursor):
    print(pd.DataFrame(mongo_cursor).dropna(axis="columns"))

def run_logic(key):
    page = 1
    keyword = input("Type in the keyword that you want to search... ")
    while page != 0:
        search_result = search_movie(key, keyword, page)
        if (len(search_result) == 0):
            print("No results to show")
            break
        else:
            show_dataframe(search_result)
        
        print("Showing page {}".format(page))
        
        temp = int(input("1 for next page and -1 for previous page and 0 for next operation "))
        if temp == 1:
            page = page + 1
        else:
            page = page - 1


while ch != 0:
    print("What would you like to do?")
    print("1. Search for Movies")
    print("2. Show Unique Genres")
    print("3. Search by Year")
    print("4. Search by Actor")
    print("5. Search by Director")
    print("0. EXIT")

    ch = int(input("Enter your choice "))

    if ch == 1:
        run_logic("Title")
    if ch == 2:
        show_dataframe(collection.distinct("Genre"))
    if ch == 3:
        run_logic("Year")
    if ch == 4:
        run_logic("Actors")
    if ch == 5:
        run_logic("Director")