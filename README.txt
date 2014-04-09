First iteration is done!


installation


are-you-human:

Go to folder
    python setup.py install



https://www.digitalocean.com/community/articles/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn
This will always deactivate whatever virtualenv is active currently. Now we need to install dependencies for PostgreSQL to work with Django with this command:

sudo apt-get install libpq-dev python-dev

Now that you have done this, install PostgreSQL like so:

sudo apt-get install postgresql postgresql-contrib

PostgreSQL is now installed on your machine and ready to roll.

Step Seven: Configure PostgreSQL
Let's start off our configuration by working with PostgreSQL. With PostgreSQL we need to create a database, create a user, and grant the user we created access to the database we created. Start off by running the following command:

sudo su - postgres

Your terminal prompt should now say "postgres@yourserver". If this is the case, then run this command to create your database:

createdb mydb

Your database has now been created and is named "mydb" if you didn't change the command. You can name your database whatever you would like. Now create your database user with the following command:

createuser -P

You will now be met with a series of 6 prompts. The first one will ask you for the name of the new user. Use whatever name you would like. The next two prompts are for your password and confirmation of password for the new user. For the last 3 prompts just enter "n" and hit "enter". This just ensures your new users only has access to what you give it access to and nothing else. Now activate the PostgreSQL command line interface like so:

psql

Finally, grant this new user access to your new database with this command:

GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

You now have a PostgreSQL database and a user to access that database with. Now we can install Django and set it up to use our new database.


