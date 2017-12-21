# -*- coding: utf8 -*-
from __future__ import unicode_literals
import os


def get_root_path():
    """アプリのルートパスを取得する

    :return:
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_data_path():
    """インポートするデータのパスを取得する。

    :return:
    """
    return os.path.join(get_root_path(), 'data')


def to_half_size(ustring):
    """文字列を半角に変換する

    :param ustring:
    :return:
    """
    if not ustring:
        return ustring

    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            # 全角スペース(0x3000)を半角スペース(0x0020)に変換
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if inside_code < 0x0020 or inside_code > 0x7e:
            rstring += uchar
        if inside_code > 0:
            rstring += chr(inside_code)
    return rstring


def to_full_size(ustring):
    """文字列を全角に変換する

    :param ustring:
    :return:
    """
    if not ustring:
        return ustring

    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code < 0x0020 or inside_code > 0x7e:
            rstring += uchar
        if inside_code == 0x0020:
            inside_code = 0x3000
        else:
            inside_code += 0xfee0
        rstring += chr(inside_code)
    return rstring
