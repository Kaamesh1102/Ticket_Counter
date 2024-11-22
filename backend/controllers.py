# app routes
from flask import Flask,render_template,request,url_for,redirect
from .models import *
from flask import current_app as app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods = ["GET","POST"])
def signin():
    if request.method == "POST":
        uname = request.form.get("user_name")
        pwd = request.form.get("password")
        usr = User_Info.query.filter_by(email = uname,password = pwd).first()
        if usr and usr.role == 0 :
            return redirect(url_for("admin_dashboard",name = uname))
        elif usr and usr.role == 1 :
            return redirect(url_for("user_dashboard",name = uname))
        else:
            return render_template("login.html",msg = "Invalid user credentials")

    return render_template("login.html",msg = "")

@app.route("/register",methods = ["GET","POST"])
def signup():
    if request.method=="POST":
        uname=request.form.get("user_name")
        pwd=request.form.get("password") 
        # pd = encrypt(pwd)
        full_name=request.form.get("full_name")
        address=request.form.get("location")
        pin_code=request.form.get("pin_code")
        usr = User_Info.query.filter_by(email = uname).first()
        if usr:
            return render_template("signup.html",msg="Sorry, this mail already registered!!!")
        new_usr=User_Info(email=uname,password = pwd , full_name = full_name,address = address,pin_code = pin_code)
        db.session.add(new_usr)
        db.session.commit()
        return render_template("login.html",msg = "Registration Succesful, Login in now")
    return render_template("signup.html",msg = "")

#Common route for admin dashboard
@app.route("/admin/<name>")
def admin_dashboard(name):
    theatres=get_theatres()
    return render_template("admin_dashboard.html",name=name,theatres=theatres)


@app.route("/user/<name>")
def user_dashboard(name):
    return render_template("user_dashboard.html",name=name)


@app.route("/venue/<name>",methods=["POST","GET"])
def add_venue(name):
    if request.method=="POST":
        vname=request.form.get("name")
        location=request.form.get("location")
        pin_code=request.form.get("pin_code")
        capacity=request.form.get("capacity")
        new_theatre=Theatre(name=vname,location=location,pin_code=pin_code,capacity=capacity)
        db.session.add(new_theatre)
        db.session.commit()
        return redirect(url_for("admin_dashboard",name=name))
    
    return render_template("add_venue.html",name=name)


#Other supported functions
def get_theatres():
    theatres=Theatre.query.all()
    return theatres