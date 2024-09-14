#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from lib.log import *
from lib.log_reader import *
from high_stakes.catalog import *
from lib.replay import *

open_log("replay.csv")

log_reader = LogReader("manual.csv")

replay(catalog, log_reader)

close_log()
