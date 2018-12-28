import pandas as pd


def google_sheet_to_dataframe(sheet, **kwargs):
    """
    Converts a Google Sheet connection object to a pandas dataframe

    Arguments:
        sheet {Google Sheet connection}

    Returns:
        {Pandas dataframe}
    """
    return pd.DataFrame(sheet.get_all_records(**kwargs))
