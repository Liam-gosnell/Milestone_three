
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

![About wireframe](https://raw.githubusercontent.com/Liam-gosnell/Milestone_three/master/wireframes/milestone3.pdf "About wireframe")


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
I used Python to programe how this would search the database. <p>

#### Bootstrap and Materialize

<p>I used Bootstrap mainly for the padding for the website. 
I also used materialize for the forms and icons as we were shown in our tutorials. The cards were made by using a custom CSS grid 
to repeat the same 3 pattern over and over for addition of new movies.</p>


#### Register and Login using passlib.hash

<p>
I based my login and register around passlib.hash to create authentication for the site.
It works well with the site and was easy to implement.
</p>

#### Jinja Templating

<p>
I used Jinja templating to create a base.html page with navbar and footer that would
ensure a standardised aesthetic across the site. I also used the templating to print data from the database 
(i.e. within 'edit movie' the previous input is displayed in the form) and create if and for loops that continued to personalise the user's experience.
</p>



### Features for the Future

<p>It would be a goal of mine  to obtain mailing data from the user in order to have a mailing list with new and featured Movies.</p>

<p>It would be highly likely that pagination would be required as the database grows.</p>

<p>I would like to have the users be able to edit/delete/add for only their page</p>

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

* [JQuery](https://jquery.com/) - JavaScript library used to make custom-code for the site which allows for DOM manipulation
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

<p>I have tested the website on:</p>

* Google Chrome
* Apple Safari
* Internet Explorer
* Mozilla Firefox

<h4>Devices</h4>

* Iphone X
* Iphone 8
* Iphone 6/7
* iPad 
* iPad Pro
* Pixel
* Pixel 2XL
* Galaxy Note 3
* Kindle fire XDH
* Galaxy s5

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

<p>There was a security issue related to the app.py view where the database string was returned in the URL.
 This could enable users to find and access the database. I quickly fixed the URL parameter to be the user._id rather than users._id.</p>


# Deployment

### How to install CinematicBase

1. From your terminal enter git clone https://github.com/Liam-gosnell/Milestone_three to clone the project and download to your IDE

2. Set up your Virtual Environment Variables

* this can be done by creating folder named .venv to hold your variables and importing them into your app.py
* this can be done in your IDE bash terminal - e.g. cd .. to your root directory and type nano.bashrc and type in your important environment variables

3. You should now install the requirements by typing $ pip3 -r install requirements.txt

4. You will also have to create your own database to get full functionality from the project. MongoDB is free and easy to use.

* I created Three collections in my Database:
 1. Movies
 2. Users
 3. Categories


### How to Deploy your site

<p>I committed my code to GitHub at regular intervals. I am now using git more often, making sure to give detailed commit messages as I know it provides version control.</p>

1. In order to deploy the site to Heroku, you must create a Procfile and requirements.txt. These will tell Heroku how to run your app.

* To create a Procfile - echo web: python (your filename).py > Procfile
* To create a requirements.txt - pip3 freeze --local > requirements.txt

2. Next, log into Heroku and set up the remote.
 * heroku login
 * then enter details

3. You then need to setup your Heroku Enivronment Variables and you can do this in two ways, either through the terminal or by navigating to Heroku.

4. On navigating to the Heroku website, log in and select your app from the dashoboard.

5. Choose settings and click on 'Reveal Config Vars' and insert the environment variables that are essential for your project to run. For example,
   "IP - 0.0.0.0 PORT - 8080 MONGO_URI - mongodb+srv://rootyour password@myfirstcluster-ug8tc.mongodb.net/your database?retryWrites=true DB_NAME - your database name SECRET KEY - create a secret key"

6. You should then send your committed code to Heroku using git push heroku master and view your deployed site on the URL provided within your Heroku dashboard.

### Differences between Development and Deployed version

<p>I set the debug to false for deployment.</p>


# Credits

### Content
<p>Information about the movies were taken from<a href="https://www.imdb.com/">IMBD</a></p>


### Media

<p>All photos in the background images are taken from <a href="https://unsplash.com/">Unsplash</a>, a stock image library.
The video on the about page was taken from <a href="https://coverr.co/search?q=movies">Coverr</a>, a video library. The movie images on the index page 
were taken from google images.
</p>

<p><a href="https://materializecss.com/">Materialize</a> - I used this to format the form elements and for icons.</p>


<p><a href="https://www.w3schools.com/">W3schools</a> - I used this to ensure I was entering all the information required correctly on my HTML 
and CSS and even for helping me with the functions on JavaScript.</p>

<p>The youtube trailers videos on the view movie
were taken from <a href="https://www.youtube.com/">Youtube</a>.</p>


### Acknowledgements

<p>I used Ian Lunn's Hover for my navbar link hover effects. I have clearly marked the borrowed code in my CSS.</p>

<p>I used <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Auto-placement_in_CSS_Grid_Layout">CSS grid </a> for the .wrapper layout for the movies on the index page. </p>

<p>Throughout this project I have sought support and guidance from Stack-Overflow, Code-Institue Slack Community, Tutors, W3Schools, CSS Tricks, YouTube videos.</p>


