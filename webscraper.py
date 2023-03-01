import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", {"class": "wikitable sortable"})
print(table)
rows = table.find_all("tr")

with open("states.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["State", "Population"])
    
    for row in rows[1:]:
        cells = row.find_all("td")
        if len(cells) >= 5:
            #print(f"cells is {cells}")
            state = cells[0].text.strip()
            population = cells[2].text.strip().replace(",", "")

            try:
                population = int(population)
            except ValueError:
                population = "N/A"
                
            writer.writerow([state, population])
