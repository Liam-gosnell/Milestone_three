import os
from flask import Flask, render_template, redirect, session, request, url_for, g, session, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from random import randint

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Anthony', password='password'))
users.append(User(id=2, username='Becca', password='secret'))
users.append(User(id=3, username='Carlos', password='somethingsimple'))

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyiknow'



app.config["MONGO_DBNAME"] = 'cinematic_base'
app.config["MONGO_URI"] = 'mongodb+srv://liam:liam_r00t@myfirstcluster-eu72b.mongodb.net/cinematic_base?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')


@app.route('/index')
def index():
    return render_template('index.html', 
                           movies=mongo.db.movies.find())


@app.route('/add_movie')
def add_movie():
    return render_template('addmovie.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_movie', methods=['POST'])
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
def delete_movie(movie_id):
    mongo.db.movies.remove({'_id': ObjectId(movie_id)})
    return redirect(url_for('index'))



@app.route('/favourites')
def favourites():
    return render_template('favourites.html')

@app.route('/add_favourite/<movie_id>', methods=['GET','POST'])
def add_favourite(movie_id):
    movies =  mongo.db.movies
    favourites.insert_one(request.form.to_dict())
    return redirect(url_for('favourites'))



if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
