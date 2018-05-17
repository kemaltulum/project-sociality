# Project-Sociality

Extract the price value of a product in the given page url. This program only works with the product detail pages of hepsiburada.com like [this](https://www.hepsiburada.com/asus-x542ur-gq030-intel-core-i7-7500u-8gb-1tb-gt930mx-freedos-15-6-tasinabilir-bilgisayar-p-HBV000008OBG5)

## How To Run

* You should first install Python 3.x
* You can run the program with the command below:

```
python extractPrice.py {{valid url}}
```
**Please make sure that `python` command in your PC runs Python 3.x. (You would need to run with `python3` command instead of `python`)**

* The program gives the price of the product if a valid url is given.
```
$ python3 extractPrice.py https://www.hepsiburada.com/dell-inspiron-3576-intel-core-i5-8250u-8gb-1tb-radeon-520-linux-15-6-fhd-tasinabilir-bilgisayar-fhdb25f81c-p-HBV00000AWDAQ?magaza=Hepsiburada
2399.00 TL
```
