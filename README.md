# etf_calc

Simple calculator for building a portfolio of MSCI ACWI/Europe/EM ETFs.


### Description

Basically, AIs were unsuccesful at correctly solving the following prompt:

>I want to build a portfolio with a given ratio of developed to emerging markets, and want the portfolio to consist of 1 ETF tracking MSCI ACWI, 1 ETF tracking MSCI Europe and 1 ETF tracking MSCI Emerging Markets. Also, I want to use the MSCI Europe to reduce the overexposure to American stocks, bringing the ratio of American and European stocks in line with the GDP ratio of America and Europe. How can I calculate correct ratio of these 3 ETFs? Please use only algebra to solve this problem and write a calculation tool in Python.

and thus I had to dig up my rusty math skills and do it myself.

### Usage

Run the calculator and enter the desired developed-market share:

```console
$ python3 etf_calc.py
Enter desired developed market share (in %): 73
ACWI ETF: 59.461%
Europe ETF: 20.780%
EM ETF: 19.759%
```

### Data assumptions

The default constants use the latest available data checked in July 2026:

```python
DEVELOPED_ACWI = 0.878222
US_ACWI = 0.636300
EUROPE_ACWI = 0.138704
GDP_RATIO_US_EUROPE = 1.303429
```

The ACWI developed-market and European shares are derived from the index
capitalizations published in MSCI's June 30, 2026 factsheets:

- Developed markets: MSCI World / MSCI ACWI = 89.1139 / 101.4708 = 87.8222%
- Europe: MSCI Europe / MSCI ACWI = 14.0744 / 101.4708 = 13.8704%
- United States: the published ACWI country weight is 63.63%

Sources: [MSCI ACWI](https://www.msci.com/documents/10199/255599/msci-acwi-net.pdf),
[MSCI World](https://www.msci.com/documents/10199/255599/msci-world-index.pdf), and
[MSCI Europe](https://www.msci.com/documents/10199/255599/msci-europe-index.pdf).

The GDP ratio compares U.S. nominal GDP with the combined nominal GDP of the
15 countries represented by MSCI Europe. Using 2025 values, USD 30.7697tn /
USD 23.6067tn = 1.303429. Source: the World Bank's
[GDP in current U.S. dollars](https://api.worldbank.org/v2/country/USA;AUT;BEL;DNK;FIN;FRA;DEU;IRL;ITA;NLD;NOR;PRT;ESP;SWE;CHE;GBR/indicator/NY.GDP.MKTP.CD?date=2025&format=json&per_page=100)
series, last updated July 13, 2026.

MSCI Europe is not the same as the European Union: it includes the UK,
Switzerland, and Norway. Using the GDP of the same 15-country region keeps the
economic target consistent with the index exposure. All of these inputs change
over time and should be refreshed periodically.

### Disclaimer

This is no financial advice. Use and invest at your own risk.
