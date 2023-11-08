# super-octo-waddle

> I have added 100 movies from `Open Movies Database (OMDB)` to my MongoDB Cluster
> `run.py` should run directly provided you have all the dependencies present in the *`requirements.txt`* file

`Movies are taken from the year 2014 - 2023`

## Steps to Add Data to Your MongoDB Client
1. Replace the `MONGO_DB_URI` with your URI (Current URI is my personal Mongo Cluster made using Atlas)
2. Run the `dataadder.py`
3. You should now have a Database with the name of `aadrila` and collection named `movies` with `**100 movies**`

## Steps to run the code
1. `pip install requirements.txt` (Creation of virtual environment was skipped, can be used if needed)
2. `python run.py`
3. You can follow the steps given on the `Command-Line Interface`
