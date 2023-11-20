from flask import Flask, render_template, request, redirect
import requests
import json
import smtplib
import datetime
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy
def write(what):
    with open("post_data.json", "w") as file:
        json.dump(what, file, indent=4)

def date_fix(dateee):
    listtt=dateee.split("-")
    for lis in range(0,len(listtt)):
        listtt[lis]=int(listtt[lis])
    return listtt

data1={
    "Punjab":
        [
            {"User": "Karman", "Title": "Swatch bharat", "Desc": "we will clean india","Date":[2022,4,19]},
            {"User": "Rehet", "Title": "Swatch bharat 1", "Desc": "we will clean Bharat","Date":[2021,4,19]},
            {"User": "Anhad", "Title": "Swatch bharat 2", "Desc": "we will clean Hindustan","Date":[2021,4,19]}
        ]
}
data={}
olderPosts={}


def check_login(email):
    allTodo=Todo.query.all()
    for todos in allTodo:
        print(todos)
        print("Email",todos.email)
        data=[f"{todos.email}",f"{todos.fname}",f"{todos.lname}",f"{todos.password}",f"{todos.phone_number}",f"{todos.region}"]
        if data[0]==email:
            return True
    return False
def delete_post():
    def write(what):
        with open("post_data_older.json", "w") as file:
            json.dump(what, file, indent=4)

    records(True)
    global data1
    todays_date=date_fix(datetime.datetime.now().strftime("%Y-%m-%d"))
    for key, value in data1.items():
        for c in value:
            targetted_date = c["Date"]
            d1 = datetime.datetime(todays_date[0], todays_date[1], todays_date[2])
            d2 = datetime.datetime(targetted_date[0], targetted_date[1], targetted_date[2])
            if d1>d2:
                Iteration=True
                with open("records.txt","a") as rec:
                    rec.write(f"{c}`state->{key}\n")
                dict_old_data={}
                list_old_data=[]

                try:
                    with open("post_data_older.json","r") as data_file:
                        data5=json.load(data_file)
                        data4=data5
                except FileNotFoundError:
                    list_old_data.append(c)
                    dict_old_data[key]=list_old_data
                    write(dict_old_data)
                else:
                    try:
                        data4[key].append(c)
                    except KeyError:
                        data4[key] = []
                        data4[key].append(c)

                    data5.update(data4)
                    write(data5)
                print("Removing----->",c)
                value.remove(c)
    records(False)


def all_details_in_db(email,loc):
    allTodo=Todo.query.all()
    for todos in allTodo:
        data = [f"{todos.email}",f"{todos.fname}",f"{todos.lname}",f"{todos.password}",f"{todos.phone_number}",f"{todos.region}"]
        if data[0] == email:
            if loc:
                return data[5]
            else:
                return data



