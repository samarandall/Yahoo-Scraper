import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict

league_number = 528 # change for different league

base_url = f'https://football.fantasysports.yahoo.com/f1/{league_number}/players?status=ALL' # will need to change since data is based on my league

#base_url = 'https://football.fantasysports.yahoo.com/f1/145337/players'

@dataclass
class Player:
    player: str
    position: str
    projected_pts: str

def get_qb():
    full_url = f'{base_url}&pos=QB&stat1=S_PS_2022&jsenabled=1' # projected season stats
    resp = httpx.get(full_url)
    html = HTMLParser(resp.text)
    #return HTMLParser(resp = httpx.get(f'{base_url}&pos=QB&stat1=S_PS_2022&jsenabled=1'))
    return html

def get_wr():
    full_url = f'{base_url}&pos=WR&stat1=S_PS_2022&jsenabled=1'
    resp = httpx.get(full_url)
    html = HTMLParser(resp.text)
    return html

def get_rb():
    full_url = f'{base_url}&pos=RB&stat1=S_PS_2022&jsenabled=1'
    resp = httpx.get(full_url)
    html = HTMLParser(resp.text)
    return html

def get_te():
    full_url = f'{base_url}&pos=TE&stat1=S_PS_2022&jsenabled=1'
    resp = httpx.get(full_url)
    html = HTMLParser(resp.text)
    return html

def get_pos(pos,page=0):
    full_url = f'{base_url}&pos={pos}&cut_type=9&stat1=S_S_2022&myteam=0&sort=PTS&sdir=1&count={page}'
    resp = httpx.get(full_url)
    html = HTMLParser(resp.text)
    return html

def parse(html,pos,player_count=25):
    player_name = html.css('div.ysf-player-name')
    player_projected_pts= html.css('span.Fw-b')
    player_table = zip(player_name,player_projected_pts)
    for player in player_table:
        new_player = Player(
            player=player[0].text(),
            position=pos,
            projected_pts=player[1].text()
        )
        print(new_player)

def main():
    qb_html = get_pos(pos='QB') #assume 18 QB's in 10 man
    parse(html=qb_html,pos='QB')

    wr_html_p1 = get_pos(pos='WR') #assume 50
    parse(html=wr_html_p1,pos='WR')
    wr_html_p2 = get_pos(pos='WR', page=25) #page = prev_page + 25, page 1 = 0. Yahoo displays 25 at a time, display starts at the count ie page=21 : [player 21, player 46]
    parse(html=wr_html_p2,pos='WR')
    
    rb_html_p1 = get_pos(pos='RB') #assume 32
    parse(html=rb_html_p1,pos='RB')
    rb_html_p2 = get_pos(pos='RB')
    parse(html=rb_html_p2,pos='RB')

    qb_html = get_pos(pos='TE') #assume 16
    parse(html=qb_html,pos='TE')

if __name__ == '__main__':
    main()
