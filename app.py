from flask import Flask,request,render_template

app=Flask(__name__)

@app.route("/geturl")
def index():
    name=request.args.get("t1")
    address=request.args.get("t2")
    return "<h1>The user {} and he stays in {}".format(name,address)

@app.route("/see")
def display():
    return render_template("home.html")

if __name__=='__main__':
    app.run()