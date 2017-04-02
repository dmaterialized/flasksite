from flask import Flask, render_template

app=Flask(__name__)
# instantiate object

@app.route('/') # instancing one page (homepage)
def home():
    return render_template("home.html")
# ^^ open home.html, then see that it extends layout.
# render home page.

@app.route('/about/') # instancing child page
def about():
    return render_template("about.html") # output will be mapped to URL above


if __name__=="__main__":
    app.run(debug=True)
