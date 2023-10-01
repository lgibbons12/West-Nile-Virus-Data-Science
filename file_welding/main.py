from welding import count_seat, fips, latlng, phylodiversity, population
import pandas as pd
from monthly_data import final
from hourly_data import extremes
import time_add
df = pd.read_csv("illinois_county_level_data_2018_2022_combine.csv")


def weld_dataframes(df):
    df = count_seat.add_seats(df)
    print("County Seats sucessfully welded")
    print()
    df = latlng.get_latlng(df)
    print("Latitude and Longitude sucessfully welded")
    print()
    df = population.get_population(df)
    print("Population sucessfully welded")
    print()
    df = fips.get_fips(df)
    print("FIPS ID sucessfully welded")
    print()
    df = phylodiversity.get_phylo(df)
    print("Phylodiversity sucessfully welded")
    print()

    return df


df = weld_dataframes(df)

df = time_add.add_time(df)
print("Time successfully welded")
print()

df = final.do(df)
print("Monthly Average Climate Data sucessfully welded")
print()
 

df = extremes.do(df)
print("Hourly Extreme Climate Data sucessfully welded")
print()

df.drop("keys", inplace = True, axis = 1)

df.drop("Keys", inplace = True, axis = 1)
df.to_csv("output.csv", index=False)


