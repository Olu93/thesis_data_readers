from thesis_data_readers.AbstractProcessLogReader import AbstractProcessLogReader


def test_reader(
        reader: AbstractProcessLogReader,
        recompute_log: bool = True,
        with_viz_bpmn: bool = True,
        with_viz_procmap: bool = True,
        with_viz_dfg: bool = True,
        save_preprocessed: bool = True,
):
    if recompute_log:
        reader = reader.init_log(save_preprocessed)
    reader = reader.init_data()
    ds_counter = reader.get_dataset()
    example = next(iter(ds_counter.batch(10)))
    print(example[0][0].shape)
    print(example[0][1].shape)
    if with_viz_bpmn:
        print("Inititiating BPMN visualization")
        reader.viz_bpmn("white")
    if with_viz_procmap:
        print("Inititiating Process Map visualization")
        reader.viz_process_map("white")
    if with_viz_dfg:
        print("Inititiating DFG visualization")
        reader.viz_dfg("white")
    
    return reader.get_data_statistics()