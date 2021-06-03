# Credits
This webscraper was taken almost verbatim from Fabian Bosler:
https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d

# What does this app do?
This webscraper opens an instance of google chrome and performs an image search for a user provided search criteria.  It then collects the links to the first n number of images returned (n is provided by the user).  Finally it downloads those images to a location specified by the user.

The user parameters are defined in main.py

# Requirements
You'll need the following requests, Pillow, and selenium packages:

```$pip3 install requests Pillow selenium```

You'll also need to install the appropriate chrome driver.  See documentation in the main.py file for clarity.

# How to run
Once all packages are installed and you've updated the parameters in main.py, run main.py:

```$python3 main.py```
