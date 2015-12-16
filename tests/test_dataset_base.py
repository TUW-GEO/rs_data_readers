from rs_data_readers.dataset_base import DatasetImgBase
import numpy as np
from datetime import datetime
import os


def test_dataset_img_base():
    # init fake img Dataset
    class TestImgDataset(DatasetImgBase):

        def _read_spec_file(self, filename, timestamp, **kwargs):
            return {'test': np.arange(50)}, {'filename': filename}, timestamp, None, None, None

    dataset = TestImgDataset("", filename_templ="test_data_%Y%m%d.dat")
    data, meta, timestamp, lon, lat, time = dataset.read_img(
        datetime(2007, 8, 1))
    assert timestamp == datetime(2007, 8, 1)
    assert meta.keys() == ['filename']
    assert meta['filename'] == "test_data_20070801.dat"


def test_dataset_img_base_subpath():
    # init fake img Dataset
    class TestImgDataset(DatasetImgBase):

        def _read_spec_file(self, filename, timestamp, **kwargs):
            return {'test': np.arange(50)}, {'filename': filename}, timestamp, None, None, None

    dataset = TestImgDataset(
        "", filename_templ="test_data_%Y%m%d.dat", sub_path=["%Y", '%m'])
    data, meta, timestamp, lon, lat, time = dataset.read_img(
        datetime(2007, 8, 1))
    assert timestamp == datetime(2007, 8, 1)
    assert meta.keys() == ['filename']
    assert meta['filename'] == os.path.join(
        "2007", "08", "test_data_20070801.dat")
