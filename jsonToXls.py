#coding:utf8
import json
import six
import pandas as pd
from collections import defaultdict
import codecs
import xlwt
from _ast import Str
import jieba


def get_data_from_dict(data, result=None):
    i=''
    #如果key不存在，则设置为空
    for key in data:
        if key not in result:
            if (key=="messages" or key=="date"):
                result[key] = []
            #if not result.keys():
               # result[key] = []
            #else:
               # result[key] = len(result[list(result.keys())[0]])*[""]
    #然后分别加入值
    for key in result:
        if key in data:
            if(key == "messages"):
                   # result[key].append("")
                    for str in data[key]:
                       resultStr=list(str.values())[0]
                       # 精确模式
                       seg_list = jieba.cut(resultStr, cut_all=False)
                       result[key].append("/".join(seg_list))
                       #result[key].append(resultStr)
            elif(key == "date"):
                result[key].append(data[key])
            #if(key == "messages"):
                                  # 搜索引擎模式
                 #seg_list = jieba.cut_for_search(data[key]) 
                 # 全模式
                 #seg_list = jieba.cut(data[key], cut_all=True)
            else:
                #result[key].append(data[key])
                result[key].append("")
        else:
            result[key].append("")
    return result

def get_all_child(father_dict, spread_dict=None):
    if spread_dict == None:
        spread_dict = {}
    for key in father_dict:
        if isinstance(father_dict[key], dict):
            spread_dict = get_all_child(father_dict[key], spread_dict)
        else:
            spread_dict[key] = father_dict[key]
    return spread_dict

def conversion(filename,outpath):
    with codecs.open(filename, encoding='utf-8') as fr:
        result = defaultdict(list)
        max_len=0
        writer = pd.ExcelWriter(outpath)
        for line in fr:
            j = json.loads(line)
            #spread_data = get_all_child(j)
            result = get_data_from_dict(j, result)
            #data = pd.DataFrame(result)
            #if(max_len == 0):
            data = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in result.items()]))
            #print(data)
            #else:
               # data2 = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in result.items()]))
            if(max_len == 0):
              data.to_excel(writer,sheet_name='pokemon',encoding="utf8",index=0)     
              writer.save()
            else:
               data.to_excel(writer, sheet_name='pokemon',encoding="utf8",header=False,startrow=max_len+1,index=0)
               writer.save()
            if(len(result['messages'])==0):
                max_len =max_len+1
            else:
                max_len =max_len+ len(result['messages'])
            result=defaultdict(list)
        writer.save()
if __name__ == "__main__":
    conversion("PokemonGo-1-23.json", "pokemon-1-23.xls")
    -213-233
    -192-212
    -171-191
    -150-170
    -129-149
    -108-128
    -87-107
    -66-86
    -45-65
    -24-44
    -1-23
