Overview of the Fitraka Fitness Tracking Application.

Fitraka Fitness Tracking Application is an all-inclusive fitness management system designed to assist individuals of all fitness levels in achieving their health and fitness objectives. This README contains installation instructions for the application as well as a list of its dependencies and their versions.

Equipped with
Create a personalized account to gain access to all of the app's features.
Set and monitor your fitness objectives, whether they involve weight loss, muscle gain, or general fitness improvement.
Log your daily routines, including exercises, sets, repetitions, and weights.
To manage your nutrition, track your daily caloric intake and maintain a food journal.
Community Assistance: Join a group of like-minded fitness enthusiasts for support and motivation.
View comprehensive reports and statistics to evaluate your progress.
![first Screenshot of my app](https://github.com/Neme88/Fitraka/blob/main/Screenshot%20from%202023-09-13%2000-28-41.png)
![Second Screenshot of my app](https://github.com/Neme88/Fitraka/blob/main/Screenshot%20from%202023-09-13%2000-32-21.png)
![Third Screenshot of my app](https://github.com/Neme88/Fitraka/blob/main/Screenshot%20from%202023-09-13%2000-33-33.png)

Setting up
To install and activate the Fitness Tracking Application, follow these steps:

The necessary prerequisites
You have Python 3.8 or higher installed.
package manager pip.
Installing Procedures
Clone the repository to a local repository:

bash
git clone https://github.com/Neme88/Fitraka.git to copy the code.
Enter the project's directory:

bash
Copy fitness-tracking app code cd
Develop a virtual environment (suggested):

copy code using bash vartualenv venv
Activate the virtual setting:

On Microsoft Windows: bash
The code is venvScriptsactivate.
bash on macOS and Linux
Copy source code from venv/bin/activate
Install the necessary dependencies with pip:

bash copy code pip install --requirements.txt
Configure the database:

flask db init flask db migrate flask db upgrade
Start the software:

bash
Copy code and execute flask
Fitraka Fitness Tracking Application should now be locally operating on your system. Use your web browser to navigate to http://localhost:5000.

Dependencies
The Fitness Tracking Application relies on the specified versions of the following Python packages:

charset-normalizer==2.0.12 click==8.1.7 contourpy==1.1.0 cycler==0.11.0 dominate==2.8.0 Flask==2.0.1
Flask-Cors==4.0.0 Flask-Login==0.6.0 Flask-Mail==0.9.1 Flask-Migrate==3.1.0 Flask-MySQLdb==0.2.0 Flask-RESTful==0.3.9 Flask-SQLAlchemy==2.5.1 Flask-Uploads==0.2.1 Flask-WTF==0.15.1


Author:
Chinemerem C Nwaka.

Common Knowledge
This open-source fitness tracking application seeks to provide individuals with an intuitive platform for monitoring and enhancing their fitness. We encourage contributions from the community to improve the functionality and usability of the site. Feel free to fork the repository and submit pull requests with problem fixes and enhancements.

Happy monitoring, and best wishes for your health!
