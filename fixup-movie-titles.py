#!/usr/bin/env python3
import sys, re

# parse out the pseudo-csv
LINE_REGEX = re.compile(r"(\d+),(\d+),(.+)$")

# it's not in UTF-8
sys.stdin.reconfigure(encoding="ISO-8859-1")

# add a header
sys.stdout.write("movie-id,year-of-release,title\n")
for original_line in sys.stdin:
    # quote the values in each line
    fixed_line = LINE_REGEX.sub(r'"\1","\2","\3"', original_line)
    sys.stdout.write(fixed_line)
