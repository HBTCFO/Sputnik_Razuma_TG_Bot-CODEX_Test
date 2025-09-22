import os
import zoneinfo
from datetime import datetime

def now_tz():
    tz = os.getenv("TZ", "Europe/Oslo")
    return datetime.now(zoneinfo.ZoneInfo(tz))
