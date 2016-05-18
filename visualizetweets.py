import argparse

import pandas as pd
import seaborn as sns

parser = argparse.ArgumentParser(description="Visualize your tweets!")
parser.add_argument("-i", "--infile", dest="infile", help="Path to the CSV file with tweets.",
                    required=True)
parser.add_argument("-r", "--resample", dest="resample", help="Resampling method.",
                    default='1T')
parser.add_argument("-q", "--query", dest="query", default='',
                    help="Search query.")
args = parser.parse_args()

data = pd.read_csv(args.infile, parse_dates=['created_at'], index_col='created_at').sort_index()

sns.plt.figure()
if not args.query:
    data.text.notnull().resample(args.resample).sum().plot()
else:
    for term in args.query.split():
        data.text.str.contains(term).resample(args.resample).sum().plot()
sns.plt.savefig("data/tweetviz.pdf")
