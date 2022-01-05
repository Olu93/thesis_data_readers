# %%
from src.thesis_data_readers.AbstractProcessLogReader import AbstractProcessLogReader, DatasetModes, ShapeModes, TaskModes, test_dataset
import itertools as it

reader = AbstractProcessLogReader(
    log_path='data/dataset_bpic2020_tu_travel/RequestForPayment.xes',
    csv_path='data/RequestForPayment.csv',
    mode=TaskModes.SIMPLE,
)
reader = reader.init_log(save=0)
reader = reader.init_data()
point = next(reader._generate_examples(DatasetModes.TRAIN))
mode_combos = list(it.product(ShapeModes, ShapeModes))
for combo in mode_combos:
    test_dataset(reader, DatasetModes.TRAIN, *combo)

print(reader.get_data_statistics())
# %%
