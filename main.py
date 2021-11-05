# HELLO ABU SIMPLE
from flask import Flask, render_template, request
from DB import dbFunktions
import requests

#apikey = ea929f344245355cfd475337fc8f93f4


# create flask object
app = Flask(__name__)

#create welcome page
@app.route('/')
def welcome():
    return render_template("welcome.html")


# create the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

# create the after sign up pages
@app.route('/loginAfterSign', methods=['GET', 'POST'])
def loginAfterSign():
    # take the info posted in the method post
     if request.method == 'POST':
            result = request.form
            #put infos in variables to check it
            userInput=result["unameUp"]
            passInput=result["pwordUp"]
            passInput1=result["pwordUp1"]
            # check if it is a user
            userOr = dbFunktions.userNameExist(**result)
            #if there is empty fields
            if userInput  == "" or passInput == "" or passInput1 =="":
                return render_template("error.html")
            #if password fields are not same
            elif passInput != passInput1:
                return render_template("samePass.html")
            #if not a user
            elif userOr == 0:
                # save in Database as new user
                dbFunktions.insert_rec(**result)
                return render_template("login.html")
            #if the user name is already used
            else:
                return render_template("alreadyExist.html")




# create the signup page
@app.route('/signup')
def signup():
    return render_template("signup.html")


# create the surprise page
@app.route('/surprise', methods=['GET', 'POST'])
def surprise():
    #take the info posted in the method post
    if request.method == 'POST':
        result = request.form
         #check if it is a user
        userOr = dbFunktions.usreOrNot(**result)
        #if not a user
        if userOr == 0:
            return render_template("error.html")
        #if a user
        else:
            # get info from the url
            # response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=london&units=metric&appid=ea929f344245355cfd475337fc8f93f4")
            response = requests.get(
                "https://newsapi.org/v2/everything?q=tesla&from=2021-09-28&sortBy=publishedAt&apiKey=73f6bd3be78e46bf98ec0f11f15717a7")
            # url=https://newsapi.org/
            # url = r"https://api.nytimes.com/svc/topstories/v2/world.json?"

            # params = {"api-key": "73f6bd3be78e46bf98ec0f11f15717a7"}
            # response = requests.get(url=url, params=params)
            response.status_code
            data = response.json()
            print(data)
            newsData = data["articles"]
            #for i in range(len(data["articles"])):
                #print(data["articles"][i]["title"])
                #print(data["articles"][i]["description"])
                #print(data["articles"][i]["url"])
                #print(data["articles"][i]["urlToImage"])

            print(data["main"]["temp"])
            # print(response.status_code)
            # print("here")
            return render_template("surprise.html", newsData=newsData)



# run the web application
if __name__ == "__main__":
    app.run()

