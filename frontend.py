import datetime
import json
import re


def get_times(day, time_span='160000-203000'):
    dt_fmt = '%Y%m%d%H%M%S'
    resp_time_pttrn = re.compile('response-time:([^ ]+)')
    times = []
    f_path = 'response-times/frontend_{}_{}.json'.format(day, time_span)
    with open(f_path) as f:
        for line in f.readlines():
            items = json.loads(line)['items']
            for item in items:
                try:
                    message = item['message']
                except:
                    continue
                if '/healthcheck' in message:
                    continue
                try:
                    resp_time = resp_time_pttrn.findall(message)[0]
                except:
                    continue
                try:
                    if 'ms' in resp_time:
                        time = float(resp_time.strip('ms')) / 1000.0
                    else:
                        time = float(resp_time.strip('s'))
                    time_str = item['date'] + item['time']
                    date_time = datetime.datetime.strptime(time_str, dt_fmt)
                    times.append(('feedId', time, time_str, item, date_time))
                except:
                    continue

    times.sort(key=lambda t: t[2])

    return times


if __name__ == '__main__':
    times = get_times('20161002')
