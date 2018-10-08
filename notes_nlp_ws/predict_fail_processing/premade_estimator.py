
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from predict_fail_processing import prod_data



tf.logging.set_verbosity(tf.logging.DEBUG)
print("started")
(train_x, train_y), (test_x, test_y) = prod_data.load_data()
print("csv file loaded")
my_feature_columns = []
for key in train_x.keys():
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))
print("column prepared")  
classifier = tf.estimator.DNNClassifier(feature_columns=my_feature_columns, hidden_units=[10, 10], n_classes=8)
print("classfier created")
classifier.train(input_fn=lambda:prod_data.train_input_fn(train_x, train_y, 100), steps=1000)
print("model trained")
eval_result = classifier.evaluate(input_fn=lambda:prod_data.eval_input_fn(test_x, test_y, 100))
print("model tested")
print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

       
def predict_fail(argv):
    expected = ['SiteOverload','WLSOverload','WMFailed']
    input = []
    for x in argv.split(","): 
        input.append(int(x))     
    if len(input) < 16:
	    raise ValueError('input size should be less than equal to 16') 
    predict_x = {
    'Apache': [input[0]],
    'EAS_Log': [input[1]],
    'MAL_log': [input[2]],
    'engp01': [input[3]],
    'BlockingSession_Eng': [input[4]],
    'No_of_DB_Process_eng': [input[5]],
    'failure_count': [input[6]],
    'temp_eng': [input[7]],
    'BlockingSession_1': [input[8]],
    'No_of_DB_Process_1': [input[9]],
    'invalidIndex_1': [input[10]],
    'temp_1': [input[11]],
    'BlocingSession_2': [input[12]],
    'No_of_DB_Process_2': [input[13]],
    'invalideIndex_2': [input[14]],
    'temp_2': [input[15]]
    }
   

    predictions = classifier.predict(
        input_fn=lambda:prod_data.eval_input_fn(predict_x,
                                                labels=None,
                                                batch_size=100))
    output_x = ""
    for x in predict_x: 
        output_x = output_x + x + " : " + str(predict_x[x][0]) + ", "

    for pred_dict, expec in zip(predictions, expected):
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]
        return prod_data.SPECIES[class_id], probability, output_x

