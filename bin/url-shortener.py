#!/usr/bin/env python3

from url_shortener import app
from url_shortener.config import LISTEN_PORT, LISTEN_HOST
app.run(debug=True, port=LISTEN_PORT, host=LISTEN_HOST)
