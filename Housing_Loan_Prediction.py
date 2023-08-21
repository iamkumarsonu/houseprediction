from flask import Flask, render_template,request

app = Flask(__name__,template_folder=r'D:\Regression Models\HousingLoan\templates')

@app.route("/")
def hello_world():
    return render_template("login.html")
@app.route("/login",methods=['POST'])
def login():
    request_data = request.form
    if request_data['username'] == 'preety' and request_data['password'] =='1234':
        return render_template("predictionPage.html")
    else:
        return render_template("login.html",error_message="Incorrect Password:- Please Enter Correct Password")       

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    
    