from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

import json
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as fo:
    all_data = json.load(fo)

all_earthquakes = all_data['features']

mags, longs, lats, hover_texts = [], [], [], []
for eq_dict in all_earthquakes:
    mag = eq_dict['properties']['mag']
    long = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    longs.append(long)
    lats.append(lat)
    hover_texts.append(title)

# Setup map

# Two different ways to set the data
# data = [Scattergeo(lon=longs, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]

layout = Layout(title='Global Earchquakes')

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='global_earhquakes.html')
