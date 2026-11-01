# Website-status-checker
This code checks HTTP-status of the site's list. It shows statuses, history and average time of analyzing HTTP-status

Features:
The program has list of URLs;
It checks each of them, shows checked URL, HTTP code status, history of attending;
At the end it shows statistics about URLs: how many successful results, HTTP- or network-errors, and what average time did it take to analyze;

Instruments:
Python
Requests (library)

Installation:

Clone this repository:
git clone YOUR_REPOSITORY_URL

Navigate to the project directory:
cd YOUR_FOLDER

Install the required library:
- pip install requests

Usage
Run the script:
- python main.py

The program will automatically send requests to the websites specified in the urls list and display their HTTP status codes, response times, redirect information, and final statistics

What i learned and practiced:

Working with HTTP requests using Python.
Managing sessions with requests.Session().
Understanding HTTP status codes.
Handling exceptions in Python.
Measuring HTTP response time.
Working with redirects and response history.
Collecting and analyzing basic request statistics.

Disclaimer
This project is intended for educational purposes. It performs basic HTTP availability and status checks and is not a vulnerability scanner or penetration testing tool.
