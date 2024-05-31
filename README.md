# GoalDigger
Overview
GoalDigger is a project management tool designed to help users set, track, and achieve their goals. This application provides a structured way to manage personal and professional goals.

Features
Goal creation and management
Progress tracking
Reporting and analytics

Prerequisites
Before you begin, ensure you have met the following requirements:
Python 3.12 installed on your machine
MySQL database server installed and running
Installation
Clone the Repository```sh
git clone https://github.com/saraalsheikh/GoalDigger.git
cd GoalDigger

Create a Virtual Environment


python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install Dependencies
Install the necessary Python packages:

pip install flask flask-mysql
Set Up the Database

Create a database in MySQL:
sql
Kopiera kod
CREATE DATABASE goaldigger;
Import the database schema:

mysql -u yourusername -p goaldigger < goaldigger.sql
Configure Environment Variables

Create a .env file in the root directory of the project and add your database configuration:


DB_HOST=localhost
DB_USER=yourusername
DB_PASSWORD=yourpassword
DB_NAME=goaldigger
Run the Application


python run.py
Usage
Access the application at http://localhost:5000/.
Follow the on-screen instructions to create and manage your goals.
Contributing
If you wish to contribute to the project, please follow these steps:

Fork the repository.
Create a new branch.
Make your changes and commit them.
Push to your forked repository.
Create a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or support, please open an issue or contact the repository owner.


What You Need to Download
**Python 3.12: Download from Python.org
MySQL: Download from MySQL.com
Python.org
Download Python
The official home of the Python Programming Language
