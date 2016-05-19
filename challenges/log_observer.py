import re
from collections import defaultdict


def requests_per_day(log):
    regex_dates = r'\d{4,4}(-\d{2,2}){2,2}'
    matches = re.finditer(regex_dates, log)
    dates = defaultdict(int)
    for match in matches:
        start, end = match.span()
        dates[log[start:end]] += 1
    return dates


def ips_set(log):
    regex_IPs = r'\d{1,3}(\.\d{1,3}){3,3}'
    matches = re.finditer(regex_IPs, log)
    IPs = set()
    for match in matches:
        start, end = match.span()
        IPs.add(log[start:end])
    return IPs
