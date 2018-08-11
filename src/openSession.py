# -*- coding:utf-8 -*-
import json,sys,os
from workflow import Workflow, web

reload(sys)
sys.setdefaultencoding('utf-8')

def main(wf):
    baseUrl = os.getenv('baseUrl')
    userId = os.getenv('userId')
    url = baseUrl + 'open-session'
    data = {'userId': userId}
    r = web.post(url=url,data=data)
    r.raise_for_status()
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
