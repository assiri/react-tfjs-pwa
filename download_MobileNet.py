import os
import subprocess
from tensorflow.keras import applications


model = applications.mobilenet.MobileNet()
model.save('./mobilenet-model.h5')




p = subprocess.Popen(['tensorflowjs_converter', '--input_format keras', '--output_format=tfjs_graph_model','mobilenet-model.h5','public/model'])



