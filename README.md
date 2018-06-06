# Test-data-amazon

This project will use Amazon Meta-Data Set maintained on the Stanford Network Analysis Project (SNAP) website. This data set is comprised of product and review metadata on 548,552 different products. The data was collected in 2006 by crawling the Amazon website.

This file is saved as the file amazon-meta.txt.

Currently the script to csv analyse the amazon-data.txt file and for each item it saves in the csv file Output.csv (these two files are not present on github because their size is too big to be uploaded here) different properties for each item : its ASIN (The Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by Amazon.com for product identification. You can lookup products by ASIN using following link: https://www.amazon.com/product-reviews/<ASIN>), its title (name of the product), its groupe (type of the product, eg. Book, Movie) and its categorie (eg. SciFi for a book, country for a music).

TODO : compute statistics with these data
