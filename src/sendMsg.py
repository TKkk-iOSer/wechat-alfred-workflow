# -*- coding:utf-8 -*-
import sys,os
from workflow import Workflow, web

reload(sys)
sys.setdefaultencoding('utf-8')

def main(wf):
    srvId = sys.argv[1]
    userId = os.getenv('userId')
    baseUrl = os.getenv('baseUrl')
    msgContent = wf.stored_data('wechat_send_content')

    url = baseUrl + 'send-message'
    data = {'userId':userId, 'content': msgContent, 'srvId': srvId}
    r = web.post(url=url,data=data)
    r.raise_for_status()
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
