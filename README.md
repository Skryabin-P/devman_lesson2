# Easy bitlink

This is a little script for creating short link on `bit.ly` and getting click counts for your bitlinks.

### Requirements

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```
### Environment variables
- TOKEN
1. Create `.env` file near script.py
2. Write there `BITLY_API_TOKEN=YOUR_TOKEN_FROM_BITLY` and save

## Run

Launch on Linux(Python 3) or Windows:

```bash
$ python script.py
```

You will see:
```
$ Enter your url address:https://bit.ly/3E7rHjX
```

Enter either an url you want to be short or your `bit.ly` link to get clicks number 

You will see:
```
Enter your url address: https://bit.ly/3E7rHjX
Total clicks on https://bit.ly/3E7rHjX is 2
```


