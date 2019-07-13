# Cryptocurrency Bot

A bot to check on cryptocurrency values

## Requirements

### Python enviroment

This section is a guide to the installations of a python environment with the requirements of this repository.

First, install [Anaconda](https://www.anaconda.com/distribution/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html), both of them give you similar results, but the latter requires less disk space.

Now, create a python virtual environment and install the required packages following the commands. Substitute **<environment_name>** with a name for your environment

```console
user@computer:~$ conda create -n <enviroment_name> anaconda python=3
user@computer:~$ conda activate <enviroment_name> or source activate <enviroment_name>
(<enviroment_name>) user@computer:~$ conda install -c anaconda beautifulsoup4 requests
```

## Using the scripts

To use the provided scripts, make sure to activate your python environment, that can be accomplished by:

```console
user@computer:~$ conda activate <enviroment_name>
```

### [Bot](./scraper.py)

This script is intended to check [coinbase](https://www.coinbase.com/price) prices daily and send a e-mail with the cryptocurrencys prices, you need to configure the **email credentials**, and **User-Agent** in the script. Usage:

```console
(<enviroment_name>) user@computer:~$ python scraper.py
```
