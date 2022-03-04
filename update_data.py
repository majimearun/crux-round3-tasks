# Imports
import pandas as pd
import requests


base_url = "https://disease.sh/v3/covid-19"


def get_time_series(url=base_url, save=False):
    """
    Args:
        url (string, optional): common/home part of url used to derive other urls from which we get required information. Defaults to base_url
        save (bool, optional): arg determing whether the content gathered/updated should be saved or not. Defaults to False
    Returns:
        (pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame): 4 timeseries, 1 global (all 3 combined into 1) and 3 country wise (segregated into confirmed, recovered and deaths) respectively
    """
    ts_base_url = url + "/historical"

    country_wise_ts_url = ts_base_url + "?lastdays=all"

    country_wise_ts = requests.get(country_wise_ts_url).json()

    ts_index = [i["country"] for i in country_wise_ts]

    country_confirmed = [i["timeline"]["cases"] for i in country_wise_ts]
    country_deaths = [i["timeline"]["deaths"] for i in country_wise_ts]

    country_confirmed_df = pd.DataFrame(
        country_confirmed, columns=country_confirmed[0].keys(), index=ts_index
    )
    country_confirmed_df = country_confirmed_df.groupby(
        country_confirmed_df.index, as_index=True
    ).sum()

    country_deaths_df = pd.DataFrame(
        country_deaths, columns=country_deaths[0].keys(), index=ts_index
    )
    country_deaths_df = country_deaths_df.groupby(
        country_deaths_df.index, as_index=True
    ).sum()

    country_deaths_df["country"] = country_deaths_df.index
    country_confirmed_df["country"] = country_confirmed_df.index

    if save:
        country_confirmed_df.to_csv("./task1/data/country_confirmed.csv", index=False)
        country_deaths_df.to_csv("./task1/data/country_deaths.csv", index=False)

    return country_confirmed_df, country_deaths_df


if __name__ == "__main__":

    (
        country_confirmed_df,
        country_deaths_df,
    ) = get_time_series(save=True)
