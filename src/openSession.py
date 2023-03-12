# -*- coding:utf-8 -*-
import json,sys,os
from workflow import Workflow
import web

def main(wf):
    srvId = 0
    if len(sys.argv) > 1:
        srvId = sys.argv[1]
        pass
    baseUrl = os.getenv('baseUrl')
    userId = os.getenv('userId')
    url = baseUrl + 'open-session'
    data = {'userId': userId, 'srvId': srvId}
    r = web.post(url=url,data=data)
    r.raise_for_status()
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
