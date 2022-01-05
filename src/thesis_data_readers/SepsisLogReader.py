from .misc.helper import test_reader
from .misc.constants import DATA_FOLDER_PREPROCESSED, DATA_FOLDER
from .AbstractProcessLogReader import AbstractProcessLogReader
import pandas as pd


class SepsisLogReader(AbstractProcessLogReader):
    COL_LIFECYCLE = "lifecycle:transition"

    def __init__(self, **kwargs) -> None:
        super().__init__(log_path=DATA_FOLDER / 'dataset_hospital_sepsis/Sepsis Cases - Event Log.xes', csv_path=DATA_FOLDER_PREPROCESSED / 'Sepsis.csv', **kwargs)

    def preprocess_level_general(self):
        super().preprocess_level_general(remove_cols=None)

    def preprocess_level_specialized(self, **kwargs):
        super().preprocess_level_specialized(**kwargs)


if __name__ == '__main__':
    reader = SepsisLogReader()
    reader = reader.init_log(save=1)
    reader = reader.init_data()
    ds_counter = reader.get_dataset()

    example = next(iter(ds_counter.batch(10)))
    print(example[0][0].shape)
    print(example[0][1].shape)
    print(reader.get_data_statistics())
    # print(data.get_example_trace_subset())
    reader.viz_bpmn("white")
    reader.viz_process_map("white")
    reader.viz_dfg("white")