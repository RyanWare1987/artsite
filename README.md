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


### Site Breakdown

#### Home Page

This simple landing page features an introductory pre-selection of pictures thanks to the Bootstrap Carousel. The carousel will automatically phase between the pre-selected images but the option for the user to browse through the Carousel remains.

#### About Page

The About Page features from information on myself, with the focus on the Artistic elements, such as Art Education and Art influences. This static page serves to display information a user may be interested in from an artist's perspective and contains social media links if a user is so inclined to add/follow my artist social media profiles to their network.
This page features a single static image and a Bootstap accordion panel group which contains all of the content provided for each header until one is clicked, thus revealing the content. I chose create this in order to keep content tidier and better presented.

#### Contact Us Page

The Contact Page features a simple submission form which is presented to the user, with the goal being for the user to contact me indirectly, submitting a message which will arrive via email to my inbox, processed and handled by SendGrid. The 'Name' and 'Email Address' are neccessary and therefore mandatory so I know who to reply to, but the 'Phone Number' is optional.

#### Products

These are the artwork I will have on sale as Products on this site. The data for these items exist in Heroku's Postgres DB with linkes to the Media which is stored in Amazon's AWS S3 Bucket. The Products Page populates from this data's location, where we see an Image, and breif detail of each Product. The user can then click into each Product, where a page will display containing more information about the selected product.
Within this page, a user is able to select an option to 'Add to Basket' and depending on the quantity selected, an amount of that particular product will be added to a user's basket.

Once a User has added a Product to their Basket, you can then navigate to the Basket page, which will show back to a user the contents of the basket (At this time, this feature doesn't display back the required information)

From within the Basket Page, we can then click 'Checkout' which will load two forms for the user, one to enter Payment Address and one to enter Card Details. The fields for the Card Data is handled by Stripe, and not stored in our Database.

The 'Basket' application and 'Checkout' integration with the existing 'Artwork' application has been forked from the work of Neil Mcewan, one of the Code Institute mentors. This was suggested by my own personal Code Institute mentor, Yoni Lavi, after my own implementation was failing and I needed to implement something that had proven functionality with the time I had remaining.

- It should be noted that in Order for a User to view Basket, they must be Signed In. This is due to the Purchasing process requiring the user's Email Address in which they signed up with. This is what is sent to Stripe so it is essntial this field is populated and correct. 

#### Register / Sign In

User's of this site are given the opporunity to Register an Account, which will create them a user account. From here, a user can create a more personal profile, or even complete a Purchase from the Products page mentioned above. 
Currently, the only information required is a Username, Email Address and password which will need verification by entering twice.

Currently, there are not many benefits to a user signing up to this site, but there are plans and features in the future which will make having an account useful for social interaction on this site with other members.

#### Profile Page

A user is able to view their own Profile page, where each field is optional except the 'Name'. As I have mentioned in this ReadMe, there is more scope to incorporate the user's profile page with other social aspects of this site, but they will be future additions and I had to cut some incomplete features which will utilise the user's profile page.

At current, it is still possible however for a User who is Signed In, to view their own profile page. A user may then edit these fields and enter as much or as little as they like, and save the data. A User's Profile is linked to their User Account on a OneToOne scale.



### Testing

The majority of testing for this project was completed during development by constructing changes with the virtualenv active and the server running locally via the `python manage.py runserver` command. Manual Testing was used to test links, views, models and how they would link with each other, images, database population, styling, css and content.

During Deployment, Chris Zielinski of Code Institute tested the site's functionality when it was first deployed to Heroku. He found that the Navbar needed some adjustment for responsiveness, as at the time it did not reduce in size when reduced to that of a mobile screen. There was also an issue with the Stripe Functionality but this is now fixed.


## Known Bugs
At the Time of Deployment, the Basket & Checkout displays do not currently populate properly. This is potentially down to the path, but could be due to other reasons.

There seems to be minimal field checks and charachter limits applied to the PaymentForm which is presented to the user when entering credit card details when purchasing a product.

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