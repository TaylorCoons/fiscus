# Notes

## Overview

Basic Python CLI script to provide notifications with stock exchange price changes

* CLI interfance to be ran as cron (or scheduler of choice)
* Interacts with yahoo finance api to pull data
* Checks against cli arguments to check if price movement is sufficient for notification
* Uses CLI arguments to notify the user of the price movement

## Implimentation Components

### CLI
Takes various arguments determining the outcome of the script
* Price movement % threshold
    - If the price movement is greater than this threshold is greater than the argument then trigger an alert
* Stock tickers
    - List of stock tickers to watch for price movements and check against the % threshold
    -  Entered as a space seperated list (nargs='+')
* Email
    - Email to send the notification to

### Notifier
Responsible for sending the email notification of the price movement
* Initialized with email?
* Inherits from a notifier interface?
* Validates email?

### Data collection
* Queries yahoo finance API for the price movement data

### Business logic
* Checks data collection
* Compares price movement data against CLI input if it is sufficient for sending a notification
* Invokes notifier to send notification