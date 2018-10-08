# Toy project to store yield_curve for personal use from website chinaBond
it's a toy project about downloading files from the website chinaBond to get the yield curve and store in the local mysql db.


# Processing Steps
1. Downloading data files year on year for the past years;
2. Formating data
3. Storing in bulk to mysql db;
4. Downloading data files day on day for the most recent year;
5. format processing to make them the same as the format in data files for past years;
6. Storing in bulk to mysql db;
7. Using crontab to trigger daily task;

# Major package tools
selenium

libreoffice

os.system, os.environ

crontab(not in python env)


