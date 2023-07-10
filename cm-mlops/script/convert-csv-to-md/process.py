import pandas as pd
import sys

csv_file = sys.argv[1] if len(sys.argv) > 1 else "summary.csv"
md_file = sys.argv[2] if len(sys.argv) > 2 else "converted.md"

df=pd.read_csv(csv_file, engine='python')

with open(md_file, "w") as md:
  df.to_markdown(buf=md)
