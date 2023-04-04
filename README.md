# challenge - Test Automation 

## Table of contents
* [Introduction](#introduction)
* [Test Actions](#test-actions)
* [Installation](#installation)
* [Running the Test](#running-the-test)
* [Tips](#tips)

## Introduction

This Python script automates the process of searching for Playstation 4 products on the MercadoLibre website, filtering them by location, and sorting them by price in descending order. It then displays the name and price of the top 5 products. The script leverages the Selenium library for automating browser actions and ChromeDriver as the web driver.

This code automates the process of searching for products on the MercadoLibre website, making it faster and more efficient for users to find what they are looking for.

## Test Actions

The test case performs the following actions:

   - Select the country as "Mexico" by clicking on the country selector element and selecting "Mexico" from the dropdown menu.
   - Enter "playstation 4" in the search bar and click the search button.
   - Apply the filter by clicking the "Nuevos" checkbox in the condition filter section.
   - Apply the filter by clicking the "Cdmx" checkbox in the location filter section.
   - Apply the order by selecting "Mayor a Menor Precio" in the order filter section.

## Installation

To run this test case, you need to have Python 3 installed on your system. You also need to install the Selenium WebDriver for Chrome.

To install the required packages, run the following command:

```
$ pip install selenium
```

To install the Selenium WebDriver for Chrome, download the latest version of ChromeDriver and add it to your system PATH. (see below)

## Running the Test

To run the test case, execute the following command in the terminal:

```
$ python3 test.py
```

If you are using Visual Studio Code, you can run it directly.

## Tips

#### Checking if you have the Selenium WebDriver for Chrome installed on your system:

   - Open your terminal/command prompt
   - Type "chromedriver" and press enter
   - If you see a message that says "Starting ChromeDriver...", then you have the ChromeDriver installed. If you see an error message, then you don't have it installed.

#### Adding the ChromeDriver to your system path:

   - Download the ChromeDriver from the official [website](https://sites.google.com/chromium.org/driver/).
   - Extract the file to a directory of your choice.
   - Open your terminal/command prompt and type "echo $PATH". This will show you the current directories in your system path.
   - Move the ChromeDriver executable file to one of the directories listed in your system path. For example, if you see "/usr/local/bin" in the output of the previous command, you can move the ChromeDriver executable file to that directory.
    
#### Viewing the report: 
You can view the report by clicking on [this link](https://docs.google.com/document/d/1xcgGZEv3k8WUms-IIi59tkjKCl8_gQoYuYRRf9GsupU/edit?usp=sharing).
