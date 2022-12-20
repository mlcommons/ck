#  Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""Example of DNNClassifier for Iris plant dataset.
This example uses APIs in Tensorflow 1.4 or above.
"""

# Converted by Grigori Fursin to the CK format (http://cKnowledge.org)
#   from https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/learn/iris.py

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import os
import json
import numpy as np
import tensorflow as tf

ck_params='ck-params.json'

def main(i):

  mode=i['mode']
  fi=i['input_file']

  # Load input file
  with open(fi) as f:
    s=f.read()
    d = json.loads(s)
    f.close()

  ftable=d['ftable']

  ctable=d.get('ctable',[])
  model_params=d.get('model_params',{})

  fo=d['output_file']
  fod=d['model_dir']

  # Prepare model parametrs
  if mode=='train':
     # Check distinct labels
     labels=[]
     max_label=0
     for q1 in ctable:
         q=q1[0]
         if q not in labels:
            labels.append(q)
            if q>max_label: max_label=q
#     xn_classes=len(labels)
     xn_classes=max_label+1

     xhidden_units=model_params.get('hidden_units',[])
     if len(xhidden_units)==0: xhidden_units=[10, 20, 10]

     feature_length=len(ftable[0])
  else:
     # Read ck-params.json
     x=os.path.join(fod, ck_params)

     with open(x) as f:
       s=f.read()
       dx = json.loads(s)
       f.close()

     xn_classes=dx['n_classes']
     feature_length=dx['feature_length']
     xhidden_units=dx['hidden_units']

  # Prepare model
  # Specify that all features have real-value data
  feature_columns = [tf.feature_column.numeric_column("x", shape=[feature_length])]

  classifier = tf.estimator.LinearClassifier(
                                          feature_columns=feature_columns,
                                          n_classes=xn_classes,
                                          model_dir=fod)

  # Use model
  if mode=='train':
     # Train model.
     print ('')
     print ('Training ...')
     print ('')

     xsteps=model_params.get('training_steps','')
     if xsteps=='' or xsteps==None: xsteps="2000"
     xsteps=int(xsteps)

     train_input_fn = tf.estimator.inputs.numpy_input_fn(
         x={"x": np.array(ftable)},
         y=np.array(ctable),
         num_epochs=None,
         shuffle=True)

     classifier.train(input_fn=train_input_fn, steps=xsteps)

     ftable_test=d.get('ftable_test',[])
     if len(ftable_test)==0: ftable_test=ftable

     ctable_test=d.get('ctable_test',[])
     if len(ctable_test)==0: ctable_test=ctable

     # Define the test inputs
     print ('')
     print ('Testing ...')
     print ('')

     test_input_fn = tf.estimator.inputs.numpy_input_fn(
         x={"x": np.array(ftable_test)},
         y=np.array(ctable_test),
         num_epochs=1,
         shuffle=False)

     # Evaluate accuracy.
     accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]

     print ('')
     print ('Test Accuracy: {0:f}'.format(accuracy_score))
     print ('')

     dd={'output_dir':fod,
         'accuracy':float(accuracy_score),
         'hidden_units':xhidden_units,
         'n_classes':xn_classes,
         'feature_length':feature_length}

     # Record model info
     s=json.dumps(dd,indent=2,sort_keys=True)
     with open(fo,'w') as f:
        f.write(s)
        f.close()

     # Record model info to TF model dir
     x=os.path.join(fod, ck_params)
     with open(x,'w') as f:
        f.write(s)
        f.close()

  ##############################################################################
  elif mode=='prediction':
     # Classify samples
     predict_input_fn = tf.estimator.inputs.numpy_input_fn(
         x={"x": np.array(ftable, dtype=np.float32)},
         num_epochs=1,
         shuffle=False)

     ctable=[]

     print ('')
     print ('Predictions:')

     predictions = list(classifier.predict(input_fn=predict_input_fn))

#     predictions1 = np.squeeze(predictions) # FGG: don't need it - wrong when only one entry

     for q in range(0, len(predictions)):
         print (str(q)+') '+str(np.asscalar(predictions[q]['class_ids'][0])))
         ctable.append(int(np.asscalar(predictions[q]['class_ids'][0])))

     # Record prediction
     dd={'ftable':ftable,
         'ctable':ctable}

     print ('')
     print ('Recording results to '+fo+' ...')
     print ('')

     s=json.dumps(dd,indent=2,sort_keys=True)
     with open(fo,'w') as f:
        f.write(s)
        f.close()

  else:
     print ('Error in CK-TF wrapper: mode "'+mode+'" is not supported ...')
     exit(1)

  return

if __name__ == "__main__":
    argv=sys.argv[1:]

    if len(argv)<2:
       print ('Not enough command line arguments ...')
       exit(1)

    mode=argv[0]
    input_file=argv[1]

    main({'mode':mode, 'input_file':input_file})
