import csv
from flask import Flask, jsonify, request, render_template

app = Flask( __name__ )
 
 
@app.route( "/", methods = [ "POST", "GET" ] )

def index():
    if request.method == "POST":
        try:
            xValue = int(request.form.get( "clickedX"))
            yValue = int(request.form.get( "clickedY"))
        except:
            raise Exception("Invalid form data.")

        containsPoint = 0;
        checkedX = xValue + 1;
        checkedY = yValue -1;
        if checkedX <= 10 and checkedY > 0:
            containsPoint = 1;


        print(xValue, yValue);

        return jsonify( contains = containsPoint,
                        postX = checkedX,
                        postY = checkedY
                        )
    else:
        return render_template("index.html")
 
 
if __name__ == "__main__":
    app.run(
        port = 7777,
        debug = True
    )