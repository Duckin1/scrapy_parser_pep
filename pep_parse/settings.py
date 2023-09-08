BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.StatusSummaryPipeline': 300,
}

FEED_FORMAT = 'csv'
FEED_URI = 'results/pep_%Y-%m-%dT%H-%M-%S.csv'
