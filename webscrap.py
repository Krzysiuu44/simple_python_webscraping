from bs4 import BeautifulSoup

with open("https://sklepy.bikeworld.pl/sklepy/rowerowy", 'r') as f:
    doc = BeautifulSoup(f)