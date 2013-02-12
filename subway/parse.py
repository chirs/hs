
import csv
import datetime
import os
from collections import defaultdict

DATA_DIR = "/home/chris/www/hs/subway/data"


def parse_stations():

    def process_item(l):
        division, line, station, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, ada, ada_notes, free_crossover, entrance_type, entry, exit_only, entrance_staffing, ns_street, ew_street, corner, lat, lng = l
        lat, lng = int(lat) / 1000000.0, int(lng) / 1000000.0
        routes = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11]
        routes = [e for e in routes if e]
        intersection = (ns_street, ew_street)

        return {
            'line': line,
            'station': station,
            'routes': routes,
            'intersection': intersection,
            'corner': corner,
            'lat': lat,
            'lng': lng,
            }

    f = open(os.path.join(DATA_DIR, "StationEntrances.csv"))
    r = csv.reader(f, delimiter=',')
    r.next() # Skip header.
    return [process_item(e) for e in r]



def parse_agencies():
    #agency_id,agency_name,agency_url,agency_timezone,agency_lang,agency_phone
    
    f = open('data/google/agency.txt')
    r = csv.reader(f, delimiter=',')
    r.next() # Skip header.

    aid, name, url, tz, lang, phone = r.next()

    return [{
            'aid': aid,
            'name': name,
            'url': url,
            'phone': phone,
            }]



def process_string_date(s):
    year = int(s[:4])
    month = int(s[4:6])
    day = int(s[6:8])
    return datetime.datetime(year, month, day)



def parse_routes():

    def process_item(l):
        rid, aid, route_short, route, description, rtype, url, color, text_color = l
        return {
            'rid': rid,
            'route': route,
            'description': description,
            'rtype': rtype,
            'url': url,
            'color': color,
            }

    f = open(os.path.join(DATA_DIR, "google/routes.txt"))
    r = csv.reader(f, delimiter=',')
    r.next() # Skip header.
    return [process_item(e) for e in r]



def parse_shapes():

    def process_item(l):
        sid, lat, lng, sequence, distance = l
        return {
            'sid': sid,
            'lat': lat,
            'lng': lng,
            'sequence': sequence,
            'distance': distance,
            }
    
    f = open(os.path.join(DATA_DIR, "google/shapes.txt"))
    r = csv.reader(f, delimiter=',')
    r.next() # Skip header.
    l = [process_item(e) for e in r]

    d = defaultdict(list)
    for shape_point in l:
        t = (shape_point['lat'], shape_point['lng']) # all items are in order, otherwise should order by sequence first...
        d[shape_point['sid']].append(t)

    print len(d.items())
    return d.items()



def parse_trips():

    def process_item(l):
        route_id, service_id, trip_id, trip_headsign, direction_id, block_id, shape_id = l
        return {
            'rid': route_id,
            'sid': service_id,
            'trip_id': trip_id,
            'direction_id': direction_id,
            'block_id': block_id,
            'shape_id': shape_id,
            }
    f = open(os.path.join(DATA_DIR, "google/trips.txt"))
    r = csv.reader(f, delimiter=',')
    r.next() # Skip header.
    return [process_item(e) for e in r]

    
    


def parse_service_calendar():

    def process_item(l):
        sid, m,t,w,th,f,sat,sun, start_date, end_date = l

        return {
            'sid': sid,
            'days': [bool(e) for e in (m,t,w,th,f,sat,sun)],
            'start_date': process_string_date(start_date),
            'end_date': process_string_date(end_date),

            }

    f = open(os.path.join(DATA_DIR, "google/calendar.txt"))
    r = csv.reader(f, delimiter=',')
    r.next() # Skip header.
    return [process_item(e) for e in r]

    

if __name__ == "__main__":
    print parse_shapes()

    #print parse_stations()

    #print parse_trips()
    #print parse_agencies()
    #print parse_routes()

    #print parse_service_calendar()
