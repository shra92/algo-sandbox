import os
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor, as_completed


class ParseHugeFile():
    def __init__(self):
        self.lines = []

    def generate_huge_file(self):
        with open("huge_file.txt", "w", encoding="utf-8") as f:
            for i in range(1, 100001):
                f.write(f"Logentry_{i}: User action performed successfully at timestamp_{i * 100}\n")

    def run(self):
        futures = []
        with open("huge_file.txt", "r") as f:
            with ThreadPoolExecutor(max_workers=10) as executor:
                for batch in self.read_file_batch(f):
                    futures.append(executor.submit(self.metrics_aggregate, batch))

                for future in as_completed(futures):
                    future.result()

    def read_file_batch(self, file):
        lines = []
        for line in file:
            lines.append(line)
            if len(lines) == 1000:
                yield lines
                lines = []

        if len(lines) > 0:
            yield lines

    def metrics_aggregate(self, lines):
        for line in lines:
            print(f"characters in each line = {len(line)}\n")