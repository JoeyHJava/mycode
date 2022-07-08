#!/usr/bin/python3

from email import message
from glob import glob
import json
from flask import Flask, jsonify, make_response, render_template
from flask import redirect
from flask import url_for
from flask import request

#use html file, atleast try AND USE make_response

app = Flask(__name__)


### NOTE FROM CHAD: There is nothing wrong with the HTML

user = ""
users = []

moreJson =[ {
    "name": "Larry",
    "favorite color": "blue",
    'number': 1,
    'bag': ["balls", "rings", "rabbit"]
}]
@app.route("/readable")
def readable():
    return jsonify(moreJson)

# @app.route("/success")
# def success():
#     return f"That is correct!"

@app.route("/",methods=["POST", "GET"]) 
def start():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
     global users
     new_user = {}
     if request.form.get("pw") is None:
        return redirect("/")
     else:
        if request.method == "POST" and request.form.get("pw") != "":
            # if pwword is present add to 
            if request.form.get("pw") != "" :
                user = request.form.get("pw")
                new_user["name"] = request.form.get("nm")
                new_user["pw"] = request.form.get("pw")
                users.append(new_user)
            else:
                user = "default_user"

            resp = make_response(render_template("index.html", message="Cookies were created"))
            # setting cookie
            resp.set_cookie("your_cookie", user)
            return resp
        else:
            return redirect("/")
            
@app.route("/body", methods=[ "GET"])
def posted():
    # getting cookie 
    if request.cookies.get("your_cookie")!= "":

        return render_template("cookie.html", users=users)
    else:
        return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)