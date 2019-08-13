from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from newsquiz.spiders.evnexpress import EvnexpressBusinessSpider, EvnexpressTravelSpider, EvnexpressSportsSpider, EvnexpressLifeSpider
from newsquiz.spiders.urbanisthanoi import UrbanisthanoiArtsCultureSpider, UrbanisthanoiEatDrinkSpider, UrbanisthanoiNewsSpider, UrbanisthanoiSocietySpider,UrbanisthanoiOldHanoiSpider
from newsquiz.spiders.vietnamnews import VietnamnewsPoliticsLawsSpider, VietnamnewsSocietySpider, VietnamnewsEconomySpider, VietnamnewsLifestyleSpider, VietnamnewsSportsSpider, VietnamnewsEnvironmentSpider
from newsquiz.spiders.kpop import KpopSpider

clses = [EvnexpressBusinessSpider, EvnexpressTravelSpider, EvnexpressSportsSpider, EvnexpressLifeSpider, UrbanisthanoiArtsCultureSpider, UrbanisthanoiEatDrinkSpider, UrbanisthanoiNewsSpider, UrbanisthanoiSocietySpider, UrbanisthanoiOldHanoiSpider, VietnamnewsPoliticsLawsSpider, VietnamnewsSocietySpider, VietnamnewsEconomySpider, VietnamnewsLifestyleSpider, VietnamnewsSportsSpider, VietnamnewsEnvironmentSpider, KpopSpider]

process = CrawlerProcess(get_project_settings())
for cl in clses:
    process.crawl(cl)

def sensor():
    process.start()

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