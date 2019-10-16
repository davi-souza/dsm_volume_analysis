from src.services.object import Object
from datetime import datetime, timedelta

prefix = '/app/mech4u/src/tests/'
filenames = [
    'part6.stp',
]

for name in filenames:
    antes = datetime.now()
    obj = Object(prefix + name)
    print(obj.get_all_info())
    depois = datetime.now()
    print((depois - antes).total_seconds(), 's')
