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
                wf.add_item(title=title, subtitle=subtitle, icon=icon, valid=True, largetext=title, quicklookurl=qlurl, copytext=copyText, arg=srvId)
        else:
            wf.add_item(title='找不到联系人…',subtitle='请重新输入')
    except IOError:
                wf.add_item(title='请先启动微信 & 登录…',subtitle='并确保安装微信小助手')

    wf.send_feedback()
if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
