#!/usr/bin/env python3
import os 
import pickle
dummy_info_path = "~/students/2020210972bicheng/spark/_dummy_info.pkl"
dummy_info = pickle.load(open(os.path.expanduser(dummy_info_path), "rb"))
print(dummy_info['factor_selected'])
print(dummy_info['factor_dropped'])
