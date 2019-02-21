import csv
from flask import Flask, jsonify, request, render_template

app = Flask( __name__ )
 
 
@app.route( "/", methods = [ "POST", "GET" ] )

def index():
    if request.method == "POST":
        xValue = request.form.get( "clickedX")
        yValue = request.form.get( "clickedY")

        containsPoint = 0;


        print("(" + xValue + " " + yValue + ")");

        return jsonify( contains = containsPoint,
                        postX = xValue + 1,
                        postY = yValue -1
                        )
    else:
        return render_template( "index.html")
 
 
if __name__ == "__main__":
    app.run(
        port = 7777,
        debug = True
    )