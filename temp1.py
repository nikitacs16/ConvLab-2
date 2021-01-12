import os
os.environ['CUDA_VISIBLE_DEVICES']="1"
from convlab2.dst.sumbt.multiwoz.sumbt import *
m = SUMBTTracker()
m.train()
