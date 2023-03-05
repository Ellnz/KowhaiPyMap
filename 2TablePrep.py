# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:36:25 2023

@author: EllisNimick
"""
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates
from matplotlib.ticker import AutoMinorLocator
import pandas as pd

# Import raw Inat data
kowhaiRaw = pd.read_csv("observations-300073.csv")
kowhaiRaw.head()


# Subset kowhai data
kowhaiSub = kowhaiRaw.filter(["time_observed_at", "quality_grade", "url", "latitude", "longitude", "positional_accuracy", "public_positional_accuracy","taxon_geoprivacy", "coordinates_obscured", "scientific_name","common_name"], axis=1)
# Format column data types
kowhaiSub['time_observed_at']=kowhaiSub['time_observed_at'].astype('datetime64[ns]') #accounts for null values in date
kowhaiSub["quality_grade"]=kowhaiSub["quality_grade"].astype('string')
kowhaiSub["taxon_geoprivacy"]=kowhaiSub["taxon_geoprivacy"].astype('string')
kowhaiSub["scientific_name"]=kowhaiSub["scientific_name"].astype('string')
kowhaiSub["common_name"]=kowhaiSub["common_name"].astype('string')
#kowhaiSub[""]=kowhaiSub[""].astype('')
kowhaiSub.head()


# for loop
# if common_name = N/A
# use scientific_name

# Select research grade kowhai\
kowhaiRes = kowhaiSub[kowhaiSub['quality_grade'] == "research"]
print(kowhaiRes)







# Basic plots
kowhaiSub.hist('latitude', bins=12, edgecolor="black");

plt.plot( 'latitude', 'time_observed_at', data=kowhaiSub, linestyle='none', marker='o')









# Advance scatter plot
latitude = kowhaiSub["latitude"].values
longitude = kowhaiSub["longitude"].values

SPECIES = kowhaiSub["scientific_name"].values
SPECIES_ = np.unique(SPECIES)

COLORS = ["#1B9E77", "#D95F02", "#7570B3"]

fig, ax = plt.subplots(figsize=(8,8))
for species, color in zip(SPECIES_, COLORS):
    idxs = np.where(SPECIES == species)
    # No legend will be generated if we don't pass label=species
    ax.scatter(
        latitude[idxs], longitude[idxs], label=species,
        s=50, color=color, alpha=0.7
    )
    
ax.legend();


# Advance scatter plot RESEARCH
latitude = kowhaiRes["latitude"].values
longitude = kowhaiRes["longitude"].values
kowhaiRes
SPECIES = kowhaiRes["scientific_name"].values
SPECIES_ = np.unique(SPECIES)

COLORS = ["#1B9E77", "#D95F02", "#7570B3"]

fig, ax = plt.subplots(figsize=(8,8))
for species, color in zip(SPECIES_, COLORS):
    idxs = np.where(SPECIES == species)
    # No legend will be generated if we don't pass label=species
    ax.scatter(
        latitude[idxs], longitude[idxs], label=species,
        s=50, color=color, alpha=0.7
    )
    
ax.legend();