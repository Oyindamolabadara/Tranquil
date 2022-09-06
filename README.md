
# Tranquil Blog 

Tranquil Blog was created to increase awareness of mental health and seeking help. Because of misconceptions and stigma surrounding mental health issues, people often suffer in silence and don't seek treatment for their conditions. Raising community awareness of mental health issues helps eliminate the stigma and makes it easier for people to seek help. This platform aims to be a safe space where users can gain more information on mental health and share their personal experiences. 

[Here]() is a link to the live version of my project.

# Wireframes
![Home Page](media/images/home-page.png)
![Register Page](media/images/register-page.png)
![Login Page](media/images/login-page.png)
![Home Page - Loggedinuser](media/images/homepage-loggedinuser.png)
![Blogpost Content](media/images/blogpost-content.png)
![Update Post](media/images/update-post.png)
![Delete Post](media/images/delete-post.png)
![New Post](media/images/new-post.png)
![Profile Page](media/images/profile-page.png)


# Final design
![Final design]()

# User Experience
## User Stories
### Users
* As a Site User, I can view a paginated list of posts so that I can select one to read.
* As a Site User, I can see the date a post was made so that I can keep up with the latest posts.
* As a Site User, I can register an account so that I can manage my posts, comment and like.
* As a Site User, I can update and delete posts.
* As a Site User, I can like or unlike a post so that I can interact with the content.
* As a Site User, I can view and leave comments on a post so that I can be involved in the conversation.
* As a Site User, I can see my login status so that I know if I am logged in or not.
* As a Site User, I can find links to resources and helplines on every page. 

### Admin
* As an Admin, I can see the date a post was made so that I can keep up with the latest posts.
* As an Admin, I can filter, search and delete posts so that I can manage my website content.
* As an Admin, I can control what comments stay on posts so that I can filter out objectionable comments.

# Features
## Existing Features
* Navigation Links:
    *  The header contains the navigation links; Home, Login and Register for users who are not logged in. 
    * The navigation bar is featured on every page throughout the site to allow users easy access should they want to go to a different page.
    * The header also contains the logo of the website at the centre of the navigation bar, which redirects users to the home page when     clicked on. 
    * For logged-in users, the navigation links include; Home, New Post, Profile and Logout. 
    * On smaller screens, the logo is modified into a dropdown menu which provides users with the same navigation. 
* Register:
    * Featured on this page is a form for users to get registered on the blog app. 
    * After successful completion of the registration form, a success message appears telling users; “Your account has been created! You are now able to log in.”
* Log in:
    * Users can access their accounts via the login feature.
    * By logging in the users can publish and manage their blog posts (update and delete). They can also like and comment on others' posts.
    * The user is directed back to the home page once logged in.
    * If the user is not logged in, there is a message telling users; “You have been logged out”, with a link to direct users to log in again 
* New Post:
    * Featured here is a section allowing users to create and post new content. 
* Blog Posts:
    * Featured on the home page is access to blog posts.
    * The user can read the full post after clicking on the title. 
    * Featured at the top of the blog posts are the update and delete buttons.
    * To delete a post, the user is asked to confirm deleting the post.  
* Profile:
    * Featured on the profile page are the details of a logged-in user. 
* Side Bar:
    * The sidebar contains a Mental Health Crisis Helpline link. 
    * The sidebar also contains card boxes of different inspiring quotes on mental health.
    * The footer containing social media links is also featured in the sidebar. 
* Page Navigation
    * These are the next and previous buttons to enable users convenient flow from one page to another. 

## Features to implement in future
Due to time constraints, I was unable to achieve what I visualised for this project. I hope to implement the following features after the project has been graded:
* Make the site more visually appealing, paying more attention to the colour scheme, font and imagery. 
* Create an About Page. 
* Enable users to upload a profile picture and more details on the profile page.
* Enable users view their posts' status of approval so that I can manage my posts. 
* Enable users to create a draft and save it on their profile so they can go back to it at a later date.
* Enable images to be uploaded with a user's comment.
* Implement a search bar for posts.
* Allow users to connect by following and sending private messages. 
* Implement password reset features
* Improve side bar to change the quotes on each page. 

