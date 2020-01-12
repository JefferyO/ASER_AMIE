import sqlite3
import csv
from relation_senses import relation_senses


def aser2tsv(tsv_path, db_path):
    with open(tsv_path, 'w', newline='') as f:
        conn = sqlite3.connect(db_path)
        tsv_writer = csv.writer(f, delimiter='\t')
        for x in conn.execute('SELECT * FROM RELATIONS;'):
            # 0: _id
            # 1: event1_id
            # 2: event2_id
            # 3-18: relation_senses
            for idx in range(3, 3+14):
                # exclude the Co_Occurrence
                count = int(float(x[idx]) + 0.5)
                row = [x[1], relation_senses[idx-3], x[2]]
                for i in range(count):
                    tsv_writer.writerow(row)
        conn.close()
    return tsv_path
'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--db_path', type=str, help='/path/to/KG.db')
    parser.add_argument('--tsv_path', type=str, help='/path/to/KG.db')
    args = parser.parse_args()
'''
