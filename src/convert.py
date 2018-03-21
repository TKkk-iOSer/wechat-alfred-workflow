# -*- coding:utf-8 -*-
import sys,os
from workflow import Workflow

reload(sys)
sys.setdefaultencoding('utf-8')

def main(wf):
    userId = os.getenv('userId')
    data = wf.stored_data('wechat_search_user_list')
    for item in data:
        if item['userId'] == userId:
            title = 'To：'+item['title']
            subTitle = item['subTitle']
            icon = item['icon']
            wf.add_item(title=title, subtitle=subTitle, icon=icon, valid=True, arg=sys.argv[1])
    wf.send_feedback()
if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
