#!/usr/bin/python
# coding:utf-8

import re
from collections import Counter
import time

p = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.*)\] "(.*)" (\d*) \d "(.*)" "(.*)" "(.*)" "(.*)"ms$'
time_format = r'(\d\d):\d\d:\d\d '

top100_urls = {}
url_list = []
hour_dict = {}
ft_dict = {}
with open('/var/log/nginx/access.log', 'r') as f:
    for line in f:
        c = re.compile(p)
        m = c.match(line)
        if not m:
            continue
        groups = m.groups()

        ip = groups[0]
        time_local = groups[1]
        request = groups[2]
        code = groups[3]
        http_referer = groups[4]
        user_agent = groups[5]
        time = float(groups[7])

        top100_urls[request] = time

        url_list.append(request)

        #hour
        match = re.search(time_format, time_local)
        hour = match.groups()[0]
        hour_dict[hour] = hour_dict.get(hour, 0) + 1

        #file type
        ft = request.split()[1].split('.')
        if len(ft) == 2:
            ft_dict[ft[1]] = ft_dict.get(ft[1], 0) + 1

sorted_top100 = sorted(top100_urls.items(), key=lambda x: x[1], reverse=True)
print sorted_top100[:100]

counter = Counter(url_list)
print counter

print hour_dict
print ft_dict
