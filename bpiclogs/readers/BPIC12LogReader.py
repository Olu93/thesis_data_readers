from enum import Enum, auto
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
        super().__init__(log_path ='data/dataset_bpic2012_financial_loan/financial_log.xes', csv_path ='data/financial_log.csv', **kwargs)

    def preprocess_level_general(self):
        super().preprocess_level_general(remove_cols=[])

    def preprocess_level_specialized(self, **kwargs):
        self.data = self.data[self.data['lifecycle:transition']=='COMPLETE']
        self.data = self.data[self.data[self.col_activity_id].str.startswith(self.subset, na=False)]
        super().preprocess_level_specialized(**kwargs)
    
    
if __name__ == '__main__':
    reader = BPIC12LogReader()
    reader = reader.init_log(True)
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