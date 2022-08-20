import os
from typing import List
from dotenv import load_dotenv
from utilities import utils

class TDConnector:
    def __init__(self, ticker_symbols: List[str] = None) -> None:
        self.ticker_symbols = ticker_symbols
        self.td_api_key = None

        def __get_env_vars__(self):
            try:
                self.td_api_key = os.getenv('TD_API_KEY')
            
            except:
                utils.error_msg('Invalid environment variable names')

        __get_env_vars__(self)


    def return_stuff(self):
        return self.td_api_key

    def get_price_history(self):
        pass
