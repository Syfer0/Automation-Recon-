# Automation
Domain Enumeration Script
This is a Python script for performing reconnaissance on a given domain using various tools. The script takes a domain name as input from the user, creates an output directory with the name of the domain followed by "_output", and saves the results of each tool in a separate file within the output directory.

Prerequisites
This script requires the following tools to be installed on the system:

assetfinder
subfinder
httpx
dirsearch
nikto
wafw00f
waybackurls
githound
gitrob
gitgraber
Usage
To run the script, execute the following command in the terminal:

Copy code
python domain_enumeration.py
The script will prompt the user to enter the domain name.

Output
The script creates an output directory with the name of the domain followed by "_output". The output directory contains the following files:

assetfinder.txt: Contains the subdomains found by Assetfinder.
subfinder.txt: Contains the subdomains found by Subfinder.
all_subdomains.txt: Contains the list of all subdomains found by both Assetfinder and Subfinder.
httpx.txt: Contains the status code, title, and URL of each subdomain that responds to HTTP/HTTPS requests.
dirsearch.txt: Contains the results of Dirsearch, including directories and files that were found on the web server.
nikto.txt: Contains the results of Nikto, including potential vulnerabilities and misconfigurations found on the web server.
wafw00f.txt: Contains the result of Wafw00f, which attempts to identify the web application firewall (WAF) in use on the web server.
waybackurls.txt: Contains the URLs found in the Wayback Machine archive for the given domain.
githound.txt: Contains the results of GitHound, which searches for sensitive information in public repositories on GitHub.
gitrob_output/: Contains the results of GitRob, which searches for sensitive information in public and private repositories on GitHub.
gitgraber.txt: Contains the results of GitGraber, which searches for sensitive information in public and private repositories on GitHub.
Note: By default, the script is set to run all tools. If you want to skip any of the tools, you can comment out the corresponding lines of code
