#coding=utf8
from BeautifulSoup import BeautifulSoup

def parseHTML(HTMLdata):#分析抓取来的选课系统的已修课程页面
    try:
        required_data = [] #分组后的数据。13个一小组(因为13个刚好就是一行数据），很多小组组成一大组。数据都是python标准str类型。

        soup = BeautifulSoup(''.join(HTMLdata))

        required_table = soup.findAll('table', 'table_biankuan')[0] #抽取出必修课的table
        required_raw = required_table.findAll('td', 'td_biaogexian')#从上table中取出所有的tb_biaogexian条目
        required_raw = [unicode(i.p.string or '') for i in required_raw] #把上述条目的数据类型转换为python标准str
        for i in range(len(required_raw)//13): #将required_raw 的数据13个一小组进行划分，并按小组加入required_data中。
            t_tuple = required_raw[i*13:i*13+13]
            required_data.append(t_tuple)
    except IndexError, e:
        return 1


