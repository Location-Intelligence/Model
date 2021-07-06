from pyproj import Proj, transform
import json
import os
script_dir = os.path.dirname(__file__)

coord_filename = os.path.join(script_dir, '../SubCity-Coordinates.json')
coordinates = open(coord_filename,)

pop_filename = os.path.join(script_dir, '../SubCity-Populations.json')
populations = open(pop_filename,)

coord_data = json.load(coordinates)
pop_data = json.load(populations)

inProj = Proj(init='epsg:32637')
outProj = Proj(init='epsg:4326')

d = {}
for subcity in coord_data:
    d[subcity] = {
        'coordinates': [],
        'population': pop_data[subcity]
    }
    for x1, y1 in coord_data[subcity]['coordinates'][0]:
        x2,y2 = transform(inProj,outProj,x1,y1)
        d[subcity]['coordinates'].append([y2, x2])

with open(os.path.join(script_dir, '../Population_per_subcity.json'), 'w') as fp:
    json.dump(d, fp)