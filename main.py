from flask import Flask, render_template
import requests, datetime, json


app = Flask(__name__)

@app.route('/')
def home():
    
    # blog_url = "https://api.npoint.io/ec033ad7c14afde7ce19"
    # response = requests.get(blog_url)
    # all_posts = response.json()
    #print(all_posts)


    current_year = datetime.datetime.now().year
    with open('blog.json') as json_file:
        posts = json.load(json_file)
        # Reverse the order of the posts
        posts.reverse()
    return render_template("index.html", posts=posts, current_year=current_year)



@app.route('/blog.html')
def blog():
    
    current_year = datetime.datetime.now().year
    with open('blog.json') as json_file:
        posts = json.load(json_file)
        # Reverse the order of the posts
        posts.reverse()
    return render_template("blog.html", posts=posts, current_year=current_year)


#num is sent from the home(index.html) route.
@app.route('/post/<int:num>')
def posting(num):
    # blog_url = "https://api.npoint.io/ec033ad7c14afde7ce19"
    # response = requests.get(blog_url)
    # all_posts = response.json()
    with open('blog.json') as json_file:
        posts = json.load(json_file)
    return render_template("post.html", posts=posts, blog_id=num)


@app.route('/about.html')
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run()
