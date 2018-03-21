# -*- coding:utf-8 -*-
import sys,os
from workflow import Workflow, web

reload(sys)
sys.setdefaultencoding('utf-8')

def main(wf):
    msgContent = sys.argv[1]
    userId = os.getenv('userId')
    baseUrl = os.getenv('baseUrl')
    url = baseUrl + 'send-message'
    data = {'userId':userId, 'content': msgContent}
    r = web.post(url=url,data=data)
    r.raise_for_status()
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