# Issues and Bugs
* When I tried to submit a comment on the blog post, I got an integrity error of null value in column "body" of relation "blog_comment" violates the not-null constraint. The tutor at CI explained to me that the error meant that the body cannot be empty and there must be a value. By default, unless it is specified with, null=True, blank=True, a data model will not allow an empty or null value when a record is created. I solved this by adding null=True, blank=True to the body field in the comment model and then re-run migrations. 
* Using django_summernote, the Html code was appearing in the content area of updating the blog post. This was solved by following the steps in [this Stack Overflow article](https://stackoverflow.com/questions/60578110/how-to-add-widgets-to-updateview-in-django) and implementing it in my code. 
* Another issue encountered was making django_summernote widget responsive in smaller screen sizes. I read through the documentation, added SUMMERNOTE_CONFIG to settings.py and customised the width and height. 
* When I tried to submit a form to create a new blog post, I got an error saying, “IntegrityError duplicate key value violates unique constraint”. It was explained to me that I was not providing a slug for when a post is being made. I eventually used the pythons replace method with the correct code. 
* At the final stage, my app was not deploying on Heroku. I got the “Error while running ‘$ python manage.py collectstatic —no input’.” It was explained to me that I had fontawesomefree installed, rather than importing the online version, which causes issues with Cloudinary. This was solved by uninstalling the fontawesome package, removing it from installed apps, pushing the changes, deleting the static folder inside the Cloudinary Media Library, and then re-deploying it. For Font Awesome, I added the online version.


# Technologies Used:
* HTML
* CSS
* JavaScript
* Python

# Frameworks, Libraries & Programs Used
* Django: Framework used in the development of the app. 
* Git: was used for version control by utilising the GitPod terminal to commit to Git and push to GitHub.
* GitHub: was used to store the overall project repository. 
* Bootstrap: was used for the design and structure of the app; grid, layout, columns, cards and forms structure.
* Summernote: was used to allow users to add styling to the blog posts and comments.  
* Crispy Form: was used for rendering the behaviour of the forms. 
* Font Awesome: was used to import icons for UX purposes.
* Am I Responsive: was used to seeing responsive design throughout the process and to generating mockup imagery to be used.
* Balsamiq Wireframes: was used in the initial design process to make wireframes.
* Heroku: used for the deployment of the project.
* Lighthouse: used for testing site functionality.
* W3C Markup Validation Service: used for HTML testing.
* W3C CSS Validation Service: used for CSS testing
* PEP8: used for Python file testing.

# Testing
Validator Testing
Lighthouse incognito
W3C Markup Validation Service
W3C CSS Validation Service
PEP8 Python Validator .py files

The W3C Markup Validator and W3C CSS Validator was used to validate my project to make sure no errors were returned.

# Deployment


# Credits

## Code
* The structure of the blog app was built using [Corey Schafer’s Django Tutorials’](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) playlist.
* [Codemy.com](https://www.youtube.com/watch?v=OuOB9ADT_bo&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=36) tutorial was used for the Post Blog Comment section. 
* [Coding Tranquility’s](https://codingtranquillity.herokuapp.com/blogpost/2/) tutorial was used for the Like/, Unlike section. 
* [The summernote documentation](https://github.com/summernote/django-summernote) and [Stackoverflow page](https://stackoverflow.com/questions/60578110/how-to-add-widgets-to-updateview-in-django) was used to add summer note widgets to the views. 

## Blog Post Content and Crisis Helplines
* [Rethink Mental Illness](https://www.rethink.org/)
* [Mind](https://www.mind.org.uk/)
* [Calm](https://www.calm.com/blog/)

# Acknowledgements
I would like to thank the tutors at Code Institute and fellow students on the Slack channel for their assistance and support. 
