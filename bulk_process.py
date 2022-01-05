# %%
from src.thesis_data_readers import *
from src.thesis_data_readers.misc import constants
from src.thesis_data_readers.misc.helper import test_reader
import itertools as it
import pandas as pd
stats_collector = []

# reader = AbstractProcessLogReader(
#     log_path=constants.DATA_FOLDER / 'dataset_bpic2020_tu_travel/RequestForPayment.xes',
#     csv_path=constants.DATA_FOLDER_PREPROCESSED / 'RequestForPayment.csv',
#     mode=TaskModes.SIMPLE,
# )
# reader = reader.init_log(save=0)
# reader = reader.init_data()
# point = next(reader._generate_examples(DatasetModes.TRAIN))
# mode_combos = list(it.product(ShapeModes, ShapeModes))
# for combo in mode_combos:
#     test_dataset(reader, DatasetModes.TRAIN, *combo)

# print(reader.get_data_statistics())
# %% -------------------------------------------------------------------------------
reader = BPIC12LogReader()
stats_collector.append(test_reader(reader, True))
# %% -------------------------------------------------------------------------------
reader = DomesticDeclarationsLogReader()
stats_collector.append(test_reader(reader, True))
# %% -------------------------------------------------------------------------------
reader = HospitalLogReader()
stats_collector.append(test_reader(reader, True))
# %% -------------------------------------------------------------------------------
reader = PermitLogReader()
stats_collector.append(test_reader(reader, True))
# %% -------------------------------------------------------------------------------
reader = RabobankTicketsLogReader()
stats_collector.append(test_reader(reader, True))
# %% -------------------------------------------------------------------------------
reader = RequestForPaymentLogReader()
stats_collector.append(test_reader(reader, True))
# %% -------------------------------------------------------------------------------
reader = SepsisLogReader()
stats_collector.append(test_reader(reader, True))
# %% -------------------------------------------------------------------------------
reader = VolvoIncidentsReader()
stats_collector.append(test_reader(reader, True))

# %%
pd.DataFrame(stats_collector).set_index("class_name")