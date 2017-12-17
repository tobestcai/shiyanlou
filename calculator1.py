#!/usr/bin/env python3
import sys

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def __get_fileaddress__(self,option):
        try:
            index = self.args(option)
            fileaddress = self.args[index+1]
        except:
            print('Parameter Error')
            exit()
        return fileaddress
    @property
    def get_cfg_add(seif)
        return self.__get_fileaddress__('-c')
    @property
    def get_user_add(self)
        return self.__get_fileaddress__('-d')
    @property
    def get_export_add(self)
        return self.__get_fileaddress__('-0')

args = Args()

class Config(object)
    def __init__(self)
        self
