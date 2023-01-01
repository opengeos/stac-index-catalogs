# stac-index-catalogs

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/stac-index-catalogs/blob/master/stac_catalogs.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/stac-index-catalogs/HEAD?labpath=stac_catalogs.ipynb)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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
- A list of open geospatial datasets on AWS with a STAC endpoint: [aws-open-data-stac](https://github.com/giswqs/aws-open-data-stac)
- A list of STAC endpoints from stacindex.org: [stac-index-catalogs](https://github.com/giswqs/stac-index-catalogs)
- A list of geospatial datasets on Microsoft Planetary Computer: [Planetary-Computer-Catalog](https://github.com/giswqs/Planetary-Computer-Catalog)
- A list of geospatial datasets on Google Earth Engine: [Earth-Engine-Catalog](https://github.com/giswqs/Earth-Engine-Catalog)
- A list of geospatial datasets on NASA's Common Metadata Repository (CMR): [NASA-CMR-STAC](https://github.com/giswqs/NASA-CMR-STAC)
- A list of geospatial data catalogs: [geospatial-data-catalogs](https://github.com/giswqs/geospatial-data-catalogs)
