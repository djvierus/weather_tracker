# Weather Tracker


## Project Description

This project is to query the weatherapi.com's site to periodically poll weather information for multiple locations and ingest the info into a postgres database.

There should be an attached SQL file in plain text attached to this project that you can run against an existing postgres database. Using pgadmin is recommended to setup.

This project assumes you have an account with weatherapi.com already and have a key to use to authenticate with them to pull back weather information.

## System Setup
To setup, ensure you have Python version 3 or later installed on your system and install all requirements in the provided "requirements.txt" file.

Rename the appsettings-template.json file to "appsettings.json" and update the values to what you need. BE SURE TO ADD YOUR OWN WEATHERAPI KEY TO THE APPSETTINGS.JSON FILE.

Once Python is installed with requirements, you should just be able to run "python /path/to/app/app.py" and start 

## Docker Setup
To setup, ensure you use a Python docker image of at least version 3 or later. The default docker file already points to Python version 3

Rename the appsettings-template.json file to "appsettings.json" and update the values to what you need. BE SURE TO ADD YOUR OWN WEATHERAPI KEY TO THE APPSETTINGS.JSON FILE.

DOUBLE CHECK THE DOCKERFILE. By default, the timezone is set to "America/Chicago", but please feel free to update it to whatever timezone you would prefer.

Run the 'docker build -t "app name" .' command in whatever directory you have a copy of this project in and then you should see it pop up on your list of available images.

Be sure to run the above "docker build" command in the same directory as the requirement.txt file so Python installs with all the dedicated python packages


## Notes

This is my first public project and most seasoned developers will likely spot plenty room for improvement in the code. This is just my personal project that I was wanting to write in my free time and to futher develop myself and skillsets. 

I am not a developer (or at least a trained one), but I am a Systems Administrator and help developers get their apps publically available, so I figured I'd give this a shot.

Open to feedback and critique, but again, this is only a passion project and not looking for perfection. 