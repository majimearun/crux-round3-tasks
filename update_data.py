# Imports
import pandas as pd
import requests


base_url = "https://disease.sh/v3/covid-19"


def get_time_series(url=base_url, save=False):
    ts_base_url = url + "/historical"

    country_wise_ts_url = ts_base_url + "?lastdays=all"

    country_wise_ts = requests.get(country_wise_ts_url).json()

    ts_index = [i["country"] for i in country_wise_ts]

    country_confirmed = [i["timeline"]["cases"] for i in country_wise_ts]

    country_confirmed_df = pd.DataFrame(
        country_confirmed, columns=country_confirmed[0].keys(), index=ts_index
    )
    country_confirmed_df = country_confirmed_df.groupby(
        country_confirmed_df.index, as_index=True
    ).sum()

    country_confirmed_df["country"] = country_confirmed_df.index

    if save:
        country_confirmed_df.to_csv("./task1/data/country_confirmed.csv", index=False)

    return country_confirmed_df


if __name__ == "__main__":

    country_confirmed_df = get_time_series(save=True)
