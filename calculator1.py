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
    def __init__(self,configfile)
        self.configfile = configfile
        self._config = {}
    def getcon(self):
        with open(self.configfile) as f:
            try:
                for line in f.readlines():
                self.config[line[0]]=float(line[1])
            except:
                print('Parameter Error')
                exit()
    def get_config(self,surance)
        return self._config[surance]
config = Config()

class UserData(object)
    def __init__(self,userdatafile):
        self.userdatafile = userdatafile
        self.userdata = {}
    def getinf(self):
        with open(self.userdatafile) as g:
            try:
                for line in g.readlines():
                self.userdata[line[0]] = float(line[1])
            except:
                print('Parameter Error')
                exit()
    def get_income(self,id)
        return self.userdata[id]
userdata = UserData()




