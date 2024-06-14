# This version is completed by Yong Zheng(413511280@qq.com), Shuyin Xia?380835019@qq.com?, Xingxin Chen, Junkuan Wang.  2020.5.1

import ctypes
import numpy as np


class ball_k_means:
    def __init__(self, isDouble=0):
        self.isDouble = isDouble

    def fit(self, s1, k, isRing = False, detail = False, random_seed=-1, s2="0"):
        # isRing == 1 represent alg with rings
        # isRing == others represent alg with no rings
        temp = np.loadtxt(s1, dtype=float, delimiter=',')
        lenth = temp.shape[0]
        m = np.linspace(1, lenth, lenth, dtype=int)
        dataptr = m.ctypes.data_as(ctypes.c_char_p)

        if self.isDouble == 1:
            dll = ctypes.cdll.LoadLibrary('.\\ball-k-means\\PythonVersion\\ballXd.dll')
            dataptr = m.ctypes.data_as(ctypes.c_char_p)
            if s2 != '0':
                dll.ball_kmeans_cent.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int,
                                                 ctypes.c_bool, ctypes.c_bool, ctypes.c_char_p)
                dll.ball_kmeans_cent(s1.encode('utf-8'), dataptr, lenth, isRing, detail, s2.encode('utf-8'))
            else:
                dll.ball_kmeans_initk.argtypes = (ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_int,
                                                  ctypes.c_bool, ctypes.c_bool, ctypes.c_int)
                dll.ball_kmeans_initk(s1.encode('utf-8'), k, dataptr, lenth, isRing, detail, random_seed)
        else:
            dll = ctypes.cdll.LoadLibrary('.\\ball-k-means\\PythonVersion\\ballXf.dll')
            dataptr = m.ctypes.data_as(ctypes.c_char_p)
            if s2 != '0':
                dll.ball_kmeans_cent.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int,
                                                 ctypes.c_bool, ctypes.c_bool, ctypes.c_char_p)
                dll.ball_kmeans_cent(s1.encode('utf-8'), dataptr, lenth, isRing, detail, s2.encode('utf-8'))
            else:
                dll.ball_kmeans_initk.argtypes = (ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_int,
                                                  ctypes.c_bool, ctypes.c_bool, ctypes.c_int)
                dll.ball_kmeans_initk(s1.encode('utf-8'), k, dataptr, lenth, isRing, detail, random_seed)
        return m

