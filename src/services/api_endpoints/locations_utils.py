from src.data_store import schemas as sch


def set_coordinates_cols():
    """
    Specify the columns to return when retrieve latitude and longitude coordinates from the database

    :return: {list of str}
    """
    return [sch.lat_col, sch.lng_col]


def set_state_cols():
    """
    Specify the columns to return when retrieve latitude and longitude coordinates from the database

    :return: {list of str}
    """
    return [sch.state_col]


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


def retrieve_state(locations_df):
    """
    Return latitude and longitude coordinates from database

    :param locations_df {Pandas dataframe}
    return: {dict}
    """
    return {'state': locations_df.ix[0][sch.state_col]}
