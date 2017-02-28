from parse import parse_stations, parse_agencies, parse_routes, parse_shapes, parse_stops, parse_stop_times, parse_trips

from sqlalchemy.orm import sessionmaker

from models import engine, Station, Route

Session = sessionmaker(bind=engine)

def load_stops():
    session = Session()

    stops = parse_stops()
    stations = []

    for stop in stops:
        if stop['parent'] == '':
            stations.append(Station(stop['sid'], stop['name'], stop['lat'], stop['lng']))


    session.add_all(stations)
    session.commit()


def load_routes():

    session = Session()

    routes = parse_routes()
    rx = []

    for r in routes:
        rx.append(Route(
                r['rid'],
                r['name'],
                r['description'],
                r['color']))

    session.add_all(rx)
    session.commit()

    
    
    
if __name__ == "__main__":
    load_stops()
    load_routes()
    import pdb; pdb.set_trace()
    x = 5
