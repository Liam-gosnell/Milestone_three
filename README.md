
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

#### Hero Video

<p>I set the body element a fixed background video on all devices as it creates a modern/ professional 
touch and adds credibility to the site. <p>

#### Search Box

<p>For good UX design I decided to have a minimal search interface on the index page. 
I used Python to programme how this would search the database. <p>

#### Bootstrap and Materialize

<p>I used Bootstrap mainly for the padding for the website. 
I also used materialize for the forms and icons as we were shown in our tutorials. The cards were made by using a custom CSS grid 
to repeat the same 3 pattern over and over for addition of new movies.</p>


#### Register and Login using 

<p>


</p>



### Features for the Future

<p>It would be a goal of mine  to obtain mailing data from the user in order to have a mailing list with new and featured Movies.</p>

<p>It would be highly likely that pagination would be required as the database grows.</p>

<p>It could be possible to allow users to comment on movies, creating more of a community ethos.</p>

<p>It would be another goal to integrate social media feeds (i.e. Facebook,Instagram) to provide more user content and community.</p>


# Technologies Used

##### Languages

* HTML - used for creating content and basic layout and validated with W3C
* CSS - used for customised styling and layout and validated with W3C
* JavaScript - used to provide interactivity and logic to the site
* Python - used to programme the site and interact between the database and the frontend

##### Frameworks

* Flask - A Python micro framework that includes Jinja Templating and Werzkeug debugger. Werzkeug also provided password hashing which would ensure users' passwords are encrypted before being stored in the database.
* Bootstrap - used for responsive layout, basic styling.
* Materialize - used for forms layout and icons

##### Tools

* [PyMongo](https://pymongo.readthedocs.io/en/stable/) - An API which provides tools for working with MongoDB in Python
* [MongoDB](https://account.mongodb.com/account/login?signedOut=true) - non-relational document style database used to store the movies and users for Cimeatic Base
* [W3C Validator](https://validator.w3.org/) - HTML Validator
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) -  CSS Validator
* [Python Validator](https://extendsclass.com/python-tester.html) - Python Validator
* [JSLINT](https://www.jslint.com/) - JS Validator
* [GITPOD](https://www.gitpod.io/) - this was the IDE where I developed and tested my application
* [GIT]- I pushed my files using Git, storing them in a repository on GitHub
* [HEROKU](https://dashboard.heroku.com/) -  I deployed my finished site through Heroku
* [Chrome developer tools](https://developers.google.com/web/tools/chrome-devtools/) - used to test and check my work throughout the development process


##### Liberaries

* [JQUERY]() - JavaScript library used to make custom-code for the site which allows for DOM manipulation
* [Material Icons](https://material.io/resources/icons/?style=baseline) - used for links and icons to make the site more appealing


# Testing

#### Manual and Automated Testing

<p>Manual testing was done for all CRUD operations from the database as well as for all links, 
buttons and forms in the site. I used Werkzeug Debugger throughout the development process to 
immediately flag errors when running my app.py file.</p>

<p>I created a test.py file that tested the connection to my database, 
ensuring data was inserted in a suitable manner and was returned to the console when requested.</p>

<p>Throughout the process I continually manually tested the frontend, 
by saving my work in Gitpod and running it in Google Chrome. 
I used Chrome Developer Tools to ensure that my site was responsive and 
functioned in all screen sizes and that my styling was applied appropriately throughout.</p>

<p>I had several users log in and out of the website searching, adding, editing and deleting (CRUD) the movies.</p>

#### Responsiveness

<p>I tested my project throughout development using 
Chrome Developer Tools to check the site was responsive.
 I continually made adjustments to my media-queries 
 in CSS to ensure it looked good at all screen-widths,
  I began to investigate a range of screen sizes and realised the best option was just to make it as responsive as I possibly could!</p>


#### Bugs

<p>There were several issues with my Python code, however,
 using the Werkzeug Debugger allowed for an immediate fix.
  I used the documentation for Flask, PyMongo and MongoDB to help solve any problems.
   I found it very difficult to get a search function that would search the movie name. 
   I eventually had code that would work in every instance although I am aware that it could be done more efficiently.</p>

<p>There is also an issue with duplicate movies not showing up, this is because I currently have each movie set as a 
key in the database and therefore can't have duplicates. I will continue to look into this.</p>

<p>I had an issue with the users profile page when logging in. Once the user was logged , it would redirect to the users profile page that would display
the users name. But I had trouble getting the exact text template to make that possible. I had got errors saying that the user was undefined.</p>




