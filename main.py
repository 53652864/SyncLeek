# coding=utf-8

import os
import time
import json
import demjson
import re
from shutil import copyfile


class SyncLeek(object):
    @classmethod
    def SyncStock(cls):
        print("cls method")

    @staticmethod
    def get_stockList_ht(filePath: str)-> list:
        stock_list = []
        with open(filePath, "r") as f:
            lines = f.readlines()
            for line in lines:
                # 通达信会在股票名字前面添加 0 和 1， 0:SZ 1: SH
                if len(line) > 6:                    
                    # 去除空行 回车 空格等
                    stock = re.sub("\s+", "", line)
                    # 2大指数滤过
                    if stock == "1999999":
                        continue
                    if stock == "0399001":
                        continue

                    stock_list.append(stock)
        return stock_list

    @staticmethod
    def AddPrefix(code: str)-> str:
            if code.startswith("0"):
                return "sz" + code[1::]
            elif code.startswith("1"):
                return "sh" + code[1::]


if __name__ == "__main__":
    # SyncLeek.SyncStock()
    # """
    FilePath = "D:\\zd_huatai\\T0002\\blocknew\\ZXG.blk"
    CodeSettingPath = "C:\\Users\\Administrator\\AppData\\Roaming\\Code\\User\\settings.json"
    # 数据备份
    CodeSettingPath_copy = "C:\\Users\\Administrator\\AppData\\Roaming\\Code\\User\\settings_copy.json"
    copyfile(CodeSettingPath, CodeSettingPath_copy)
    stocks = SyncLeek.get_stockList_ht(FilePath)
    if len(stocks) > 0:
        # print(stocks)
        obj = demjson.decode_file(CodeSettingPath)
        # 
        m = map(SyncLeek.AddPrefix, stocks)
        # m = list(m)
        # 添加指数
        m.append("sh000001")
        m.append("sz399001")
        obj["leek-fund.stocks"] = list(m)
        # print(obj)
        # 格式化输出到str
        s = json.dumps(obj, indent=4)
        with open(CodeSettingPath, "w") as f:
            f.write(s)
    
    # 运行vscode
    VsCodeCmd = "D:\\Program Files\\Microsoft VS Code\\Code.exe"
    os.popen(VsCodeCmd)
    time.sleep(1)
    # """

