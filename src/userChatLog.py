# -*- coding:utf-8 -*-
import json,sys,os
from workflow import Workflow, web

reload(sys)
sys.setdefaultencoding('utf-8')

def main(wf):
    userId = os.getenv('userId')
    baseUrl = os.getenv('baseUrl')
    url = baseUrl + 'chatlog?userId=' + userId + '&count=45'
    try:
        result = web.get(url=url)
        result.raise_for_status()
        resp = result.text
        userList = json.loads(resp)
        if len(userList) > 0:
            wf.store_data('wechat_send_content',sys.argv[1])
            for item in userList:
                title = item['title']
                subtitle = item['subTitle']
                icon = item['icon']
                userId = item['userId']
                copyText = item['copyText']
                qlurl = item['url']
                srvId = str(item['srvId'])
                titleLen = len(title)
                lineNun = 70
                if titleLen < lineNun:
                    largetext = title
                else:
                    titleArray = []
                    for n in range(titleLen):
                        if n % lineNun == 0:
                            titleArray.append(title[n:n+lineNun])
                    largetext='\n'.join(titleArray)
                wf.add_item(title=title, subtitle=subtitle, icon=icon, valid=True, largetext=largetext, quicklookurl=qlurl, copytext=copyText, arg=srvId)
        else:
            wf.add_item(title='找不到联系人…',subtitle='请重新输入')
    except IOError:
                wf.add_item(title='请先启动微信 & 登录…',subtitle='并确保安装微信小助手')

    wf.send_feedback()
if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
