import csv


class Performance_Evaluation_core:

    @staticmethod
    def get_csv_data(csv_path):
        rows = []
        csv_data = open(str(csv_path), "r", encoding="utf8")
        content = csv.reader(csv_data)
        next(content, None)
        for row in content:
            rows.append(row)
        return rows
