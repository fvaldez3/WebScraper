from bs4 import BeautifulSoup
import requests

def main():
    headers = ["Rnd","Pick","Player","Pos","Age","College/Univ"]
    wantedPositions = ["QB","RB","WR","TE"]
    yearIndex = 2000
    finalYear = 2022

    while(yearIndex <= finalYear):
        htmlText = requests.get(f"https://www.pro-football-reference.com/years/{yearIndex}/draft.htm").text
        soup = BeautifulSoup(htmlText,"lxml")
        tableBody = soup.find("tbody")
        records = tableBody.find_all("tr", class_=False)
        with open(f"DraftsOffenseOnly/{yearIndex}.txt","w") as f:
            f.write("Player,Age,Position,Round,Pick,College\n")
            for record in records:
                pos = record.find("td", attrs={"data-stat": "pos"}).text
                if pos in wantedPositions:
                    draftRound = record.find("th").text
                    draftPick = record.find("td",attrs={"data-stat":"draft_pick"}).text
                    playerName = record.find("td",attrs={"data-stat":"player"}).text
                    age = record.find("td", attrs={"data-stat": "age"}).text
                    college = record.find("td", attrs={"data-stat": "college_id"}).text
                    f.write(f"{playerName},{age},{pos},{draftRound},{draftPick},{college}\n")
        print(f"Offensive Players from {yearIndex} ran successfully!")
        yearIndex = yearIndex + 1


   
    
   


if __name__ == "__main__":
    main()
