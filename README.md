# challenge - Test Automation - Global Hitss

This is a test case to navigate to the MercadoLibre website and perform several actions. 
The test script was written in Python and uses the Pytest testing framework.

## Test Actions

The following actions are performed by the test case:

    * Select the country as "Mexico" by clicking on the country selector element and selecting "Mexico" from the dropdown menu.
    * Enter "playstation 4" in the search bar and click the search button.
    * Apply the filter by clicking the "Nuevos" checkbox in the condition filter section.
    * Apply the filter by clicking the "Cdmx" checkbox in the location filter section.
    * Apply the order by selecting "Mayor a Menor Precio" in the order filter section.


## Running the Test

To run the test case, execute the following command in the terminal:

```
$ pytest test.py
```
