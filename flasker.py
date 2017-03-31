from flask import Flask, render_template

app=Flask(__name__)
# instantiate object

@app.route('/') # instancing one page (homepage)
def home():
    return render_template("home.html")


@app.route('/about/') # instancing one page (homepage)
def about():
    return "About page is here." # output will be mapped to URL above


if __name__=="__main__":
    app.run(debug=True)
