

from flask import Flask, render_template, redirect, url_for, request, jsonify, Response, flash, send_file

from flask.templating import TemplateNotFound




app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
#cache = Cache(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pope")
def pope():
    return render_template("pope.html")


@app.route("/subway")
def subway_index():
    #return render_template("subway/open.html")
    return render_template("subway/google.html")


@app.route("/subway/stations")
def subway_stations():
    from subway import parse
    return jsonify(stations=parse.parse_stops())



@app.route("/subway/routeshapes")
def subway_route_shapes():
    from subway import parse
    route_shapes = parse.parse_shapes()
    route_shapes = [e[1] for e in route_shapes] # Ignoring names for now for convenience.
    return jsonify(routeshapes=route_shapes)





if __name__ == "__main__":
    app.run(port=29992)
