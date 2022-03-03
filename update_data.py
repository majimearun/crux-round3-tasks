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
    global_ts_url = ts_base_url + "/all?lastdays=all"

    global_ts_update = requests.get(global_ts_url).json()

    global_ts_df = pd.DataFrame(
        global_ts_update, columns=global_ts_update.keys()
    ).transpose()

    country_wise_ts_url = ts_base_url + "?lastdays=all"

    country_wise_ts = requests.get(country_wise_ts_url).json()

    ts_index = [i["country"] for i in country_wise_ts]

    country_confirmed = [i["timeline"]["cases"] for i in country_wise_ts]
    country_recovered = [i["timeline"]["recovered"] for i in country_wise_ts]
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

    country_recovered_df = pd.DataFrame(
        country_recovered, columns=country_recovered[0].keys(), index=ts_index
    )
    country_recovered_df = country_recovered_df.groupby(
        country_recovered_df.index, as_index=True
    ).sum()

    global_ts_df["category"] = global_ts_df.index
    country_recovered_df["country"] = country_recovered_df.index
    country_deaths_df["country"] = country_deaths_df.index
    country_confirmed_df["country"] = country_confirmed_df.index

    if save:

        global_ts_df.to_csv("./task1/data/global_ts.csv", index=False)
        country_confirmed_df.to_csv("./task1/data/country_confirmed.csv", index=False)
        country_deaths_df.to_csv("./task1/data/country_deaths.csv", index=False)
        country_recovered_df.to_csv("./task1/data/country_recovered.csv", index=False)

    return global_ts_df, country_confirmed_df, country_deaths_df, country_recovered_df


if __name__ == "__main__":

    (
        global_ts_df,
        country_confirmed_df,
        country_deaths_df,
        country_recovered_df,
    ) = get_time_series(save=True)
