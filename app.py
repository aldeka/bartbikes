from flask import Flask
from flask import render_template

import os
import datetime
from pytz import timezone

app = Flask(__name__)

@app.route('/')
def index():
    # data = bart_schedule()
    # more_info = data['more_info'] if 'more_info' in data else None
    more_info = None
    # chart = data['chart'] if 'chart' in data else None
    chart = None
    return render_template('index.html', answer='<a href="http://www.sfbike.org/main/big-news-bart-votes-to-lift-bike-blackout-permanently/">YES, ALWAYS</a>', more_info=more_info, chart=chart)
    
@app.route('/testing/')
def testing():
    data = bart_schedule(datetime.datetime(year=2013, month=2, day=1, hour=8, minute=53))
    print "WHEEEEEE"
    print data
    try:
        more_info = data['more_info']
    except KeyError:
        more_info = None
    chart = data['chart'] if 'chart' in data else None
    return render_template('index.html', answer=data['answer'], more_info=more_info, chart=chart)
    
def bart_schedule(current_time=None):
    sf = timezone('America/Los_Angeles')
    current_sf_time = datetime.datetime.now(sf)
    if current_time:
        current_sf_time = current_time
    
    data = {'answer': "YES"}
    
    if current_sf_time.weekday() > 4:
        data['more_info'] = "WEEKEND, BABY"
        return data

    if current_sf_time >= datetime.datetime(year=2013, month=7, day=1, tzinfo=sf) and current_sf_time < datetime.datetime(year=2013, month=12, day=1, tzinfo=sf):
        if (current_sf_time.hour >= 7 and current_sf_time.hour < 9) or ( (current_sf_time.hour >= 16 and current_sf_time.minute >= 30) and (current_sf_time.hour < 18 and current_sf_time.minute < 30)):
            data['more_info'] = "But avoid the first three cars"
        return data

    # until the trial ends, the below is irrelevant
        
    if datetime.time(hour=7, minute=34) < current_sf_time.time() < datetime.time(hour=8, minute=2) or \
        datetime.time(hour=16, minute=59) < current_sf_time.time() < datetime.time(hour=18, minute=0):
        data['answer'] = "NO"
        data['more_info'] = 'Maybe you should get a <a target="_blank" href="http://www.amazon.com/gp/search/ref=as_li_qf_sp_sr_tl?ie=UTF8&camp=1789&creative=9325&index=aps&keywords=folding%20bike&linkCode=ur2&tag=littlegreenri-20">folding bike?</a><img src="https://www.assoc-amazon.com/e/ir?t=littlegreenri-20&l=ur2&o=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
        return data
    
    if datetime.time(hour=6, minute=17) < current_sf_time.time() < datetime.time(hour=9, minute=5) or \
        datetime.time(hour=16, minute=12) < current_sf_time.time() < datetime.time(hour=18, minute=59):
        data['answer'] = "MAYBE"
        data['more_info'] = "Depends where you are:"
        data['chart'] = {}
        data['chart']['yellow_line'] = {}
        data['chart']['blue_line'] = {}
        data['chart']['green_line'] = {}
        data['chart']['red_line'] = {}
        
        data = populate_chart(data, current_sf_time)
            
    return data
    
