# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import tushare as ts


s = ts.get_h_data('600848')
print s.index.values    # 获取dataframe索引值