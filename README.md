# G-Audit
Simple python script to check for public Google groups and sites.

It automates the following two security checks.
1. https://tutorgeeks.blogspot.com/2019/06/google-sites-misconfiguration.html
2. https://tutorgeeks.blogspot.com/2019/05/google-groups-misconfiguration.html

# Usage
1. git clone git@github.com:tutorgeeks/G-Audit.git && cd G-Audit.git
2. pip install -r requirements.txt
3. Configure your chromedriver path.
   webdriver.Chrome('Path to your ChromeDriver installation')
4. Enter the list of domains that you wanted to test in "list.txt" file.
   hackerone.com
   facebook.com

# output
Trying to login into Google...
Successfully logged into Google...
List of websites that will be tested: ['hackerone.com', 'bugcrowd.com']
<------- Checking for Google groups misconfiguration ------->
No misconfiguration: https://groups.google.com/a/hackerone.com
No misconfiguration: https://groups.google.com/a/bugcrowd.com
<------- Checking for Google sites misconfiguration ------->
Access Denied:https://sites.google.com/a/hackerone.com
Access Denied:https://sites.google.com/a/bugcrowd.com
