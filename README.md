# etf_calc
Simple calculator for building a portfolio of MSCI ACWI/EU/EM ETFs


### Description

Basically, AIs were unsuccesful at correctly solving the following prompt:

>I want to build a portfolio with a given ratio of developed to emerging markets, and want the portfolio to consist of 1 ETF tracking MSCI ACWI, 1 ETF tracking MSCI Europe and 1 ETF tracking MSCI Emerging Markets. Also, I want to use the MSCI Europe to reduce the overexposure to American stocks, bringing the ratio of American and European stocks in line with the GDP ratio of America and Europe. How can I calculate correct ratio of these 3 ETFs? Please use only algebra to solve this problem and write a calculation tool in Python.

and thus I had to dig up my rusty math skills and do it myself.

Usage should be self-explanatory. The required constants (shares of US, EU, EM in ACWI as well as GDP ratio of US vs. EU) were researched by some quick online searches and maybe are not 100% accurate.

### Disclaimer
This is no financial advice. Use and invest at your own risk.
