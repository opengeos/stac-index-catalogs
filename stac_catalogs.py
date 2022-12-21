import json
import leafmap
import pandas as pd

url = "https://stacindex.org/api/catalogs"
out_file = "stac_catalogs.json"

leafmap.download_file(url, output=out_file, overwrite=True, unzip=False)

with open(out_file) as f:
    datasets = json.load(f)

print(f"Total number of STAC datasets: {len(datasets)}")

df = pd.DataFrame(datasets)
df = df.replace(r'\n',' ', regex=True) 
df['title'] = df['title'].apply(lambda x: x.title() if x[0].islower() else x)
df = df.sort_values(by="title")
df.set_index("title", inplace=True)
df.reset_index(inplace=True)
df.to_csv("stac_catalogs.tsv", index=False, sep="\t")
df.to_json("stac_catalogs.json", orient="records", indent=4)
