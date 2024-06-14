#!/usr/bin/env python3
import sys, tarfile, pandas as pd
import numpy as np

tf = tarfile.open(sys.argv[1])
movie_dfs = []

for member in tf.getmembers():
    if not member.name.startswith("training_set/mv_"):
        continue
    # manually setting integer sizes here (and below) avoids pandas using int64
    # everywhere
    movie_id = np.int16(member.name[len("training_set/mv_") : -4])
    movie_df = pd.read_csv(
        tf.extractfile(member),
        skiprows=1,
        names=["user_id", "rating", "rating_date"],
        parse_dates=["rating_date"],
        dtype={"rating": "int8", "user_id": "int32"},
    )
    movie_df = movie_df.assign(movie_id=movie_id)
    movie_dfs.append(movie_df)

movies_df = pd.concat(movie_dfs)
del movie_dfs  # jettison per-file dfs to free some mem

# sorting helps compression
movies_df = movies_df[["user_id", "rating_date", "rating", "movie_id"]]
movies_df = movies_df.sort_values(list(movies_df.columns))

movies_df.to_parquet("training-set.parquet")
