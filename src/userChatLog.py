# -*- coding:utf-8 -*-
import json,sys,os
from workflow import Workflow
import web


def main(wf):
    query = sys.argv[1].encode()
    userId = os.getenv('userId')
    baseUrl = os.getenv('baseUrl')
    url = baseUrl + 'chatlog?userId=' + userId + '&count=60'
    try:
        userList = web.get(url=url)
        if len(userList) > 0:
            wf.store_data('wechat_send_content',query)
            for item in userList:
                title = item['title']
                subtitle = item['subTitle']
                icon = item['icon']
                userId = item['userId']
                copyText = item['copyText']
                qlurl = item['url']
                srvId = str(item['srvId'])
                l = len(title)
                lineNun = 70
                # if l < lineNun:
                largetext = title
                # else:
                #     b = []
                #     for n in range(l):
                #         if n % lineNun == 0:
                #             b.append(title[n:n+lineNun])
                #     largetext='\n'.join(b)
                wf.add_item(title=title, subtitle=subtitle, icon=icon, valid=True, largetext=largetext, quicklookurl=qlurl, copytext=copyText, arg=srvId)
        else:
            wf.add_item(title='找不到联系人…',subtitle='请重新输入')
    except IOError:
                wf.add_item(title='请先启动微信 & 登录…',subtitle='并确保安装微信小助手')

    wf.send_feedback()
if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
