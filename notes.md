# clock / plane monitor

## main idea:
### hardware clock
clock, no microcontrolers, **just** hardware like 555 timers, and an lcd - maybe the lcd needs an esp, but take inspo from fake bombs

### plane overhead monitor
use an api to make a lcd monior for what the plane nearest to a given gps point is, maybe find one??

## code stuf:

### hardware clock
hopefully n/a - but may need an esp-32 for the lcd

### plane monitor
- use an api for the nearest plane location, or list most interesting planes
- could be on a laptop, but displaying on an lcd would be cool
 - threading will be needed :(

#### api options:
- opensky REST api (for where planes are altitude, speed, direction, gps etc)
- aerodatabox (for flight timetables)
- flightradar24 api (paid for)

## hardware stuff

### clock
- model after movie tnt bomb props
- use 555 timers and maybe and esp with the lcd for the display

### plane monitor
- if using lcd, 3d printed case - if not just use a streamlit or html css js frontend on a website