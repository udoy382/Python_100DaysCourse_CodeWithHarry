# Creating command line utility in Python


import argparse
import requests


def download_file(url, local_filename):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


parser = argparse.ArgumentParser()

# Add command line arguments ~
parser.add_argument("url", help="Url of the file to downlaod")
parser.add_argument("output", help="by which name do you wnat to save your file")


# Parser the arguments ~
args = parser.parse_args()

# Use the arguments in your code ~
# print(args.url)
# print(args.output)
download_file(args.url, args.output)


# ------------------------------------------------------------------

# How to use this program:

# If we want to use this program we must use command Prompt
# -> Open `CMD`
# -> come to this folder like: `D:` then `cd Python_100DaysCourse_CodeWithHarry`
# -> after all we can type in the cmd `python ThisFileName imgURL OutPut` for example: `python Day85.py https://som.iitkgp.ac.in/images/71stFoundationDay.jpg myimg.jpg`

# ------------------------------------------------------------------
