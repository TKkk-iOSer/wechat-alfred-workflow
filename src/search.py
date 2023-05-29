# -*- coding:utf-8 -*-
import json,sys,os
from workflow import Workflow
import web

def main(wf):
    query = sys.argv[1]
    baseUrl = os.getenv('baseUrl')
    url = baseUrl + 'user?keyword=' 
    try:
        userList = web.get(url)
        userList = wf.filter(query, userList, key = lambda d: d['title'], min_score=20)
        if len(userList) > 0:
            for item in userList:
                title = item['title']
                subtitle = item['subTitle']
                icon = item['icon']
                userId = item['userId']
                copyText = item['copyText']
                qlurl = item['url']
                if 'unReadCount' in item:
                    unReadCount = item['unReadCount']
                    if unReadCount > 0:
                     title = title + '      (未读: ' + str(unReadCount) + ')'
                wf.add_item(title=title, subtitle=subtitle, icon=icon, largetext=title, copytext=copyText, quicklookurl=qlurl, arg=userId, valid=True)
        else:
            wf.add_item(title='找不到联系人…',subtitle='请重新输入')
    except IOError:
        wf.add_item(title='请先启动微信 & 登录…',subtitle='并确保安装微信小助手')
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
