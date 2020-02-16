"""
find the ip count from the weblog
"""
import re

def getip(filename):
    ip = dict()
    with open(filename,'r') as fileobj:
        for line in fileobj:
            # print(line)
            ip_match = re.search('\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}',line)
            if ip_match:
                if ip_match.group() in ip:
                    ip[ip_match.group()] += 1
                else:
                     ip[ip_match.group()] = 1
        return ip

filename = "weblog.log"
ip_with_count = getip(filename)
print(ip_with_count)