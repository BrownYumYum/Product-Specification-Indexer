import argparse,csv
if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('--index',required=True);p.add_argument('--query',required=True);a=p.parse_args()
    with open(a.index,newline='',encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if a.query.upper() in row['model'].upper(): print(row['model'],row['source'])
