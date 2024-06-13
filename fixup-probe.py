#!/usr/bin/env python3
import sys, csv

writer = csv.writer(sys.stdout)
writer.writerow(["movie-id", "customer-id"])
for line in sys.stdin:
    stripped = line.strip()
    if stripped.endswith(":"):
        movie_id = int(stripped[:-1])
    else:
        customer_id = int(stripped)
        writer.writerow([movie_id, customer_id])
