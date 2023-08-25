# Easy bitlink

This is a little script for creating short link on `bit.ly` and getting click counts for your bitlinks.

### Requirements

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```
It's recommended to use virtual enviroment for project isolation
### Environment variables
- TOKEN
1. Create `.env` file near script.py
2. Write there `BITLY_API_TOKEN=YOUR_TOKEN_FROM_BITLY` and save

## Run

Launch on Linux(Python 3) or Windows:

```bash
$ python script.py YOUR_URL
```


You will see:
```
(venv) PS ..\devman_lesson2> python script.py https://bit.ly/3OPqBy2
Total clicks on https://bit.ly/3OPqBy2 is 1

```


