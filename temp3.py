import os
os.environ['CUDA_VISIBLE_DEVICES']="1"
from convlab2.dst.sumbt.multiwoz.sumbt import *
m = SUMBTTracker(arg_path='/fs/startiger0/nmoghe/code/ConvLab-2/convlab2/dst/sumbt/multiwoz/config1.json')
m.train()
