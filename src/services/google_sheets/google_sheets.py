import gspread
import logging
from oauth2client.service_account import ServiceAccountCredentials

from src.data_store import schemas as sch
from src.utils.utils import google_sheet_to_dataframe
from src.utils.settings import GOOGLE_CRED, CLIMBING_SHEET_ID

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s', )


class GoogleSheets(object):

    def __init__(self, locations):
        self.google_cred = GOOGLE_CRED
        self.locations = locations

    def _connect(self, key, tab=0, retry=True):
        """
        Connects to a Google sheet by key.
        """

        sheet = None
        if retry is True:
            try:
                scope = ['https://spreadsheets.google.com/feeds']
                cred = ServiceAccountCredentials.from_json_keyfile_name(self.google_cred, scope)
                gc = gspread.authorize(cred)

                # open spreadsheet of interest
                doc = gc.open_by_key(key)
                sheet = doc.get_worksheet(tab)
            except gspread.exceptions.APIError as exc:
                logging.warning(exc)
                return self._connect(key, tab=tab, retry=False)

            if sheet is None:
                return self._connect(key, tab=tab, retry=False)

        return sheet

    def connect_to_google_sheet_by_location(self, location):
        """
        Return Google sheet data by location

        :param location: {str}
        :return: {str}
        """

        state = self.locations.query_location_by_name(location_name=location, query_type='state')[sch.state_col]
        tab = '1537329742'  # todo here
        return tab
