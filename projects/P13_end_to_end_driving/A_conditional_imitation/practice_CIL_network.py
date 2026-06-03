# ───────────────────────────────────────────────────────────────────────────
# P13-A 실습본 — 실제 논문 코드 기반 (중요 포인트만 비움)
#
# 원본: reference/papers/A_imitation-learning/agents/imitation/
#         imitation_learning_network.py  (Codevilla et al., CIL, arXiv:1710.02410)
# 비운 곳: load_imitation_learning_network() 의
#   STEP 1) conv backbone (conv1은 예시로 남김 — 패턴 보고 conv2~4 채우기)
#   STEP 2) speed(측정값) 처리 + 영상특징과 결합
#   STEP 3) ★분기(branching)★  ← 조건부 모방학습의 핵심
# 비교: 다 채운 뒤 원본과 diff 로 대조해보세요.
# 주의: 원본은 TensorFlow 1.x (tf.contrib 등). 구조 학습이 목적.
# ───────────────────────────────────────────────────────────────────────────
from __future__ import print_function
import numpy as np
import tensorflow as tf


def weight_xavi_init(shape, name):
    return tf.get_variable(name=name, shape=shape,
                           initializer=tf.contrib.layers.xavier_initializer())


def bias_variable(shape, name):
    return tf.Variable(tf.constant(0.1, shape=shape, name=name))


# ── (제공) 네트워크 빌딩블록 — 그대로 사용 (conv/pool/bn/fc/block) ──
class Network(object):
    def __init__(self, dropout, image_shape):
        self._dropout_vec = dropout
        self._count_conv = self._count_pool = self._count_bn = 0
        self._count_activations = self._count_dropouts = self._count_fc = 0
        self._weights = {}; self._features = {}

    def conv(self, x, kernel_size, stride, output_size, padding_in='SAME'):
        self._count_conv += 1
        filters_in = x.get_shape()[-1]
        shape = [kernel_size, kernel_size, filters_in, output_size]
        weights = weight_xavi_init(shape, 'W_c_' + str(self._count_conv))
        bias = bias_variable([output_size], name='B_c_' + str(self._count_conv))
        return tf.add(tf.nn.conv2d(x, weights, [1, stride, stride, 1], padding=padding_in), bias)

    def bn(self, x):
        self._count_bn += 1
        return tf.contrib.layers.batch_norm(x, is_training=False, updates_collections=None,
                                            scope='bn' + str(self._count_bn))

    def activation(self, x):
        self._count_activations += 1
        return tf.nn.relu(x)

    def dropout(self, x):
        self._count_dropouts += 1
        return tf.nn.dropout(x, self._dropout_vec[self._count_dropouts - 1])

    def fc(self, x, output_size):
        self._count_fc += 1
        filters_in = x.get_shape()[-1]
        weights = weight_xavi_init([filters_in, output_size], 'W_f_' + str(self._count_fc))
        bias = bias_variable([output_size], name='B_f_' + str(self._count_fc))
        return tf.nn.xw_plus_b(x, weights, bias)

    def conv_block(self, x, kernel_size, stride, output_size, padding_in='SAME'):
        with tf.name_scope("conv_block" + str(self._count_conv)):
            x = self.conv(x, kernel_size, stride, output_size, padding_in=padding_in)
            x = self.bn(x); x = self.dropout(x)
            return self.activation(x)

    def fc_block(self, x, output_size):
        with tf.name_scope("fc" + str(self._count_fc + 1)):
            x = self.fc(x, output_size); x = self.dropout(x)
            return self.activation(x)


def load_imitation_learning_network(input_image, input_data, input_size, dropout):
    branches = []
    x = input_image
    nm = Network(dropout, tf.shape(x))

    # ── STEP 1. Conv backbone ──
    # conv1 (예시, 제공): (kernel, stride, out) 패턴을 익혀 conv2~4를 직접 채운다.
    xc = nm.conv_block(x,  5, 2, 32, padding_in='VALID')
    xc = nm.conv_block(xc, 3, 1, 32, padding_in='VALID')
    # TODO STEP 1: conv2 = (3,2,64)→(3,1,64),  conv3 = (3,2,128)→(3,1,128),
    #              conv4 = (3,1,256)→(3,1,256)  를 nm.conv_block 으로 이어 붙여라.
    raise NotImplementedError("STEP 1: conv2~conv4 backbone 채우기")

    # reshape → fc1, fc2 (영상 특징)
    x = tf.reshape(xc, [-1, int(np.prod(xc.get_shape()[1:]))], name='reshape')
    x = nm.fc_block(x, 512)
    x = nm.fc_block(x, 512)

    # ── STEP 2. 속도(측정값) 처리 + 결합 ──
    # [할 일]
    #   speed = input_data[1]
    #   speed = nm.fc_block(speed, 128); speed = nm.fc_block(speed, 128)
    #   j = tf.concat([x, speed], 1); j = nm.fc_block(j, 512)
    # TODO STEP 2
    raise NotImplementedError("STEP 2: speed 처리 + joint 결합")

    # ── STEP 3. ★분기(Branching)★ — 조건부 모방학습의 핵심 ──
    # 명령 4종은 (조향,가속,브레이크) 3출력, 마지막 'Speed' 분기는 속도 1출력.
    # 'Speed' 분기는 영상특징 x 만 입력, 나머지는 joint j 입력.
    branch_config = [["Steer", "Gas", "Brake"], ["Steer", "Gas", "Brake"],
                     ["Steer", "Gas", "Brake"], ["Steer", "Gas", "Brake"], ["Speed"]]
    # [할 일] 각 분기마다:
    #   - "Speed" 분기: branch_output = fc_block(x,256) → fc_block(.,256)
    #   - 그 외:        branch_output = fc_block(j,256) → fc_block(.,256)
    #   - branches.append( nm.fc(branch_output, len(branch_config[i])) )
    # TODO STEP 3
    raise NotImplementedError("STEP 3: 명령별 분기 출력 구성")

    return branches
