import urllib.parse
import folium
import pandas as pd
from numpy import nan

df=pd.read_excel('geocoded_libraries.xlsx')
map=folium.Map(location = [41.82875745,-72.55291695],zoom_start=10)
colors = [
    'red',
    'blue',
    'gray',
    'darkred',
    'lightred',
    'orange',
    'beige',
    'green',
    'darkgreen',
    'lightgreen',
    'darkblue',
    'lightblue',
    'purple',
    'darkpurple',
    'pink',
    'cadetblue',
    'lightgray',
    'black'
]
n=len(colors)
for ix,row in df.iterrows():
  grp_color=(row['Group']-1)%n
  icon=folium.Icon(color=colors[grp_color])
  tt=f"{row['Library']}. {row['Full Address']}<br>Group: {row['Group']}"
  for day in 'Mon','Tues','Fri','Sat','Sun','Note':
    hrs=row[day]
    if pd.notna(hrs):
      tt+=f'<br>{day}: {hrs}'
  full_address=row['Full Address']
  full_address2=urllib.parse.quote_plus(full_address)
  href=f"<a href=http://maps.apple.com?daddr={full_address2}>{full_address}</a>"
  marker=folium.Marker([row['latitude'],row['longitude']],
    tooltip=tt,popup=href,icon=icon)

  marker.add_to(map)
fn='docs/index.html'
map.save(fn)
print('saved to '+fn)