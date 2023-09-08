import csv
import os


class StatusSummaryPipeline:
    def __init__(self):
        self.status_counts = {}
        self.total_count = 0

    def process_item(self, item, spider):
        status = item['status']
        self.status_counts[status] = self.status_counts.get(status, 0) + 1
        self.total_count += 1
        return item

    def close_spider(self, spider):
        output_dir = 'results'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'status_summary_%Y-%m-%dT%H-%M-%S.csv')

        with open(output_path, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            for status, count in self.status_counts.items():
                writer.writerow([status, count])
            writer.writerow(['Total', self.total_count])
