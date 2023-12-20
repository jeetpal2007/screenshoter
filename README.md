# Subdomain Screenshot Tool

This Python script automates the process of capturing screenshots of subdomains' webpages using the Firefox browser and Selenium.

## Features

- Capture screenshots of single or multiple subdomains.
- Run in headless mode for non-GUI operation.
- Save screenshots as PNG files.

## Getting Started

Follow these steps to set up and use the tool on your local machine.

### Prerequisites

- Python 3.x
- Firefox browser (installed on your system)
- GeckoDriver (Firefox WebDriver) - Download from [GeckoDriver Releases](https://github.com/mozilla/geckodriver/releases)

### Installation

1. Clone the repository :

`git clone https://github.com/jeetpal2007/screenshoter.giy `

2. Install the required packages using pip:
   
` pip install -r requirements.txt`

3. Place the `geckodriver` executable in the same directory as the script. 

### Usage

1. Open a terminal and navigate to the directory containing the script.

2. Run the script:
   
`python3 screenshoter.py'

3. Follow the on-screen instructions to choose between capturing screenshots for a single subdomain or multiple subdomains.

4. Provide the required inputs, such as the subdomain(s) or the path to the file containing a list of subdomains.

5. The tool will open each subdomain's webpage, capture a screenshot, and save it as a PNG file in the same directory.

## Notes

- Ensure that the subdomains are provided in the correct format (with or without "http://").
- Respect website terms of use and scraping policies when using this tool.
- This script assumes you're running it on a Linux environment. If you're using another operating system, make the necessary adjustments.



