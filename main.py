import tensorflow as tf 
import keras 
import numpy as np 
import data_pre_process as dpp


data_dir = r'/Users/dangriffith/Library/CloudStorage/OneDrive-CarletonUniversity/Data_Sceince_Seeminar_Project/Price-Forecast-Modeling/Data'

raw_data = dpp.read_data(data_dir)