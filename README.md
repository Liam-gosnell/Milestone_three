
# Milestone-Three

# Cinematic BASE
<p>Stream Three Project: Data Centric Development - Code Institute<p>

<p> This is a web application that allows users to store and access Movies. 
There is a robust non-relational database schema hosted on MongoDB.
 A backend code that groups and summarises the movies on the site, 
 based on their attributes and a frontend page to show this summary.
  Using Python and Flask the backend code will retrieve a list of movies, descriptions,
  trailers and more.
   There is a detailed view for each movie, that would just show all attributes for that movie,
    and full information about that specific movie. Users can edit and delete their own movie records.
</p>

# Demo 

A live demo can be found [here]().

# UX
<hr>

### Strategy

#### The site should

* be visually appealing - using colours, styles and fonts which reflects the style of the brand
* provide quick access to the database of movies
* allow the user to search for movies by name
* allow users to add/delete and change movies in the database

<p>For the user the site should...<p>

* be intuitive and easy to use
* be personalised and welcoming
* provide quick access to movies with a very simple search function
* look appealing and in keeping with the brand
* ensure their data is secure
* allow them to manage their own movies

#### user stories

* As a non movie enthusiast..
  1. As a user, I want quick access to a variety of movies
  1. As a user, I want to be able to find movies that are rated well
  1. As a user, I want to be able to save the movies that I have enjoyed

* As a movie enthusiast...
  1. As a user, I want quick access to a variety of movies
  1. As a user, I want to see information about the movie (such as movie plot) at a glance
  1. As a user, I want to be able to share my knowledge by easily adding my own movies to the site
  1. As a user, I want to be able to manage my movies, editing them or deleting them as necessary
  1. As a user, I want to be able to save my favourite movies and access them quickly


### Scope

<p>In order to create a good UX Cinematic BASE..<p>

* be developed with a mobile-first approach in order to suit any movie enthusiast
* be responsive in order to display across a range of devices
* be intuitive and provide feedback to the user on their actions
* should feature a cohesive design which promotes the Cinematic BASE brand
* will have a simple search
* will be functional to any user, whether logged in or not

### Wireframes



# Features

### Existing Features

#### Navigation bar/ Side menu

<p>I used Materialize to create a minimalist navigation bar that would toggle a side menu on mobile/tablet devices. 
A user should not have to use the browser's back-button as the navigation bar is fixed.<p>

#### Hero Image

<p>I set the body element a fixed background image on all devices as it creates a modern/ professional 
touch and adds credibility to the site. <p>

#### Search Box

<p>For good UX design I decided to have a minimal search interface on the index page. 
I used Python to programme how this would search the database. <p>

#### css grid layout and cards

I used Bootstrap styling for my search results and user home pages to ensure that the pages 
would be as responsive as possible. I also used cards for a standard layout of recipes, 
this is visually effective because it porvides the necessary 'at-a-glance' details for the user. 
I also used "object-fit:cover" in CSS to try to ensure that each movie image would display nicely within the card.



