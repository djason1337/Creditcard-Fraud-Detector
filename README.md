Overview

This Flask web application detects potential fraudulent activities based on the user's IP address and the billing and shipping information provided by the user. 
It compares the user's city, as determined by their IP address, with the city they enter on the form. It also checks if the billing and shipping addresses match. 
The application renders a "success" or "failed" page based on a predefined threshold.

Features:

 -Retrieves the user's public IP address.

 -Determines the user's city based on the IP address.

 -Compares the user's provided city with the IP-derived city.

 -Checks if billing and shipping addresses match.

 -Renders appropriate templates based on the fraud score.

Dependencies:

-Flask

-Requests

How It Works
IP Address Retrieval: grab_ip() function uses the ipify API to get the user's public IP address.

Location Data: get_location() function uses the ipinfo.io API to get location data based on the IP address.

Index Route: The index() route renders the index.html template with the user's IP address and location data.

Fraud Score Calculation: The post_fraudscore() route calculates a fraud score based on the provided city, billing, and shipping addresses. If the score exceeds the threshold, it renders the failed.html template; otherwise, it renders the success.html template.

Templates
index.html: The main page where users enter their billing and shipping information.

failed.html: Displayed if the transaction is flagged as potentially fraudulent.

success.html: Displayed if the transaction is deemed legitimate.
