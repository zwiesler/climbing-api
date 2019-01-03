from src.data_store import schemas as sch

def retrieve_coordinates(locations_df):
    """
    Return latitude and longitude coordinates from database

    :param locations_df {Pandas dataframe}
    return: {dict}
    """
    return {
        'lat': locations_df.ix[0][sch.lat_col],
        'lng': locations_df.ix[0][sch.lng_col]
    }


def retrieve_tab(locations_df):
    """
    Return tab value from database

    :param locations_df: {Pandas dataframe}
    :return: {dict}
    """
    return {'tab': locations_df.ix[0][sch.tab_col]}
