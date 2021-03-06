from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from scrapy.utils.project import get_project_settings
import scrapy
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from newsquiz.spiders.evnexpress import EvnexpressBusinessSpider, EvnexpressTravelSpider, EvnexpressSportsSpider, EvnexpressLifeSpider
from newsquiz.spiders.urbanisthanoi import UrbanisthanoiArtsCultureSpider, UrbanisthanoiEatDrinkSpider, UrbanisthanoiNewsSpider, UrbanisthanoiSocietySpider,UrbanisthanoiOldHanoiSpider
from newsquiz.spiders.vietnamnews import VietnamnewsPoliticsLawsSpider, VietnamnewsSocietySpider, VietnamnewsEconomySpider, VietnamnewsLifestyleSpider, VietnamnewsSportsSpider, VietnamnewsEnvironmentSpider
from newsquiz.spiders.kpop import KpopSpider

clses = [EvnexpressBusinessSpider, EvnexpressTravelSpider, EvnexpressSportsSpider, EvnexpressLifeSpider, UrbanisthanoiArtsCultureSpider, UrbanisthanoiEatDrinkSpider, UrbanisthanoiNewsSpider, UrbanisthanoiSocietySpider, UrbanisthanoiOldHanoiSpider, VietnamnewsPoliticsLawsSpider, VietnamnewsSocietySpider, VietnamnewsEconomySpider, VietnamnewsLifestyleSpider, VietnamnewsSportsSpider, VietnamnewsEnvironmentSpider, KpopSpider]

configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    for cl in clses:
        yield runner.crawl(cl)
    reactor.stop()

crawl()

def sensor():
    reactor.run()

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',minutes=60*5)
sched.start()

app = Flask(__name__)

@app.route("/home")
def home():
    """ Function for test purposes. """
    return "Welcome Home :) !"

if __name__ == "__main__":
    app.run()