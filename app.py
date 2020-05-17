import os
from flask import Flask, render_template, redirect, session, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId




app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cinematic_base'
app.config["MONGO_URI"] = 'mongodb+srv://liam:liam_r00t@myfirstcluster-eu72b.mongodb.net/cinematic_base?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
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

@app.route('/view_movie')
def view_movie():
    return render_template('viewmovie.html',
                           movies=mongo.db.movies.find())




if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)