def populate_chart(data, current_sf_time):
    # initialize
    data['chart']['yellow_line']['west'] = "YES"
    data['chart']['yellow_line']['east'] = "YES"
    data['chart']['blue_line']['west'] = "YES"
    data['chart']['blue_line']['east'] = "YES"
    data['chart']['green_line']['west'] = "YES"
    data['chart']['green_line']['east'] = "YES"
    data['chart']['red_line']['west'] = "YES"
    data['chart']['red_line']['east'] = "YES"
    
    # yellow line morning data
    if datetime.time(hour=6, minute=17) < current_sf_time.time() < datetime.time(hour=8, minute=57):
        data['chart']['yellow_line']['west'] = "MAYBE"
    if datetime.time(hour=6, minute=54) < current_sf_time.time() < datetime.time(hour=8, minute=39):
        data['chart']['yellow_line']['east'] = "MAYBE"
        
    if datetime.time(hour=6, minute=47) < current_sf_time.time() < datetime.time(hour=8, minute=37):
        data['chart']['yellow_line']['west'] = "PROBLY NOT"
    if datetime.time(hour=7, minute=9) < current_sf_time.time() < datetime.time(hour=8, minute=24):
        data['chart']['yellow_line']['east'] = "PROBLY NOT"
        
    if datetime.time(hour=7, minute=12) < current_sf_time.time() < datetime.time(hour=8, minute=2):
        data['chart']['yellow_line']['west'] = "NO"
    if datetime.time(hour=7, minute=24) < current_sf_time.time() < datetime.time(hour=8, minute=9):
        data['chart']['yellow_line']['east'] = "NO"
        
    # yellow line evening data
    if datetime.time(hour=16, minute=24) < current_sf_time.time() < datetime.time(hour=18, minute=27):
        data['chart']['yellow_line']['west'] = "MAYBE"
    if datetime.time(hour=16, minute=21) < current_sf_time.time() < datetime.time(hour=18, minute=59):
        data['chart']['yellow_line']['east'] = "MAYBE"
        
    if datetime.time(hour=16, minute=33) < current_sf_time.time() < datetime.time(hour=18, minute=21):
        data['chart']['yellow_line']['west'] = "PROBLY NOT"
    if datetime.time(hour=16, minute=40) < current_sf_time.time() < datetime.time(hour=18, minute=40):
        data['chart']['yellow_line']['east'] = "PROBLY NOT"
        
    if datetime.time(hour=16, minute=42) < current_sf_time.time() < datetime.time(hour=18, minute=0):
        data['chart']['yellow_line']['west'] = "NO"
    if datetime.time(hour=16, minute=59) < current_sf_time.time() < datetime.time(hour=18, minute=21):
        data['chart']['yellow_line']['east'] = "NO"
        
    # blue line morning data
    if datetime.time(hour=6, minute=27) < current_sf_time.time() < datetime.time(hour=9, minute=1):
        data['chart']['blue_line']['west'] = "MAYBE"
    if datetime.time(hour=7, minute=6) < current_sf_time.time() < datetime.time(hour=8, minute=53):
        data['chart']['blue_line']['east'] = "MAYBE"
        
    if datetime.time(hour=6, minute=57) < current_sf_time.time() < datetime.time(hour=8, minute=40):
        data['chart']['blue_line']['west'] = "PROBLY NOT"
    if datetime.time(hour=7, minute=17) < current_sf_time.time() < datetime.time(hour=8, minute=45):
        data['chart']['blue_line']['east'] = "PROBLY NOT"
        
    if datetime.time(hour=7, minute=16) < current_sf_time.time() < datetime.time(hour=8, minute=25):
        data['chart']['blue_line']['west'] = "NO"
    if datetime.time(hour=7, minute=23) < current_sf_time.time() < datetime.time(hour=8, minute=36):
        data['chart']['blue_line']['east'] = "NO"
        
    # blue line evening data
    if datetime.time(hour=16, minute=12) < current_sf_time.time() < datetime.time(hour=18, minute=31):
        data['chart']['blue_line']['west'] = "MAYBE"
    if datetime.time(hour=16, minute=20) < current_sf_time.time() < datetime.time(hour=18, minute=47):
        data['chart']['blue_line']['east'] = "MAYBE"
        
    if datetime.time(hour=16, minute=20) < current_sf_time.time() < datetime.time(hour=18, minute=27):
        data['chart']['blue_line']['west'] = "PROBLY NOT"
    if datetime.time(hour=16, minute=35) < current_sf_time.time() < datetime.time(hour=18, minute=35):
        data['chart']['blue_line']['east'] = "PROBLY NOT"
        
    if datetime.time(hour=16, minute=31) < current_sf_time.time() < datetime.time(hour=18, minute=1):
        data['chart']['blue_line']['west'] = "NO"
    if datetime.time(hour=16, minute=47) < current_sf_time.time() < datetime.time(hour=18, minute=20):
        data['chart']['blue_line']['east'] = "NO"
        
    # green line morning data
    if datetime.time(hour=6, minute=36) < current_sf_time.time() < datetime.time(hour=8, minute=54):
        data['chart']['green_line']['west'] = "MAYBE"
    if datetime.time(hour=7, minute=13) < current_sf_time.time() < datetime.time(hour=9, minute=0):
        data['chart']['green_line']['east'] = "MAYBE"
        
    if datetime.time(hour=6, minute=54) < current_sf_time.time() < datetime.time(hour=8, minute=36):
        data['chart']['green_line']['west'] = "PROBLY NOT"
    if datetime.time(hour=7, minute=21) < current_sf_time.time() < datetime.time(hour=8, minute=51):
        data['chart']['green_line']['east'] = "PROBLY NOT"
        
    if datetime.time(hour=7, minute=24) < current_sf_time.time() < datetime.time(hour=8, minute=6):
        data['chart']['green_line']['west'] = "NO"
    if datetime.time(hour=7, minute=30) < current_sf_time.time() < datetime.time(hour=8, minute=43):
        data['chart']['green_line']['east'] = "NO"
        
    # green line evening data
    if datetime.time(hour=16, minute=21) < current_sf_time.time() < datetime.time(hour=18, minute=26):
        data['chart']['green_line']['west'] = "MAYBE"
    if datetime.time(hour=16, minute=27) < current_sf_time.time() < datetime.time(hour=18, minute=39):
        data['chart']['green_line']['east'] = "MAYBE"
        
    if datetime.time(hour=16, minute=30) < current_sf_time.time() < datetime.time(hour=18, minute=21):
        data['chart']['green_line']['west'] = "PROBLY NOT"
    if datetime.time(hour=16, minute=33) < current_sf_time.time() < datetime.time(hour=18, minute=28):
        data['chart']['green_line']['east'] = "PROBLY NOT"
        
    if datetime.time(hour=16, minute=39) < current_sf_time.time() < datetime.time(hour=18, minute=0):
        data['chart']['green_line']['west'] = "NO"
    if datetime.time(hour=16, minute=40) < current_sf_time.time() < datetime.time(hour=18, minute=16):
        data['chart']['green_line']['east'] = "NO"
        
    # red line morning data
    if datetime.time(hour=6, minute=42) < current_sf_time.time() < datetime.time(hour=9, minute=5):
        data['chart']['red_line']['west'] = "MAYBE"
    if datetime.time(hour=7, minute=3) < current_sf_time.time() < datetime.time(hour=9, minute=4):
        data['chart']['red_line']['east'] = "MAYBE"
        
    if datetime.time(hour=7, minute=0) < current_sf_time.time() < datetime.time(hour=8, minute=47):
        data['chart']['red_line']['west'] = "PROBLY NOT"
    if datetime.time(hour=7, minute=13) < current_sf_time.time() < datetime.time(hour=8, minute=50):
        data['chart']['red_line']['east'] = "PROBLY NOT"
        
    if datetime.time(hour=7, minute=20) < current_sf_time.time() < datetime.time(hour=8, minute=27):
        data['chart']['red_line']['west'] = "NO"
    if datetime.time(hour=7, minute=23) < current_sf_time.time() < datetime.time(hour=8, minute=36):
        data['chart']['red_line']['east'] = "NO"
        
    # red line evening data
    if datetime.time(hour=16, minute=17) < current_sf_time.time() < datetime.time(hour=18, minute=22):
        data['chart']['red_line']['west'] = "MAYBE"
    if datetime.time(hour=16, minute=16) < current_sf_time.time() < datetime.time(hour=18, minute=40):
        data['chart']['red_line']['east'] = "MAYBE"
        
    if datetime.time(hour=16, minute=25) < current_sf_time.time() < datetime.time(hour=18, minute=17):
        data['chart']['red_line']['west'] = "PROBLY NOT"
    if datetime.time(hour=16, minute=27) < current_sf_time.time() < datetime.time(hour=18, minute=28):
        data['chart']['red_line']['east'] = "PROBLY NOT"
        
    if datetime.time(hour=16, minute=35) < current_sf_time.time() < datetime.time(hour=18, minute=1):
        data['chart']['red_line']['west'] = "NO"
    if datetime.time(hour=16, minute=40) < current_sf_time.time() < datetime.time(hour=18, minute=16):
        data['chart']['red_line']['east'] = "NO"
        
    return data

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
