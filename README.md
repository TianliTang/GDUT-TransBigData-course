# GDUT-TransBigData-course

《交通大数据分析与应用》课程第 1—5 次课学生操练代码、数据，以及 PEMS-BAY 课程项目学生任务与数据。

## 内容

- `lessons/lesson-01`—`lessons/lesson-05`：每次课的学生 Notebook、课堂练习数据、数据字典和环境自检脚本。
- `project/task`：PEMS-BAY 课程项目学生版任务书与任务说明（Markdown、DOCX、PDF、PPTX）。
- `project/data`：课程项目学生数据包，包括速度矩阵、检测站信息、距离关系、字段字典、已知数据问题和读取示例。
- `environment/requirements-course.txt`：课程 Notebook 的 Python 依赖版本。

## 使用方式

```bash
python -m venv .venv
source .venv/bin/activate       # Windows：.venv\\Scripts\\activate
python -m pip install -r environment/requirements-course.txt
```

先在相应的 `lessons/lesson-0x` 目录中打开 Notebook，并保持 `data`、`outputs` 与 Notebook 的相对位置不变。项目数据先阅读 `project/data/README_数据说明.md`，再运行 `project/data/load_data_example.py` 检查文件结构。

## 数据边界

PEMS-BAY 课程数据主要记录检测站 5 分钟平均速度、检测站位置和部分站点距离关系。它不包含流量、占有率、事故、天气、施工或控制措施字段，因此不能仅凭这些数据断言拥堵原因、道路容量或管理措施的因果效果。详细字段、时间缺口和 0 值说明见数据包 README 与字段字典。

课程练习数据为教学用模拟数据；项目数据为课程固定学生发布版本。请勿用其他版本替换课程项目数据。

## 发布边界

本仓库只包含学生材料：不含教师演示 Notebook、参考答案、教师评分参考、教师数据审计报告、历史版本和内部 QA 文件。

## 参考来源

PEMS-BAY 数据结构与站点空间文件参照 DCRNN 项目公开资料整理：

- https://github.com/liyaguang/DCRNN
- https://github.com/liyaguang/DCRNN/blob/master/data/sensor_graph/graph_sensor_locations_bay.csv
- https://arxiv.org/abs/1707.01926

