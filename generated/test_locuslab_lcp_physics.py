import sys
_module = sys.modules[__name__]
del sys
demo = _module
fixed_joint_demo = _module
grad_demo = _module
encoder = _module
learn_params = _module
run_breakout = _module
inference = _module
lcp_physics = _module
lcp = _module
solvers = _module
dev_pdipm = _module
pdipm = _module
util = _module
physics = _module
bodies = _module
constraints = _module
contacts = _module
engines = _module
forces = _module
utils = _module
world = _module
setup = _module
test_bodies = _module
test_demos = _module
test_hull = _module

from _paritybench_helpers import _mock_config, patch_functional
from unittest.mock import mock_open, MagicMock
from torch.autograd import Function
from torch.nn import Module
import abc, collections, copy, enum, functools, inspect, itertools, logging, math, numbers, numpy, random, re, scipy, string, time, torch, torchaudio, torchtext, torchvision, types, typing, uuid, warnings
import numpy as np
from torch import Tensor
patch_functional()
open = mock_open()
logging = sys = argparse = MagicMock()
ArgumentParser = argparse.ArgumentParser
_global_config = args = argv = cfg = config = params = _mock_config()
argparse.ArgumentParser.return_value.parse_args.return_value = _global_config
sys.argv = _global_config
__version__ = '1.0.0'


import numpy as np


import torch


from torch.nn import MSELoss


from torch.optim import RMSprop


import time


from torch import nn