def records(first):
    global data,data1
    try:
        with open("post_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        write(data1)
        data=data1
    else:
        if first:
            data1=data
        else:
            data.update(data1)
            write(data)
def older_p():
    global olderPosts
    try:
        with open("post_data_older.json", "r") as data_file:
            data5 = json.load(data_file)
    except FileNotFoundError:
        data5 = {}
    # print("olderPosts=====", data5)
    olderPosts=data5
records(True)
def refresh():
    delete_post()
    older_p()

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = ""
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    email = db.Column(db.String(500), nullable=False, primary_key=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    region = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.email} ` {self.fname} ` {self.lname} ` {self.password} ` {self.phone_number} ` {self.region}"


OUR_EMAIL = "karman.test.smtp@gmail.com"
OUR_PASSWORD = "cxptcritxtpoxwav"


@app.route('/')
def get_all_posts():
    refresh()
    posts = []
    for key, value in data.items():
        for c in value:
            posts.append(c)
    return render_template("index.html", all_posts=posts,old=False,login=False,e_mail=None,state=None)

@app.route('/olderposts')
def show_old_posts():
    refresh()
    posts=[]
    for key,value in olderPosts.items():
        for c in value:
            posts.append(c)
    return render_template("index.html", all_posts=posts,old=True,login=False,e_mail=None,state=None)

@app.route("/<mail>/<state>")
def get_all_posts_state_wise(state,mail):
    refresh()
    try:
        listt=data[state.title().strip()]
    except:
        listt=[]
    return render_template("index.html", all_posts=listt,old=False,login=check_login(mail),e_mail=mail,state=state)

@app.route("/olderposts/<mail>/<state>")
def get_all_posts_state_wise_older(state):
    refresh()
    try:
        listt=olderPosts[state.title().strip()]
    except:
        listt=[]
    return render_template("index.html", all_posts=listt,old=True)

@app.route("/about")
def about():
    refresh()
    return render_template("about.html")

# @app.route("/login/<emailR>/<passR>",methods=["GET"])
# def success_or_not(emailR,passR):
#     EMAILr=emailR
#     PASSr=passR
#     print("EMAILr ",EMAILr,"PASSr ",PASSr)



@app.route("/login",methods=["GET","POST"])
def login():
    temp=0
    refresh()
    if request.method == "POST":
        try:
            data2=request.form
            EMAIL = data2["email"]
            PASSWORD_=data2["pass"]
            FNAME=data2["fname"].title().strip()
            LNAME=data2["lname"].title().strip()
            PHONE_NUMBER = data2["mobile"]
            REGION=data2["region"].title().strip()
            temp=1
            print(EMAIL,PASSWORD_,FNAME,LNAME,PHONE_NUMBER,REGION)
        except:
            data2 = request.form
            EMAIL = data2["emailR"]
            PASSWORD_ = data2["passR"]
            temp=2
            print(EMAIL, PASSWORD_)

        if temp==1:
            if check_login(EMAIL):
                return render_template('textss.html',Title="Already a user!",Subtitle="login as an existing user")
            else:
                todo=Todo(email=EMAIL,fname=FNAME,lname=LNAME,password=PASSWORD_,phone_number=PHONE_NUMBER,region=REGION)
                db.session.add(todo)
                db.session.commit()
                return render_template('textss.html', Title="Login Successful", Subtitle="Enjoy the website!")
        elif temp==2:
            if check_login(EMAIL):
                user_details_=all_details_in_db(EMAIL,False)
                user_details=user_details_[5]
                if user_details_[3]==PASSWORD_:
                    return redirect(f"/{EMAIL}/{user_details}")
                else:
                    return render_template('textss.html',Title="Wrong Password!",Subtitle="Try again")
            else:
                return render_template('textss.html',Title="Not a user!",Subtitle="login as a new user")
    return render_template("dog.html")



@app.route("/post", methods=["GET", "POST"])
def post():
    refresh()
    if request.method == "POST":
        data2=request.form
        NAME=data2["name"].title().strip()
        STATE=data2["State"].title().strip()
        DATE=date_fix(data2["Date"])
        TITLE=data2["Title"].title()
        DESCRIPTION=data2["description"]
        EMAIL=data2["email"]
        PHONE_NUMBER=data2["Phno"]
        LOCATION=data2["address"]
        try:
            data1[STATE].append({"User": NAME, "Title": TITLE, "Desc": DESCRIPTION,"Date":DATE,"Email":EMAIL,"Phone number":PHONE_NUMBER,"Location":LOCATION})
        except KeyError:
            data1[STATE] = []
            data1[STATE].append({"User": NAME, "Title": TITLE, "Desc": DESCRIPTION,"Date":DATE,"Email":EMAIL,"Phone number":PHONE_NUMBER,"Location":LOCATION})
        records(False)
        print(data)
        return render_template("upload_event.html", msg_sent=True)
    return render_template("upload_event.html", msg_sent=False)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)




def send_email(name,email, phone, message):
    smtp_add = "smtp.gmail.com"
    to_address = "karman.test.smtp@outlook.com"
    with smtplib.SMTP(smtp_add,port=587) as connection:
        connection.starttls()
        connection.login(user=OUR_EMAIL, password=OUR_PASSWORD)
        connection.sendmail(from_addr=email,
                            to_addrs=OUR_EMAIL,
                            msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}")




@app.route("/post/<index>",methods=["GET", "POST"])
def show_post(index):
    refresh()
    # print("Received index----->",index)
    requested_post = None
    for key_,value_ in data.items():
        for rat in value_:
            if rat['Desc'] == index:
                requested_post=rat
    if requested_post==None:
        for key_, value_ in olderPosts.items():
            for rat in value_:
                if rat['Desc'] == index:
                    requested_post = rat
    # for blog_post in posts:
    #     if blog_post["id"] == index:
    #         requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,host="172.17.141.231",port=2100)
