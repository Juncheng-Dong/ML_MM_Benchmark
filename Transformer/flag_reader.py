"""
This file serves to hold helper functions that is related to the "Flag" object which contains
all the parameters during training and inference
"""
# Built-in
import argparse
import pickle
import os

from torch.nn.modules.linear import Linear
# Libs

# Own module
from parameters import *

# Torch

def read_flag():
    """
    This function is to write the read the flags from a parameter file and put them in formats
    :return: flags: a struct where all the input params are stored
    """
    parser = argparse.ArgumentParser()
    # Data_Set parameter
    parser.add_argument('--data-set', default=DATA_SET, type=str, help='which data set you are chosing')
    parser.add_argument('--test-ratio', default=TEST_RATIO, type=float, help='the ratio of the test set')
    parser.add_argument('--dim-G', default=DIM_G, type=int, help='the dimension of G')
    parser.add_argument('--dim-S', default=DIM_S, type=int, help='the dimension of S')
    # Transformer specific parameter
    parser.add_argument('--feature-channel-num', default=FEATURE_CHANNEL_NUM, type=int, help='the number of channels for feature')
    parser.add_argument('--nhead-encoder', default=NHEAD_ENCODER, type=int, help='the number of attention head of encoder')
    parser.add_argument('--dim-fc-encoder', default=DIM_FC_ENCODER, type=int, help='the dim of FC layer in encoder')
    parser.add_argument('--num-encoder-layer', default=NUM_ENCODER_LAYER, type=int, help='the number of encoder layers')
    parser.add_argument('--head-linear', default=HEAD_LINEAR, type=list, help='the fully connected layers that is at the start (head)')
    parser.add_argument('--tail-linear', default=TAIL_LINEAR, type=list, help='the fully connected layers that is at the end (TAIL)')
    parser.add_argument('--sequence-length', default=SEQUENCE_LENGTH, type=int, help='the length of the geometry sequence')
    
    # Optimizer specific parameter
    parser.add_argument('--optim', default=OPTIM, type=str, help='the type of optimizer that you want to use')
    parser.add_argument('--reg-scale', type=float, default=REG_SCALE, help='#scale for regularization of dense layers')
    parser.add_argument('--batch-size', default=BATCH_SIZE, type=int, help='batch size (100)')
    parser.add_argument('--eval-step', default=EVAL_STEP, type=int, help='# steps between evaluations')
    parser.add_argument('--train-step', default=TRAIN_STEP, type=int, help='# steps to train on the dataSet')
    parser.add_argument('--lr', default=LEARN_RATE, type=float, help='learning rate')
    parser.add_argument('--lr-scheduler', default=LR_SCHEDULER, type=str, help='learning rate scheduler, there are two choices available, either reducePlateau or warm_restart')
    parser.add_argument('--warm-restart-T-0', default=WARM_RESTART_T_0, type=int,
                        help='the starting epoch of warm restart')
    parser.add_argument('--lr-decay-rate', default=LR_DECAY_RATE, type=float,
                        help='decay learn rate by multiplying this factor')
    parser.add_argument('--stop_threshold', default=STOP_THRESHOLD, type=float,
                        help='The threshold below which training should stop')
    # Data Specific params
    parser.add_argument('--model-name', default=MODEL_NAME, type=str, help='name of the model')
    parser.add_argument('--data-dir', default=DATA_DIR, type=str, help='data directory')
    parser.add_argument('--normalize-input', default=NORMALIZE_INPUT, type=bool,
                        help='whether we should normalize the input or not')
    # Running specific params
    parser.add_argument('--eval-model', default=EVAL_MODEL, type=str, help='the folder name of the model that you want to evaluate')
    parser.add_argument('--use-cpu-only', type=bool, default=USE_CPU_ONLY, help='The boolean flag that indicate use CPU only')
    flags = parser.parse_args()  # This is for command line version of the code
    # flags = parser.parse_args(args = [])#This is for jupyter notebook version of the code
    # flagsVar = vars(flags)
    return flags

