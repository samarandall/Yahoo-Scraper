import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict

league_number = 528 # change for different league

base_url = f'https://football.fantasysports.yahoo.com/f1/{league_number}/players?&sort=AR&sdir=1&status=ALL' # will need to change since data is based on my league

#base_url = 'https://football.fantasysports.yahoo.com/f1/145337/players'

@dataclass
class Player:
    player: str
    position: str
    projected_pts: str

def get_pos(pos):
    full_url = f'{base_url}&pos={pos}&stat1=S_PS_2022&jsenabled=1'
    resp = httpx.get(full_url)
    html = HTMLParser(resp.text)
    return html

def parse(html,pos):
    player_name = html.css('div.ysf-player-name')
    player_projected_pts= html.css('span.Fw-b')
    player_table = zip(player_name,player_projected_pts)
    #print(player_projected_pts, player_name)
    for player in player_table:
        new_player = Player(
            player=player[0].text(),
            position=pos,
            projected_pts=player[1].text()
        )
        print(new_player)

def main():
    #qb_html = get_qb(base_url=url)
    qb_html = get_pos(pos='QB')
    parse(html=qb_html, pos='QB')
    #print(qb_html.css_first('title').text())

if __name__ == '__main__':
    main()
