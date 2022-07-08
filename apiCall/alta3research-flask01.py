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
    "age": 21
}]
user = "d"
@app.route("/success")
def success():
    return f"That is correct!"

@app.route("/",methods=["POST", "GET"]) #index should check for cookies. If cookes present, just send all info, maybe increment, if not, login
def start():
    return render_template("login.html")




@app.route("/login", methods=["POST"])
def login():
     global user
     if request.method == "POST":
        if request.form.get("pass") is not None :
            user = request.form.get("pass")
        else:
            user = "default_user"

        resp = make_response(render_template("index.html"))
        resp.set_cookie("your_cookie", user)
        # return jsonify(students)
        return resp
        # return redirect(url_for("posted"))

@app.route("/body", methods=["POST", "GET"])
def posted():
    print("GLOBAAAA ", user)
    print("dfsd", request.cookies.get("your_cookie"))
    if request.cookies.get("your_cookie")!= "":
        students[0]['hasCookie'] =  request.cookies.get("your_cookie") != None
        print("SUTDENT: ", students)
        return jsonify(students)
    else:
        return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)