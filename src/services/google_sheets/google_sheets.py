import gspread
import logging
from oauth2client.service_account import ServiceAccountCredentials

from src.utils.utils import google_sheet_to_dataframe
from src.utils.settings import GOOGLE_CRED, CLIMBING_SHEET_ID
from src.services.google_sheets import google_sheets_utils as gsutils

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s', )


class GoogleSheets(object):

    def __init__(self):
        self.google_cred = GOOGLE_CRED

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
        :return: {JSON}
        """

        sheet = self._connect(key=CLIMBING_SHEET_ID, tab=gsutils.google_sheets_locations_tab_map[location])
        df = google_sheet_to_dataframe(sheet=sheet)
        df = df[gsutils.location_cols]
        return df.to_json(orient='records', date_format='iso')
