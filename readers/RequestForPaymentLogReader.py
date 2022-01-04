from readers.AbstractProcessLogReader import AbstractProcessLogReader, TaskModes
import tensorflow as tf
import category_encoders as ce
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Trick to assess cols {col:{'n_unique':len(self.data[col].unique()), 'dtype':self.data[col].dtype} for col in self.data.columns}
class RequestForPaymentLogReader(AbstractProcessLogReader):
    def __init__(self, **kwargs) -> None:
        super().__init__(log_path='data/dataset_bpic2020_tu_travel/RequestForPayment.xes', csv_path='data/RequestForPayment.csv', **kwargs)

    def preprocess_level_general(self):
        super().preprocess_level_general(remove_cols=[
            "case:Cost Type",
            'case:Rfp_id',
            'id',
            'case:Project',
            'case:RfpNumber',
        ])

    def preprocess_level_specialized(self, **kwargs):
        self.data[self.col_activity_id] = self.data[self.col_activity_id].replace(
            'Request For Payment ',
            '',
            regex=True,
        ).replace(
            ' ',
            '_',
            regex=True,
        )
        self.data[self.col_case_id] = self.data[self.col_case_id].replace(
            'request for ',
            '',
            regex=True,
        ).replace(
            ' ',
            '_',
            regex=True,
        )


        # cat_encoder = ce.HashingEncoder(verbose=1, return_df=True)
        # cat_encoder = ce.BaseNEncoder(verbose=1, return_df=True, base=1)
        cat_encoder = ce.BaseNEncoder(verbose=1, return_df=True, base=2)
        # cat_encoder = ce.BaseNEncoder(verbose=1, return_df=True, base=3)
        num_encoder = StandardScaler()
        categorical_columns = [
            "case:Task",
            "case:OrganizationalEntity",
            "case:Activity",
            "org:role",
            "org:resource",
        ]

        normalization_columns = [
            "case:RequestedAmount",
        ]

        
        self.data = self.data.join(cat_encoder.fit_transform(self.data[categorical_columns]))
        self.data[normalization_columns] = num_encoder.fit_transform(self.data[normalization_columns])
        self.data = self.data.drop(categorical_columns, axis=1)
        
        self.preprocessors['categoricals'] = cat_encoder
        self.preprocessors['normalized'] = num_encoder
        
        super().preprocess_level_specialized(**kwargs)


if __name__ == '__main__':
    reader = RequestForPaymentLogReader(mode=TaskModes.SIMPLE).init_log(save=True).init_data()
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