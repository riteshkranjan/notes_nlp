import pandas as pd
import tensorflow as tf

CSV_COLUMN_NAMES = ['Apache','EAS_Log','MAL_log','engp01','BlockingSession_Eng','No_of_DB_Process_eng','failure_count','temp_eng','BlockingSession_1','No_of_DB_Process_1','invalidIndex_1','temp_1','BlocingSession_2','No_of_DB_Process_2','invalideIndex_2','temp_2','Species']
SPECIES = ['NoIssue', 'WMFailed', 'WMPartialFailed', 'WLSOverload', 'SiteOverload', 'DBIssue']

def get_input_path():
    train_path = 'predict_fail_processing/training.csv'
    test_path = 'predict_fail_processing/test.csv'
    return train_path, test_path

def load_data(y_name='Species'):
    train_path, test_path = get_input_path()

    train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
    train_x, train_y = train, train.pop(y_name)

    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
    test_x, test_y = test, test.pop(y_name)

    return (train_x, train_y), (test_x, test_y)


def train_input_fn(features, labels, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)
    return dataset


def eval_input_fn(features, labels, batch_size):
    features=dict(features)
    if labels is None:
        inputs = features
    else:
        inputs = (features, labels)

    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)
    return dataset

CSV_TYPES = [[0], [0], [0], [0], [0],[0], [0], [0], [0], [0],[0], [0], [0], [0], [0],[0], [0]]

def _parse_line(line):
    fields = tf.decode_csv(line, record_defaults=CSV_TYPES)
    features = dict(zip(CSV_COLUMN_NAMES, fields))
    label = features.pop('Species')
    return features, label


def csv_input_fn(csv_path, batch_size):
    dataset = tf.data.TextLineDataset(csv_path).skip(1)
    dataset = dataset.map(_parse_line)
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)
    return dataset
