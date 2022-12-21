# stac-index-catalogs

## Introduction

The [STAC Index](https://stacindex.org/) website hosts a lot of geospatial datasets with a [SpatioTemporal Asset Catalog (STAC)](https://stacspec.org/) endpoint. This repo compiles the list of the STAC endpoints as a CSV file, making it easier to find and use geospatial datasets programmatically. The list is updated daily.

A complete list of all STAC endpoints as a JSON file is available [here](https://stacindex.org/api/catalogs).

## Usage

This repo provides the list of STAC endpoints in two formats:

- Tab separated values (TSV) file: [stac_catalogs.tsv](https://github.com/giswqs/stac-index-catalogs/blob/master/stac_catalogs.tsv)
- JSON file: [stac_catalogs.json](https://github.com/giswqs/stac-index-catalogs/blob/master/stac_catalogs.json)

The TSV file can be easily read into a Pandas DataFrame using the following code:

```python
import pandas as pd

url = 'https://github.com/giswqs/stac-index-catalogs/raw/master/stac_catalogs.tsv'
df = pd.read_csv(url, sep='\t')
df.head()
```

## Related Projects

- A list of open datasets on AWS: [aws-open-data](https://github.com/giswqs/aws-open-data)
- A list of open geospatial datasets on AWS: [aws-open-data-geo](https://github.com/giswqs/aws-open-data-geo)
- A list of AWS open geospatial datasets with a STAC endpoint: [aws-open-data-stac](https://github.com/giswqs/aws-open-data-stac)
