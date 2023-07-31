# Deployment
The site was deployed via [Heroku]( https://id.heroku.com/login), and the live link can be found here: [Drizzle and Shade website](https://drizzleandshade-4e77ed93aac5.herokuapp.com/) 

## Table of contents

* [Github](#github)
    * [Clone the repository](#clone_the_repository)
    * [Fork Repository](#fork_repository)
* [Django](#django)
    * [AllAuth](#all-auth)
* [Heroku](#heroku)
    * [Preparing for deployment](#preparation-for-deployment)
    * [Generate a SECRET KEY](#generate-a-secret-key)
* [Setting up AWS](#setting-up-aws)
    * [S3](#s3)
    * [IAM](#iam)
    * [Connecting AWS to django](#connecting-aws-to-django)
* [Stripe](#stripe)
    * [Payments](#payments)
    * [Webhooks](#webhooks)
    


## Github

This project was developed utilising the [Code Institute Template]( https://github.com/Code-Institute-Org/python-essentials-template). Some of the deployment steps below are specifically required for the new CI template and may not be applicable to older versions, or different projects.

Gitpod was used to write the code and push the code to repository created in github.

The git commands I used to push the code from gitpod to github were:

        git add .
This command was used to add the file(s) to the staging area before they are committed.

        git commit -m “commit message”
This command was used to commit changes to the local repository queue ready for the final step.

        git push
This command was used to push all committed code to the remote repository on github.


### Clone the repository
The steps to clone a repository are as follows:
1.	Navigate to the GitHub repository you would like to clone
2.	Click on the code drop down button
3.	Select if you prefere to clone using HTTPS, SSH, or Github CLI 
4.	Copy the repository link to the clipboard
5.	Open Git Bash
6.	Change the current working directory to the one where you want the cloned directory
7.	Type git clone and then paste the URL from the clipboard 
8.	Press Enter to create your local clone.

The repository will now be cloned on your local machine for use.

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

##### Back to [top](#table-of-contents)

## Django

This project build using the Django framework. 

These are the steps I followed to install django:

* In the IDE (I used gitpod), type the command

        pip3 install django

* To name the project and add the django project folder to the file explorer, type the command 

        django-admin startproject *Your project name here* 

* Add a gitignore file, type the command 

        touch .gitignore

* Inside this file add these 3 lines: 
    
        *.sqlite3
        *.pyc
        __pycache__
    
* To check everything is working, type the command 

        python3 manage.py runserver

This should expose port 8000. Open that port and you should be welcomed by Django's success page, I needed to add the host name to allowed hosts in the setting file.

* To perform the initial migrations, type the command 

        python3 manage.py migrate

* To access to the admin panel, create a superuser, type the command
        
        python3 manage.py createsuperuser

Add a username and password with an optional email address.

* Once these steps are completed, push your changes to github but using the above commands.

### All Auth

Inside the django framework is a package called Allauth. This package handles all the registration and sign in processes. The steps to install Allauth can be found [here](https://django-allauth.readthedocs.io/en/latest/installation.html).

##### Back to [top](#table-of-contents)

## Heroku

Heroku was used to deploy the project

1. Sign in to Heroku. If you do not have an account you can sign up for free [here](https://signup.heroku.com/).
2. Once you are logged in, click the button 'New' and select 'Create new app'.
3. Name the app, then select what region is closest to you and click 'Create App'.
4. The database URL you copied from elephantSQL should be pasted into the value of a new configuration variable called DATABASE URL that you create in the settings tab (the value should not have quotation marks around it)

### Preparation for deployment

* Install dj_database_url and psycopg2 as they are both needed for connecting to the external database you've just created

        pip3 install dj_database_url==0.5.0 psycopg2

* Update your requirements.txt file

        pip3 freeze > requirements.txt

* In settings.py underneath import os, add import dj_database_url

* Then scroll down the file till you find your database settings. Comment out the default configuration and underneath insert the code:  

        DATABASES = {
        'default': dj_database_url.parse('paste-elephantsql-db-url-here')
    }

* In the terminal, run the show migrations command to confirm connection to the external database.

        python3 manage.py showmigrations

* If it is connected to the database, you will see a list of unchecked migrations. Now run migrations to migrate the models to the new database:

        python3 manage.py migrate

* Create a superuser for the new database by running the below command and input a username, email and password when prompted

        python3 manage.py createsuperuser

* You should now be able to go to the browser tab on the left of the page in elephantsql, click the table queries button and see the user you've just created by selecting the auth_user table.

* Before you commit these changes, you will need to remove the Databases section in the settings.py and uncomment the original database. This is to stop your Postgres database URL from ending up in version control.

* Add an if statement in our settings.py to run the postgres database when using the app on heroku or sqlite if not. Scroll back to the database section and refactor the code to look like this:  
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
    ```

* Install gunicorn which will act as the web server and freeze this to the requirements.txt file.

        pip3 install gunicorn 
        pip3 freeze > requirements.txt

* Create a Procfile in the root directory. This instructs Heroku to build a web dyno that serves our Django app and runs Gunicorn. Add the following code in the procfile

        web: gunicorn drizzle_and_shade.wsgi


* Back in heroku, navigate to settings and in the config vars input the key DISABLE_COLLECTSTATIC with the value 1, and click 'Add'. This is to stop heroku from collecting any static files when you deploy.

* Add heroku to your allowed hosts in your settings.py. Back in your project, in the settings file, scroll down to ALLOWED_HOSTS, and inside the brackets insert the url to your app, followed by 'localhost'. It should look something like this:     

        ALLOWED_HOSTS = ['your-project-name.herokuapp.com', 'localhost']

* Add, commit and push these changes, followed by a push to heroku with the below command. The app will now be deployed, without any static files, but this will be fixed when setting up AWS, documented below. 

        git push heroku main'

* To setup the project to automatically deployed to heroku when pushing your work to github you can. To do so, In heroku go to the deploy tab, and in the 'deployment method' section connect it to github. You will need to search for your repository and once found click 'connect'. Then scroll down and click 'Enable automatic deploys'. Now when you push to github your code will automatically deploy to Heroku as well. 

##### Back to [top](#table-of-contents)

### Generate a SECRET KEY

* When you start a project in Django, a secret key is immediately generated; however, we shouldn't utilize this key in our deployed version as it makes our website insecure.

* We can use a random key generator to create a new SECRET_KEY which we can then add to our Heroku config vars which will then keep the key protected.

* [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) is one of the sites where we can generate a secret key for our django project
- Create a new key and copy the key
- Create a new config var with the key SECRET KEY in the Heroku settings.

* Update the SECRET_KEY in the settings.py

        SECRET_KEY = os.environ.get('SECRET_KEY', ' ')

* Update the debug variable to true if in development

        DEBUG = 'DEVELOPMENT' in os.environ

* Save, add, commit and push these changes.

##### Back to [top](#table-of-contents)

## Setting up AWS

Amazon web services are used to store all our static and media files. 

### S3

* First you will need to sign up to AWS which you can do [here](https://aws.amazon.com/).
* Once you have created an account and logged in, under the All Services>Storage menu, navigate to S3
* On the S3 page you will need to create a new bucket. To do this click the orange button that says 'Create Bucket'.
* Name the bucket and select the closest region to you. To keep things simple it is recommended naming the bucket after your project.
* Under 'Object Ownership' select 'ACLs enabled' and leave the Object Ownership as Bucket owner preferred. 
* Uncheck the 'Block all public access' checkbox and check the warning box to acknowledge that the bucket will be made public, then click create bucket. 
* Once created, click the bucket's name and navigate to the properties tab. Scroll to the bottom and under 'Static website hosting' click 'edit' and change the Static website hosting option to 'enabled'. Copy the default values for the index and error documents and click 'save changes'.
* Now navigate to the permissions tab, scroll down to the Cross-origin resource sharing (CORS) section, click edit and paste in the following code:  

    [
        {
            "AllowedHeaders": [
            "Authorization"
            ],
            "AllowedMethods": [
            "GET"
            ],
            "AllowedOrigins": [
            "*"
            ],
            "ExposeHeaders": []
        }
    ]

* Then scroll back up to the 'Bucket Policy' section. Click 'edit' and then 'Policy generator'. This should open the AWS policy generator page.
* From here under the 'select type of policy' dropdown menu, select 'S3 Bucket Policy'. Then inside 'Principle' allow all principals by typing a *.
* From the 'Actions dropdown menu select 'Get object'. Then head back to the previous tab and locate the Bucket ARN number. Copy that, return to the policy generator and paste it in the field labelled Amazon Resource Name (ARN).
* Once that's completed click 'Add statement', then 'Generate Policy'. Copy the policy that's been generated and paste it into the bucket policy editor.
* Before you click save, add a '/*' at the end of your resource key. This is to allow access to all resources in this bucket.
* Once those changes are saved, scroll down to the Access control list (ACL) section and click 'edit'.
* Next to 'Everyone (public access)', check the 'list' checkbox. This will pop up a warning box that you will also have to check. Once that's done click 'save'. 

##### Back to [top](#table-of-contents)

### IAM

* Now that your bucket is ready we need to create a user to access it. In the search bar at the top of the window, search for IAM and select it.
* Once on the IAM page, click 'User Groups' from the side bar, then click 'Create group'.
* Name the group 'manage-*your-project-name*' and click 'Create group' at the bottom of the page. 
* Then from the sidebar click 'Policies', then 'Create policy'.
* Go to the JSON tab and click 'import managed policy'. Search for 'S3' and select 'AmazonS3FullAccess' and click import.
* Once this is imported you will need to edit it slightly. Go back to your bucket and copy your ARN number. Head back to this policy and update the Resource key to include your ARN, and another line with your ARN followed by a /*. It should end up looking something like this: 

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:*",
                    "s3-object-lambda:*"
                ],
                "Resource": [
                    "YOUR-ARN-NO-HERE",
                    "YOUR-ARN-NO-HERE/*"
                ]
            }
        ]
    }

* Click 'Next: Tags', 'Next: Review', and on this page give the policy a name. This could be something as simple as the project name followed by the word policy, and then a short description eg: Access to S3 bucket for 'YOUR PROJECT' static files. Then click 'Create policy'. 
* This will take you back to the policy page where you should be able to see your newly created policy. Now we need to attach it to the group we created.  
* Click 'User groups', and click the group you created earlier. Go to the permissions tab and click 'Add permission' and from the dropdown click 'Attach policies'. 
* Find the policy you just created, select it and click 'Add permissions'.
* Finally, create a user to put in the group. Select users from the sidebar and click 'Add user'.  
* Give your user a user name, check 'Programmatic Access', then click 'Next: Permissions'. 
* Select your group that has the policy attached and click 'Next: Tags', 'Next: Review', then 'Create user'.
* On the next page, download the CSV file. This contains the user's access key and secret access key which you will need later. 

##### Back to [top](#table-of-contents)

### Connecting AWS to django

Now that you have created a S3 bucket with its user group attached, we need to connect it to django.

* Install boto3 and django storages 

        pip3 install boto3
        pip3 install django-storages

* Freze them to the requirements.txt file

        pip3 freeze > requirements.txt

* Add storages to the installed apps in settings.py

* Add the following code in settings.py to use our bucket

        if 'USE_AWS' in os.environ:
            AWS_S3_OBJECT_PARAMETERS = {
                'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
                'CacheControl': 'max-age=9460800',
            }
            
            AWS_STORAGE_BUCKET_NAME = 'enter your bucket name here'
            AWS_S3_REGION_NAME = 'enter the region you selected here'
            AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
            AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

            # Static and media files
            STATICFILES_STORAGE = 'custom_storages.StaticStorage'
            STATICFILES_LOCATION = 'static'
            DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
            MEDIAFILES_LOCATION = 'media'

            # Override static and media URLs in production
            STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
            MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

* Add the keys from AWS to the configuration variables in Heroku:

    | KEY                       | VALUE         |
    | -------------             | ------------- |
    | `AWS_ACCESS_KEY_ID`       | PasteThe access key value from the amazon csv file downloaded in the last section         |
    | `AWS_SECRET_ACCESS_KEY`   | Paste The secret access key from the amazon csv file downloaded in the last section         |
    | `USE_AWS`                 | True         |

* Remove the DISABLE_COLLECTSTATIC variable in Heroku.

* Create a file called custom_storages.py in the root directory and add the following code to file you created just now

        """ Custom storages for AWS file storage. """
        from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage

        class StaticStorage(S3Boto3Storage):
            location = settings.STATICFILES_LOCATION

        class MediaStorage(S3Boto3Storage):
            location = settings.MEDIAFILES_LOCATION

* In order to override the static and media URLs in production and update the app where to put static and media assets, add the following to settings.py.

        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

* Save everything, add, commit and push these changes to make a deployment to Heroku.

* In S3 in AWS, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'. 
* Inside the new media folder you just created, click 'Upload', 'Add files', and then select all the images that you are using on your site.
* Under 'Permissions' select the option 'Grant public-read access' and click upload. You may need to also check an acknowledgment warning checkbox too. 
* Once that is finished you're all set. All your static files and media files should be automatically linked from django to your S3 bucket.

##### Back to [top](#table-of-contents)

## Stripe

Stripe is needed to handle the checkout process when a payment is made. You will need a stripe account which you can sign up for [here](https://stripe.com/en-gb).

### Payments

* To set up stripe payments you can follow their guide [here](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details).

### Webhooks

* To set up a webhook, sign into your stripe account and click 'Developers' located in the top right of the navbar.
* Then in the side-nav under the Developers title, click on 'Webhooks', then 'Add endpoint'.
* On the next page you will need to input the link to your heroku app followed by /checkout/wh/. It should look something like this:  

        https://your-app-name.herokuapp.com/checkout/wh/

* Then click '+ Select events' and check the 'Select all events' checkbox at the top before clicking 'Add events' at the bottom. Once this is done finish the form by clicking 'Add endpoint'.
* Your webhook is now created and you should see that it has generated a secret key. You will need this to add to your heroku config vars.
* Head over to your app in heroku and navigate to the config vars section under settings. You will need the secret key you just generated for your webhook, in addition to your Publishable key and secret key that you can find in the API keys section back in stripe.
* Add these values under these keys:  

        STRIPE_PUBLIC_KEY = 'insert your stripe publishable key'
        STRIPE_SECRET_KEY = 'insert your secret key'
        STRIPE_WH_SECRET = 'insert your webhooks secret key'

* In your setting.py file in django, insert the following near the bottom of the file:  

        STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
        STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
        STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

##### Back to [top](#table-of-contents)

[Return to README.md](README.md)