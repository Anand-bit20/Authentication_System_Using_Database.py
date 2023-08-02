# Authentication_System_Using_Database.py
I have developed this code of authentication system using Python and MySQL. Users can register and login. It validates user inputs for name, email, password, contact, and address before storing them in the "registration" table. The login() function checks user credentials and prints login success if valid.

1. Install Python and MySQL: Make sure you have Python installed on your computer. If not, download and install the latest version from the Python website (https://www.python.org/).
Install MySQL Server and MySQL Connector/Python. You can download them from the official MySQL website (https://dev.mysql.com/downloads/connector/python/) and follow the installation instructions.

2. Clone the Project: Clone or download the project from the GitHub repository to your local machine.

3. Set up MySQL Database: Open MySQL Workbench or any MySQL client and create a new database called "anand" (or any desired name).
Modify the connection details (host, user, password, database) in the Python script (main.py) to match your MySQL setup.

4. Install Required Libraries: Navigate to the project directory using the command prompt or terminal.
Install the required libraries using pip: pip install mysql-connector-python

5. Create the Database Table: Run the script main.py. It will automatically create the table called "registration" in the "anand" database if it doesn't exist.

6. Run the Authentication System: Run the script main.py in the command prompt or terminal using: python main.py
The program will display the main menu with options for registration, login, or exit.

7. Registration: Choose option 1 for registration.
Follow the prompts to enter your name, email, password, contact number, and address.
The system will validate the inputs, and if they are valid, it will store the user data in the database.

8. Login: Choose option 2 for login.
Enter your registered email and password when prompted.
If the credentials match the database, it will display "Login success" along with your email and password.

9. Exit: Choose option 3 to exit the program.
