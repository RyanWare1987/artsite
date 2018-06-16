# Artsite
Artsite is a Python Django website. This serves as a personal website showcasing artwork which can be sold through the site. There is scope to add social features to the website in the future.
## Getting Started
These instructions will get the site running locally on your machine for development and testing purposes. See deployment notes for how to access the live deployed site

### Prerequisites
You will need the following installed on your local machine to run this locally:
- Python (Minimum version 2.7.14)
- Django (version 1.11.7)
- Pip 

#### Installing Locally
Once you have the above two packages installed and the project pulled down from git, you will need to do the following:
- Create a new virtual environment
- CD into the virtual environment, then activate it with `Scripts\activate`
- CD back into the project directory
- Run `pip install -r requirements.txt`
- Run `python manage.py makemigrations` (This will trigger the creation of a dbsqlite3 file)
- Run `python manage.py migrate` (This will construct the schema using the models in the code)
- Run `python manage.py runserver` 

You should now be able to browse to this locally on `localhost:8000`

### Deployment

This application is currently deployed live on Heroku, using a Postgres Database and Amazon AWS S3 Bucket for Storage and backend files.

The Application can be viewed on Heroku here: https://artsite-ryanware.herokuapp.com/home


### Testing

The majority of testing for this project was completed during development by constructing changes with the virtualenv active and the server running locally via the `python manage.py runserver` command. Manual Testing was used to test links, views, models and how they would link with each other, images, database population, styling, css and content.

During Deployment, Chris Zielinski of Code Institute tested the site's functionality when it was first deployed to Heroku. He found that the Navbar needed some adjustment for responsiveness, as at the time it did not reduce in size when reduced to that of a mobile screen. There was also an issue with the Stripe Functionality but this is now fixed.


## Known Bugs
At the Time of Deployment, the Basket & Checkout displays do not currently populate properly. This is potentially down to the path, but could be due to other reasons.

## Improvements
I am currently in the process of improving visuals, such as page layouts, css and bootstrap components. This is purely down to personal preference and to make the site easier on the eye. 


## Future Version Features
There are ideas in the pipeline, some have been developed slightly but are absent from the code itself as it stands in the Repo. I would like to have users interacting with one another, possessing the ability to own their own Gallery, and upload their own art pictures into it.

These Galleries would be publically viewable, and registered users would be able to interact with these user-uploaded images by way of 'liking' and 'commenting' them. There is also potential to create a blog space, or even a forum space for these users to further enhance their interaction with other artists. Users would also be able to share their Art-focused social media pages and links via their public profile, as it would feature more prominently within these areas of the website.






## Built With
- Python Django Framework
- Microsoft VSCode
- Sublime Text
- Heroku (CLI & Website)
- Amazon AWS S3 (Bucket Storage)
- Postgres Database
- SendGrid Email Server
- Bootstrap

## Acknowledgements
- Yoni Lavi, Mentor
- Neil McEwen, Code Institute
- Chris Zielinski, Code Institute