import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict

league_number = 528 # change for different league

url = f'https://football.fantasysports.yahoo.com/f1/{league_number}/players?&sort=AR&sdir=1&status=ALL' # will need to change since data is based on my league

base_url = 'https://football.fantasysports.yahoo.com/f1/145337/players'

@dataclass
class Player:
    player: str
    position: str
    projected_pts: str
    
def get_qb(base_url):
    full_url = f'{base_url}&pos=QB&stat1=S_PS_2022&jsenabled=1' # projected season stats
    resp = httpx.get(full_url)
    html = HTMLParser(resp.text)
    #return HTMLParser(resp = httpx.get(f'{base_url}&pos=QB&stat1=S_PS_2022&jsenabled=1'))
    return html
    
def get_wr(base_url):
    full_url = f'{base_url}&pos=WR&stat1=S_PS_2022&jsenabled=1'
    return

def get_rb(base_url):
    full_url = f'{base_url}&pos=RB&stat1=S_PS_2022&jsenabled=1'
    return

def get_te(base_url):
    full_url = f'{base_url}&pos=TE&stat1=S_PS_2022&jsenabled=1'
    return

def parse(html):
    player_table = html.css('div.ysf-player-name')
    player_table = html.css('a.Nowrap')
    for player in player_table:
        new_player = Player(
            player=player.css_first().text(),
            position="QB",
            projected_pts='1'
        )
        print(new_player)

def main():
    qb_html = get_qb(base_url=url)
    parse(qb_html)
    #print(qb_html.css_first('title').text())

if __name__ == '__main__':
    main()
