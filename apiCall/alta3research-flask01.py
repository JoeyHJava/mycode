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


students = [{
    "name": "one",
    "pass": 21
}]
user = "d"
@app.route("/success")
def success():
    return f"That is correct!"

@app.route("/",methods=["POST", "GET"]) 
def start():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
     global user
     new_user = {}
     if request.form.get("pass") == "":
        return redirect("/")
     else:
        if request.method == "POST":
            # only checking if password is present
            if request.form.get("pass") is not None :
                user = request.form.get("pass")
                new_user["name"] = request.form.get("nm")
                new_user["pass"] = request.form.get("pass")
                students.append(new_user)
            else:
                user = "default_user"

        resp = make_response(render_template("index.html"))
        # setting cookie
        resp.set_cookie("your_cookie", user)
        return resp

@app.route("/body", methods=[ "GET"])
def posted():
    # getting cookie 
    if request.cookies.get("your_cookie")!= "":
        return jsonify(students)
    else:
        return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)