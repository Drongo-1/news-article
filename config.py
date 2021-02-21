import os

from flask import Config


class Config:

    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'
    # CAT_API_URL='https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    CAT_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'




    class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
