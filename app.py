from functools import wraps
import os
from flask import Flask, render_template, redirect, session, request, url_for, g, session, abort, flash, Blueprint
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from random import randint
from functools import wraps
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256
import os
from os import path
if path.exists("env.py"):
    import env 

"""
app config
"""

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'cinematic_base'
app.config["MONGO_URI"] = 'mongodb+srv://liam:liam_r00t@myfirstcluster-eu72b.mongodb.net/cinematic_base?retryWrites=true&w=majority'
app.secret_key = "B,t=u0W};gBf{DnBClV8/BwiW[1k~7EEzoiv(1Ng'*1k!^R,4sd|4-[:8:_t4c8"
mongo = PyMongo(app)


def check_logged_in(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        if 'loggedin' in session:
            return(func(*args, **kwargs))
        else:
            return render_template('nologin.html')
    return wrapped_function

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/index')
def index():
    return render_template('index.html', 
                           movies=mongo.db.movies.find())


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method == "POST":
        username = request.form['userid']
        password = request.form['password']
        user_type = request.form['type']
        _hash = pbkdf2_sha256.hash(password)
        mongo.db.users.insert_one({
            'username': username,
            'password': _hash,
            'type': user_type
        })
        return redirect(url_for('login'))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form['userid']
        user = mongo.db.users.find_one({'username': username})
        user_password = user['password']
        form_password = request.form['password']
        if pbkdf2_sha256.verify(form_password, user_password):
            session['loggedin'] = True
            session['username'] = username
            session['userid'] = str(user['_id'])
            session['usertype'] = user['type']
            return render_template('profile.html')
        else:
            return render_template('loginerror.html')   
        

@app.route('/profile')
@check_logged_in
def profile():
    username = session['username']
    print("------------------------------------------", username)
    user = mongo.db.users.find_one({ 'username': username })
    print("------------------------------------------", username)
    return render_template('profile.html', user=user)
   

@app.route('/logout')
@check_logged_in
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('userid', None)
    session.pop('usertype', None)
    return redirect(url_for('login'))



@app.route('/add_movie')
@check_logged_in
def add_movie():
    return render_template('addmovie.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_movie', methods=['POST'])
@check_logged_in
def insert_movie():
    movies =  mongo.db.movies
    movies.insert_one(request.form.to_dict())
    return redirect(url_for('index'))


@app.route('/view_movie/<movie_id>')
def view_movie(movie_id):
    movie = mongo.db.movies.find_one({'_id': ObjectId(movie_id)})
    return render_template('viewmovie.html', movie=movie)

@app.route('/edit_movie/<movie_id>')

def edit_movie(movie_id):
    movie = mongo.db.movies.find_one({'_id': ObjectId(movie_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editmovie.html', movie=movie, categories=all_categories)

@app.route('/update_movie/<movie_id>', methods=['POST'])
def update_movie(movie_id):
    movie = mongo.db.movies
    movie.update( {'_id': ObjectId(movie_id)},
    {
        'movie_name':request.form.get('movie_name'),
        'movie_director':request.form.get('movie_director'),
        'movie_writer':request.form.get('movie_writer'),
        'movie_description': request.form.get('movie_description'),
        'category_name':request.form.get('category_name'),
        'movie_rating': request.form.get('movie_rating'),
        'movie_stars': request.form.get('movie_stars'),
        'movie_time': request.form.get('movie_time'),
        'img_url': request.form.get('img_url'),
        'movie_trailer': request.form.get('movie_trailer')

    })
    return redirect(url_for('index'))

@app.route('/delete_movie/<movie_id>')
@check_logged_in
def delete_movie(movie_id):
    mongo.db.movies.remove({'_id': ObjectId(movie_id)})
    return redirect(url_for('index'))

@app.route("/search_movie", methods=['POST'] )
def search_movie():
    search_term = request.form["movie_name"] 
    movie_name = search_term.title()
    results = mongo.db.movies.find_one({"movie_name": movie_name})
    return render_template('searchresult.html', results=results) 

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")
    


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
