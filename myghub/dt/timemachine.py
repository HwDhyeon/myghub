"""Python datetime convertor"""

import datetime


class TimeMachine:
    """Change String to datetime or datetime to String"""

    def __init__(self, dt_format: str = '%Y-%m-%d %H:%M:%S'):
        self.format = dt_format

    def str_to_dt(
        self, dt_str: str, dt_format: str = None
    ) -> datetime.datetime:
        """Change str to datetime

        Args:
            dt_str (str): Datetime str
            dt_format (str, optional):
                Datetime format.
                Defaults to '%Y-%m-%d %H:%M:%S'.

        Returns:
            datetime.datetime: Datetime object
        """

        if dt_format is None:
            dt_format = self.format

        dt_obj = datetime.datetime.strptime(dt_str, dt_format)
        return dt_obj

    def dt_to_str(
        self, dt_obj: datetime.datetime, dt_format: str = None
    ) -> str:
        """Change datetime to str

        Args:
            dt_obj (datetime.datetime): Datetime object
            dt_format (str, optional):
                Datetime format.
                Defaults to '%Y-%m-%dT%H:%M:%SZ'.

        Returns:
            str: Datetime str
        """

        if dt_format is None:
            dt_format = self.format

        dt_str = datetime.datetime.strftime(dt_obj, dt_format)
        return dt_str
