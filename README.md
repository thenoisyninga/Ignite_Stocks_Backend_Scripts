# Ignite_Stocks_Backend_Scripts
## About
A package of scripts that handle Database Populating Operations, Admin Controls, Stock Value Changes, Automated Mass Email Communication for FPS Ignite Stocks Round.

This package contains the main program that executees stocks, and other modules that:
- Initialize all kinds of stock market values (ICs, Owned Assets, Asset Values).
- Log out or allow login to all, a single delegation group, or a single delegation.
- Check and report exactly how many people are logged in.
- Allow or Block Stock Market Logins
- Spontaneously change a delegation's ICs.
- Migrate users from the mobile app database to the stock market database.
- Delete prior data and add dummy users for testing

## Installation
Install the required python libraries, have everything in the same directory. Have the ServiceAccountKey.json file in the directory for validation of the firebase connection, and have a text file 'password.txt' with the stock database password in the same directory to validate the SQL connection.

## Usage
The Main_Process.py file executes the stock market round
The Admin_Controls.py file is a diverse package that gives access to all the features mentioned above
