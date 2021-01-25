import os
os.environ['CUDA_VISIBLE_DEVICES']="1"
from convlab2.dst.sumbt.multiwoz.sumbt import *
m = SUMBTTracker(arg_path='/fs/startiger0/nmoghe/code/ConvLab-2/convlab2/dst/sumbt/multiwoz/config4.json')
m.train(load_model=True, model_path='/fs/startiger0/nmoghe/code/ConvLab-2/convlab2/dst/sumbt/multiwoz/model_output_mbert_ft_train_zh_few_shot/pytorch_model.bin')
