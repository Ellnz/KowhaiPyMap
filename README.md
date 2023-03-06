# Overview
Objective: to recreate this map of Japan's Cherry Blossom forecast map using the Kowhai species found in Aotearoa New Zealand, along with some additional informative plots. 

![[2023_CherryBlossomsMap.png|600]]

Additional plots could include comparing the flowering-period of kowhai across different years:
![Spaghetti](https://images.squarespace-cdn.com/content/55b6a6dce4b089e11621d3ed/1438044559948-J3FTKF9YR6NNAJWEN0B7/image-asset.jpeg?content-type=image%2Fjpeg)

Or a scatter plot similar to this one:
![Scatter|500](https://ichef.bbci.co.uk/news/640/cpsprodpb/16729/production/_117754919_cherry_v2-nc.png)

## Inat Data
All flowering Sophora observations need a 'flowering' annotation. 


## Export data
To filter by annotation (Plant Phenology = Flowering), go to the Identify page, and use the filters here (enable Research Grade observations). Annotation filters are not available elsewhere. 

Current Query: ``
```
reviewed=any&quality_grade=needs_id%2Cresearch&term_id=12&term_value_id=13&taxon_id=70037&month=7%2C8%2C9%2C10%2C11%2C12&createdDateType=month
```


# Web Scraping
[Web scraping with Pandas](https://www.youtube.com/watch?v=oF-EMiPZQGA)

# Data Preparation
- [ ] Use Pandas to create a new data frame from the spreadsheet data
	- [ ] Remove undesired columns
	- [ ] Properly declare necessary fields.

## Attributes

| name                       | desired format | purpose                                 |
| -------------------------- | -------------- | --------------------------------------- |
| time_observed_at          | datetime       | Initial observation of flowering kowhai |
| quality_grade              | string         | For filtering by grade                  |
| url                        | hyperlink      | For checking data source                |
| latitude                   | float          | Mapping - especially as change can be expected here                                 |
| longitude                  | float          | Mapping                                 |
| positional accuracy        | int            | For scaling loc accuracy                |
| public_positional_accuracy | int            | For scaling loc accuracy                |
| taxon_geoprivacy           | string         | for toggling obscure taxon              |
| coordinates_obscured       | string         | for toggling obscured entries           |
| scientific_name            | string         | labelling/filtering                     |
| common_name                           |         string       |  labelling/filtering                                       |


# Plot data
Time range
Time / latitude


# Spatial Projection
- [ ] plot data spatially
- [ ] perform hull analysis
- [ ] 
