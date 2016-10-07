import datetime
import json
import logging
import re


def get_times(day, time_span='160000-203000'):
    dt_fmt = '%Y-%m-%d %H:%M:%S.%f'
    feed_pttrn = re.compile('/render/feeds/([^/]+)/posts/page')
    time_pttrn = re.compile('time="([^"]+)"')
    times = []
    f_path = 'response-times/backend_{}_{}.json'.format(day, time_span)
    canceled = 0
    with open(f_path) as f:
        for line in f.readlines():
            items = json.loads(line)['items']
            for item in items:
                try:
                    message = item['message']
                except:
                    continue
                if 'net/http: request canceled' in message:
                    canceled += 1
                    continue
                if ('/healthcheck' in message or
                        'Lista de posts vazia' in message or
                        '400 - body: no such route' in message or
                        'pageNumber invalid param' in message or
                        'Invalid param number' in message or
                        '- statusCode: 404 -' in message):
                    continue
                try:
                    took = item['metadata']['took'][0]
                except Exception as e:
                    logging.error(e)
                    continue
                try:
                    feed = feed_pttrn.findall(message)[0]
                    time_str = time_pttrn.findall(message)[0]
                    date_time = datetime.datetime.strptime(time_str, dt_fmt)
                except:
                    continue
                try:
                    if 'ms' in took:
                        time = float(took.strip('ms')) / 1000.0
                    else:
                        time = float(took.strip('s'))
                    times.append((feed, time, time_str, item, date_time))
                except:
                    continue

    times.sort(key=lambda t: t[2])

    return times, canceled


if __name__ == '__main__':
    times, canceled = get_times('20161002')
