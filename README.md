# challenge - Test Automation - Global Hitss

This is a test case to navigate to the MercadoLibre website and perform several actions. 
The test script was written in Python and uses Selenium library for web automation. We also used ChromeDriver as the web driver.

## Test Actions

The following actions are performed by the test case:

   - Select the country as "Mexico" by clicking on the country selector element and selecting "Mexico" from the dropdown menu.
   - Enter "playstation 4" in the search bar and click the search button.
   - Apply the filter by clicking the "Nuevos" checkbox in the condition filter section.
   - Apply the filter by clicking the "Cdmx" checkbox in the location filter section.
   - Apply the order by selecting "Mayor a Menor Precio" in the order filter section.


## Running the Test

To run the test case, execute the following command in the terminal:

```
$ pytest test.py
```

## Tips.

#### You will need Selenium WebDriver for Chrome installed on your system. To check if you have it you can follow these steps:

   - Open your terminal/command prompt
   - Type "chromedriver" and press enter
   - If you see a message that says "Starting ChromeDriver...", then you have the ChromeDriver installed. If you see an error message, then you don't have it installed.

#### To add the ChromeDriver to your system path, you can follow these steps:

   - Download the ChromeDriver from the official [website](https://sites.google.com/chromium.org/driver/).
   - Extract the file to a directory of your choice.
   - Open your terminal/command prompt and type "echo $PATH". This will show you the current directories in your system path.
   - Move the ChromeDriver executable file to one of the directories listed in your system path. For example, if you see "/usr/local/bin" in the output of the previous command, you can move the ChromeDriver executable file to that directory.
    
#### Finally if you want to take a look for a report you can access by [this link](https://docs.google.com/document/d/1xcgGZEv3k8WUms-IIi59tkjKCl8_gQoYuYRRf9GsupU/edit?usp=sharing).
