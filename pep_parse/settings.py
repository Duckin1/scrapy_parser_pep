from pathlib import Path

# Пути
BASE_DIR = Path(__file__).resolve().parent.parent
RESULT_DIR = BASE_DIR / 'results'

# Бот
BOT_NAME = 'pep_parse'

# Домен
PEP_DOMAIN = 'peps.python.org'
ALLOWED_DOMAINS = [PEP_DOMAIN, ]
URLS = [f'https://{PEP_DOMAIN}/']

# Спайдеры
SPIDER_MODULES = [f'{BOT_NAME}.spiders']

# Правила для robots.txt
ROBOTSTXT_OBEY = True

# Настройки для записи в CSV
FEEDS = {
    str(RESULT_DIR / 'pep_%(time)s.csv'): {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}

# Пайплайны
ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}
