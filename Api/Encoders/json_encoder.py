import json
from datetime import datetime, date
from json import JSONEncoder

class CustomDatetimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)