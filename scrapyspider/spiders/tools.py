import re

class tools_spider:
    #去除字符串中的html标签
    def str_tool_html(self,str_html):
        str_tool_html=''.join(str_html)
        str_tool_html=re.sub('<[^<]+?>', '', str_tool_html).replace('\n', '').strip()
        # print(str_tool_html)
        return str_tool_html




