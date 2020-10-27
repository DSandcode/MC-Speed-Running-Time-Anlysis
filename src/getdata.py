import pandas as pd
import requests
from bs4 import BeautifulSoup
import io

urls = {
    "JMCSR_AnyGl_RS_1.16": "https://www.speedrun.com/ajax_leaderboard.php?variable3207=57574&variable19152=63015&variable19112=62876&variable19153=63017&variable19126=62927&variable39353=155578&variable39354=134299&variable39355=134302&variable19154=63019&variable22659=75556&variable33251=112570&variable38458=130683&variable43715=149839&variable43716=149841&variable44953=153992&game=mc&verified=1&category=7135&platform=&variable666=&variable667=&variable21271=&variable42617=&loadtimes=2&video=&obsolete=&date=",
    "JMCSR_AnyGl_RS_1.9-1.15": "https://www.speedrun.com/ajax_leaderboard.php?variable3207=57574&variable19152=63016&variable19112=62876&variable19153=63017&variable19126=62926&variable39353=134297&variable39354=134299&variable39355=134302&variable19154=63019&variable22659=129306&variable33251=152775&variable38458=130686&variable43715=149839&variable43716=149841&variable44953=153992&game=mc&verified=1&category=7135&platform=&variable666=&variable667=&variable21271=&variable42617=&loadtimes=2&video=&obsolete=&date=",
    "JMCSR_AnyGl_RS_p1.9": "https://www.speedrun.com/ajax_leaderboard.php?variable3207=57574&variable19152=63016&variable19112=62876&variable19153=63017&variable19126=62926&variable39353=134296&variable39354=134299&variable39355=134302&variable19154=63019&variable22659=129306&variable33251=152775&variable38458=130686&variable43715=149839&variable43716=149841&variable44953=153992&game=mc&verified=1&category=7135&platform=&variable666=&variable667=&variable21271=&variable42617=&loadtimes=2&video=&obsolete=&date=",
    "JMCSR_AnyGl_SS_1.9-1.15": "https://www.speedrun.com/ajax_leaderboard.php?variable3207=57574&variable19152=63015&variable19112=62875&variable19153=63017&variable19126=62927&variable39353=134297&variable39354=134299&variable39355=134302&variable19154=63019&variable22659=75556&variable33251=112570&variable38458=130683&variable43715=149839&variable43716=149841&variable44953=153992&game=mc&verified=1&category=7135&platform=&variable666=&variable667=&variable21271=&variable42617=&loadtimes=2&video=&obsolete=&date=",
    "JMCSR_AnyGl_SS_p1.9": "https://www.speedrun.com/ajax_leaderboard.php?variable3207=57574&variable19152=63015&variable19112=62875&variable19153=63017&variable19126=62927&variable39353=134296&variable39354=134299&variable39355=134302&variable19154=63019&variable22659=75556&variable33251=112570&variable38458=130683&variable43715=149839&variable43716=149841&variable44953=153992&game=mc&verified=1&category=7135&platform=&variable666=&variable667=&variable21271=&variable42617=&loadtimes=2&video=&obsolete=&date=",
    "JMCSR_Any_RS_1.9-": "https://www.speedrun.com/ajax_leaderboard.php?variable3207=57574&variable19152=63016&variable19112=62875&variable19153=63017&variable19126=62927&variable39353=134296&variable39354=134299&variable39355=134302&variable19154=63019&variable22659=75556&variable33251=112570&variable38458=130683&variable43715=149839&variable43716=149841&variable44953=153992&game=mc&verified=1&category=7133&platform=&variable666=&variable667=&variable21271=&variable42617=&loadtimes=2&video=&obsolete=&date=",
    "JMCSR_Any_RS_p1.9": "https://www.speedrun.com/ajax_leaderboard.php?variable3207=57574&variable19152=63016&variable19112=62875&variable19153=63017&variable19126=62927&variable39353=134296&variable39354=134298&variable39355=134302&variable19154=63019&variable22659=75556&variable33251=112570&variable38458=130683&variable43715=149839&variable43716=149841&variable44953=153992&game=mc&verified=1&category=7133&platform=&variable666=&variable667=&variable21271=&variable42617=&loadtimes=2&video=&obsolete=&date=",
    "JMCSR_Any_SS_1.9-": "https://www.speedrun.com/ajax_leaderboard.php?variable3207=57574&variable19152=63015&variable19112=62875&variable19153=63017&variable19126=62927&variable39353=134296&variable39354=134299&variable39355=134302&variable19154=63019&variable22659=75556&variable33251=112570&variable38458=130683&variable43715=149839&variable43716=149841&variable44953=153992&game=mc&verified=1&category=7133&platform=&variable666=&variable667=&variable21271=&variable42617=&loadtimes=2&video=&obsolete=&date=",
    "JMCSR_Any_SS_p1.9": "https://www.speedrun.com/ajax_leaderboard.php?variable3207=57574&variable19152=63015&variable19112=62875&variable19153=63017&variable19126=62927&variable39353=134296&variable39354=134298&variable39355=134302&variable19154=63019&variable22659=75556&variable33251=112570&variable38458=130683&variable43715=149839&variable43716=149841&variable44953=153992&game=mc&verified=1&category=7133&platform=&variable666=&variable667=&variable21271=&variable42617=&loadtimes=2&video=&obsolete=&date=",
}


def mcsr_csv_maker(url, key):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    leaderboard = soup.findAll("td")
    r_txt = "Rank,Player,Real time,In-game time,Time,Version,Difficulty,F3,Mods,Date,,"
    for it in leaderboard:
        r_txt += (
            it.text if it.text != "" else "" if "small" in it.attrs["class"] else "None"
        )
        r_txt += ","

    df = pd.read_csv(io.StringIO(r_txt.replace(",,", "\n")), sep=",")
    df.to_csv("./data/versions/{}.csv".format(key), index=False)


for key, url in urls.items():
    mcsr_csv_maker(url, key)
