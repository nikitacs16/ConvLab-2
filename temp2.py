import os
os.environ['CUDA_VISIBLE_DEVICES']="0"
from convlab2.dst.sumbt.multiwoz_zh.sumbt import *
m = SUMBTTracker()
m.train()
