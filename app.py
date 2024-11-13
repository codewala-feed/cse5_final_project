from flask import Flask, render_template,request, redirect
from pymongo import MongoClient

app = Flask(__name__)
host = "ocdb.app"
port = 5050
database = "db_42xt2ftzx"
username = "user_42xt2ftzx"
password = "p42xt2ftzx"

connection_string = f"mongodb://{username}:{password}@{host}:{port}/{database}"
my_connection = MongoClient(connection_string)
my_db = my_connection[database]
callme = my_db["callme"]
students = my_db["students"]

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/admissions", methods=["GET"])
def admission():
    return render_template("admissions.html")

@app.route("/callme", methods=["POST", "GET"])
def callme_details():
    name = request.form["name"]
    email = request.form["email"]
    number = request.form["number"]
    course = request.form["course"]
    callme.insert_one({
        "name":name, "email":email, "number":number, "course":course
    })
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        _id = request.form["id"]
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        percentage = request.form["percentage"]
        rank = request.form["rank"]
        course = request.form["course"]
        address = request.form["address"]

        students.insert_one({
            "id":_id, "name":name, "email":email, 
            "phone":phone, "percentage":percentage, 
            "rank":rank, "course":course, "address":address
        })

        return redirect("/register")
    else:
        return render_template("register.html")

@app.route("/view", methods=["GET"])
def view():
    data = students.find()
    # print(list(data))
    return render_template("view.html", response = list(data))

@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
       _id = request.form["id"]
       new_field = request.form["new_field"]
       new_value = request.form["new_value"]
       print(_id, new_field, new_value)
       students.update_one(
           {"id":_id}, {"$set":{new_field:new_value}}
       )
       return redirect("/update")
    else:
        return render_template("update.html")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        _id = request.form["id"]
        students.delete_one({"id":_id})
        return redirect("/delete")
    else:
        return render_template("delete.html")

@app.route("/campus_tour", methods=["GET"])
def campus_tour():
    return render_template("campus_tour.html")

app.run(debug=True)