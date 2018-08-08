#!/usr/bin/env python
import os
from flask_script import Manager

from app import index

app = index()
app.config.from_object(os.environ['APP_SETTINGS'])
print(app.config)
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
