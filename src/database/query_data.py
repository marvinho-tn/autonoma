from datetime import datetime
from database import session
from models import Data, Source

sources = session.query(Source).all()
for source in sources:
    print(f'Source: {source.name}')
    for data in source.data:
        print(f'  Data: {data.value} - Timestamp: {data.timestamp}')

data = session.query(Data).filter(Data.value == '789').first()
print(f'Data: {data.value} - Source: {data.source.name} - Timestamp: {data.timestamp}')

data = session.query(Data).filter(Data.timestamp > datetime(2023, 1, 1)).all()
for datum in data:
    print(f'Data: {datum.value} - Source: {datum.source.name} - Timestamp: {datum.timestamp}')