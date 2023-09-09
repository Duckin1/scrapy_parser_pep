import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import (BASE_DIR, FILE_NAME, HEADERS_PEP_TABLE,
                                RESULT_DIR, TIME_FORMAT, TOTAL_STATUSES)


class PepParsePipeline:
    """
    Пайплайн для обработки данных и создания сводной таблицы статусов PEP.
    """
    def __init__(self):
        self.status_count = None
        self.results_dir = BASE_DIR / RESULT_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
            self.results_dir / FILE_NAME.format(
                datetime=dt.now().strftime(TIME_FORMAT)
            ),
            mode='w',
            encoding='utf-8'
        ) as file:
            csv.writer(file).writerows([
                HEADERS_PEP_TABLE,
                *(self.status_count.items()),
                [TOTAL_STATUSES, sum(self.status_count.values())]
            ])
