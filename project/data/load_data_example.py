"""PEMS-BAY课程数据读取与结构检查示例。

本文件只演示读取、连接和最基本的检查，不包含任何课程项目答案。
"""

from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).resolve().parent


speed = pd.read_csv(DATA_DIR / "pems_bay_speed.csv.gz", parse_dates=["timestamp"])
stations = pd.read_csv(DATA_DIR / "stations.csv", dtype={"sensor_id": "string"})
distances = pd.read_csv(
    DATA_DIR / "sensor_distances.csv.gz",
    dtype={"from_sensor_id": "string", "to_sensor_id": "string"},
)

sensor_columns = speed.columns.drop("timestamp").astype(str)

assert speed["timestamp"].is_monotonic_increasing
assert not speed["timestamp"].duplicated().any()
assert len(sensor_columns) == 325
assert sensor_columns.tolist() == stations.sort_values("sensor_order")["sensor_id"].tolist()
assert set(distances["from_sensor_id"]).issubset(set(sensor_columns))
assert set(distances["to_sensor_id"]).issubset(set(sensor_columns))

print("speed:", speed.shape, speed["timestamp"].min(), speed["timestamp"].max())
print("stations:", stations.shape)
print("distances:", distances.shape)
print("结构检查通过。")
