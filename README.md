# Subito.it query to pdf

Given one or more Subito.it car research url, generate pdf(s) containing the specs and the photo of the cars in the ads.

*works only for cars*

## Instructions

1. execute (one by one) this commands
```bash
# 1. download this repo
$ git clone https://github.com/marinimau/subito-it_query_to_pdf
# 2. install requirements (globally, venv may have issues with ssl certificates)
$ pip3 install -r requirements.txt
```

2. add your Subito.it car search url in conf.py


if you are on Mac and you get errors regarding ssl certificates try this command:
```
sudo /Applications/Python\ 3.x/Install\ Certificates.command
```

substituting the "x" whit the number of your Python 3 version
