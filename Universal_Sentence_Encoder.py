import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import re
import seaborn as sns

embed = hub.Module('/Users/monk/Desktop/tf_hub')



# Reduce logging output.
tf.logging.set_verbosity(tf.logging.ERROR)

with tf.Session() as session:
    session.run([tf.global_variables_initializer(), tf.tables_initializer()])
    message_embeddings = session.run(embed(["I am a sentence for which I would like to get its embedding."]))
    print(np.array(message_embeddings).tolist())
    
    
