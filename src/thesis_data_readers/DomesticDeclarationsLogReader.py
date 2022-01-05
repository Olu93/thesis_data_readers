from .misc.helper import test_reader
from .misc.constants import DATA_FOLDER_PREPROCESSED, DATA_FOLDER
from .AbstractProcessLogReader import AbstractProcessLogReader
import pandas as pd


class DomesticDeclarationsLogReader(AbstractProcessLogReader):
    COL_DECLARATION_NUM = "case:DeclarationNumber"

    def __init__(self, **kwargs) -> None:
        super().__init__(log_path=DATA_FOLDER / 'dataset_bpic2020_tu_travel/DomesticDeclarations.xes', csv_path=DATA_FOLDER_PREPROCESSED / 'DomesticDeclarations.csv', **kwargs)

    def preprocess_level_general(self):
        super().preprocess_level_general(remove_cols=None)

    def preprocess_level_specialized(self, **kwargs):
        self.data[self.col_activity_id] = self.data[self.col_activity_id].replace(
            'Declaration ',
            'DEC',
            regex=True,
        ).replace(
            ' by ',
            ' ',
            regex=True,
        ).replace(
            ' ',
            '_',
            regex=True,
        )
        self.data[self.col_case_id] = self.data[self.col_case_id].replace(
            ' ',
            '_',
            regex=True,
        )
        self.data[DomesticDeclarationsLogReader.COL_DECLARATION_NUM] = self.data[DomesticDeclarationsLogReader.COL_DECLARATION_NUM].replace(
            'declaration number ',
            'no_',
            regex=True,
        )
        super().preprocess_level_specialized(**kwargs)


if __name__ == '__main__':
    reader = DomesticDeclarationsLogReader()
    print(test_reader(reader, True))
