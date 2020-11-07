from datetime import datetime
import json

data = {
    'timestamp': datetime.now(),
    'name': 'fredrik'
}


def convert_dt(value):
    if hasattr(value, 'isoformat'):
        return value.isoformat()
    raise TypeError()


print(json.dumps(data, indent=4, default=convert_dt))
