import csv
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    data = list(csv.reader(open(csv_file_path)))
    return data
