from enum import Enum, auto

from .misc.helper import test_reader
from .misc.constants import DATA_FOLDER_PREPROCESSED, DATA_FOLDER

from .AbstractProcessLogReader import AbstractProcessLogReader
import random


class BPIC12LogReader(AbstractProcessLogReader):
    class subsets:
        A = ('A_')
        W = ('W_')
        O = ('O_')
        AW = ('A_', 'W_')
        AO = ('A_', 'O_')
        WO = ('W_', 'O_')
        AWO = ('A_', 'W_', 'O_')

    def __init__(self, **kwargs) -> None:
        self.subset = kwargs.get('subset', BPIC12LogReader.subsets.AW)
        if 'subset' in kwargs:
            del kwargs['subset']
        super().__init__(log_path=DATA_FOLDER / 'dataset_bpic2012_financial_loan/financial_log.xes', csv_path=DATA_FOLDER_PREPROCESSED / 'FinancialLog.csv', **kwargs)

    def preprocess_level_general(self):
        super().preprocess_level_general(remove_cols=[])

    def preprocess_level_specialized(self, **kwargs):
        self.data = self.data[self.data['lifecycle:transition'] == 'COMPLETE']
        self.data = self.data[self.data[self.col_activity_id].str.startswith(self.subset, na=False)]
        super().preprocess_level_specialized(**kwargs)


if __name__ == '__main__':
    reader = BPIC12LogReader()
    print(test_reader(reader, True))
    # reader = reader.init_log(True)
    # reader = reader.init_data()
    # ds_counter = reader.get_dataset()

    # example = next(iter(ds_counter.batch(10)))
    # print(example[0][0].shape)
    # print(example[0][1].shape)
    # reader.viz_bpmn("white")
    # reader.viz_process_map("white")
    # reader.viz_dfg("white")
    # print(reader.get_data_statistics())