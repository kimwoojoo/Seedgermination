# -*- coding: utf-8 -*-
"""Inception v3 architecture 모델을 retraining한 모델을 이용해서 이미지에 대한 추론(inference)을 진행하는 예제"""

import numpy as np
import tensorflow as tf
import json

imagePath = 'C:/tmp/test.jpg'                                      # 추론을 진행할 이미지 경로
modelFullPath = 'C:/tmp/output_graph.pb'                                      # 읽어들일 graph 파일 경로
labelsFullPath = 'C:/tmp/output_labels.txt'                                   # 읽어들일 labels 파일 경로

def create_graph():
    """저장된(saved) GraphDef 파일로부터 graph를 생성하고 saver를 반환한다."""
    # 저장된(saved) graph_def.pb로부터 graph를 생성한다.
    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')


def run_inference_on_image(imgaePath):
    answer = None

    if not tf.gfile.Exists(imgaePath):
        tf.logging.fatal('File does not exist %s', imgaePath)
        return answer
    image_data = tf.gfile.FastGFile(imgaePath, 'rb').read()
    # 저장된(saved) GraphDef 파일로부터 graph를 생성한다.
    create_graph()
    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-5:][::-1]  # 가장 높은 확률을 가진 5개(top 5)의 예측값(predictions)을 얻는다.

        with open(labelsFullPath, 'rb') as getlabel:
            temps = getlabel.read()

        #label 출력
        labels = str(temps).replace('b\'','').replace('\'','').split("\\n")
        labels.pop()
        DataKey = []
        DataValue = []
        for node_id in top_k:
            human_string = labels[node_id]
            score = str(predictions[node_id])
            human_string = human_string.strip()
            score = score.strip()
            DataKey.append(human_string)
            DataValue.append(score)
            print('%s (score = %s)' % (human_string, score))

        Zip = zip(tuple(DataKey),tuple(DataValue))
        Dict = dict(Zip)
        Return_JsonValue = json.dumps(Dict)
        jsonValue = json.loads(Return_JsonValue)
        returnValue = jsonValue
        print(returnValue)
        return returnValue


if __name__ == '__main__':
    run_inference_on_image()
