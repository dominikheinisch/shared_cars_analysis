import pytest
from datetime import datetime, timezone

from utils import load_df


class Test:
    @pytest.fixture(scope='session', autouse=True)
    def df(self):
        return load_df()

    def test_load(self, df):
        pass

    def test_latitude(self, df):
        MIN_LATITUDE = 31.9
        MAX_LATITUDE = 32.2
        assert MIN_LATITUDE < df.latitude.min()
        assert MAX_LATITUDE > df.latitude.max()

    def test_longitude(self, df):
        MIN_LONGITUDE = 34.5
        MAX_LONGITUDE = 35.0
        assert MIN_LONGITUDE < df.longitude.min()
        assert MAX_LONGITUDE > df.longitude.max()

    def test_timestamp(self, df):
        MIN_TIMESTAMP = datetime(2018, 7, 14, tzinfo=timezone.utc)
        MAX_TIMESTAMP = datetime(2020, 2, 26, tzinfo=timezone.utc)
        assert MIN_TIMESTAMP < df.timestamp.min()
        assert MAX_TIMESTAMP > df.timestamp.max()
