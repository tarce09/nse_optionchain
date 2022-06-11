# Nse_optionchain

This program takes nse option chain data from all the available equities and finds the equity's highest oi call value, its corresponding strike price, the highest put oi value and its strike price.

This uses the nseindia's api and can be run anytime 

It gives an excel file output with the equity name,highest call oi,its strike price,highest put oi,its stike price.

The equity symbols must be changed everytime the symbol or equity list is refreshed in the website 

## Installation

Install project with cmd line

```bash
  pip install pandas
  pip install requests
```

## Running
Go to code-

In header variable change the key values according to your browser data by
going into https://www.nseindia.com/option-chain , right click,inspect element->network->refresh the screen->click on option-chain
and copy the values of the keys and paste in the code

go to the place where u have saved the file in the terminal and write
``
  python new_code.py
``

note:-new_code.py is the name of my file if u have a different file name change it accordingly.



## Code done for

Voltago Electricals Pvt. Ltd
    
