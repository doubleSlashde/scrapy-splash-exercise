# Dynamic website scraping excercise with Scrapy-Splash

This is a Scrapy-Splash project to scrape reviews from Google Maps for some restaurants near our office in Friedrichshafen. 
This project is only meant for educational purposes.

## Running the spider

A running Python and Scrapy installation is mandatory for this project. Additionally, a running Splash container has to be started via Docker before running the example. Therefore, a valid Docker installation is required for running the exercise.

In case there is no Docker installation running on your machine, get it ([here](https://docs.docker.com/docker-for-windows/install)).  

First, pull the Docker image

    $ docker pull scrapinghub/splash
  
Then run the Docker container on port 8050
    
    $ docker run -it -p 8050:8050 scrapinghub/splash

For running the spider, enter the following command in your CLI:
    
    $ scrapy crawl places_review_spider -o reviews.json
