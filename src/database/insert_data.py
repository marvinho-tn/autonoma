from datetime import datetime
from database import session
from models import Data, Source

source = Source(name='source1')
session.add(source)
session.commit()

data = Data(value='123', source=source)
session.add(data)
session.commit()

data = Data(value='456', source=source)
session.add(data)
session.commit()

data = Data(value='789', source=source)
session.add(data)
session.commit()

source = Source(name='source2')
session.add(source)
session.commit()

data = Data(value='012', source=source)
session.add(data)
session.commit()

data = Data(value='345', source=source)
session.add(data)
session.commit()