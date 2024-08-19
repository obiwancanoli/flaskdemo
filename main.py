from flask import Flask, render_template
import requests, datetime


app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    blog_url = "https://api.npoint.io/ec033ad7c14afde7ce19"
    response = requests.get(blog_url)
    all_posts = response.json()
    #print(all_posts)
    return render_template("index.html", posts=all_posts, year=current_year)
#num is sent from the home(index.html) route.
@app.route('/post/<int:num>')
def posting(num):
    blog_url = "https://api.npoint.io/ec033ad7c14afde7ce19"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("post.html", posts=all_posts, blog_id=num)



if __name__ == "__main__":
    app.run()
