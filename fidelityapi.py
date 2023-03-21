import urllib.parse, re, json, requests
from datetime import datetime
from typing import Optional


class FidelityAPI:
    def __init__(self, symbol: str, start_date: datetime, end_date: datetime, interval: int = 5,
                 extended_hours: bool = False, corp_actions: bool = True, num_days: int = 2, use_cache: bool = True,
                 product_id: str = "oce", callback: str = "Fidelity", uuid: str = "Fidelity",
                 timestamp: str = "start", quote_type: str = "R"):
        self.base_url = "https://fastquote.fidelity.com/service/marketdata/historical/chart/json?"
        self.product_id = product_id
        self.callback = callback
        self.uuid = uuid
        self.timestamp = timestamp
        self.quote_type = quote_type

        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.extended_hours = "Y" if extended_hours else "N"
        self.corp_actions = "Y" if corp_actions else "N"
        self.num_days = num_days
        self.use_cache = "Y" if use_cache else "N"

    def generate_url(self) -> str:
        params = {
            "productid": self.product_id,
            "symbols": self.symbol,
            "startDate": self.format_date(self.start_date),
            "endDate": self.format_date(self.end_date),
            "barWidth": self.interval,
            "extendedHours": self.extended_hours,
            "quoteType": self.quote_type,
            "corpActions": self.corp_actions,
            "timestamp": self.timestamp,
            "numDays": self.num_days,
            "usecache": self.use_cache,
            "callback": self.callback,
            "uuid": self.uuid
        }

        query_string = urllib.parse.urlencode(params)
        return self.base_url + query_string
    def get_day_open(self):
        return self.get_data()["Symbol"][0]["DayOpen"]
    def get_day_low(self):
        return self.get_data()["Symbol"][0]["DayLow"]
    def get_day_high(self):
        return self.get_data()["Symbol"][0]["DayHigh"]
    def get_percent_change(self):
        return self.get_data()["Symbol"][0]["NetChangePercent"]
    def get_dollar_change(self):
        return self.get_data()["Symbol"][0]["NetChange"]
    def get_last_price(self):
        return self.get_data()["Symbol"][0]["LastTrade"]
    def get_last_close(self):
        return self.get_data()["Symbol"][0]["LastClose"]
    def get_data(self):
        s = requests.get(self.generate_url()).text
        return self.extract_json(s)
    def get_bar_record(self):
        data = self.get_data()["Symbol"][0]["BarList"]["BarRecord"]
        rec = {}

        for record in data:
            rec.update({record["lt"]:{"open":record["op"],"close":record["cl"], "high":record["hi"], "low":record["lo"], "volume":record["v"]}})
        return rec
    @staticmethod
    def extract_json(response):
        start = response.find("(") + 1
        end = response.rfind(")")
        json_str = response[start:end]
        return json.loads(json_str)
    @staticmethod
    def format_date(date: datetime) -> str:
        return date.strftime("%Y/%m/%d-%H:%M:%S")
