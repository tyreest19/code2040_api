import requests
import datetime

def main():
    t = datetime.time(1, 2, 3)
    url = 'http://challenge.code2040.org/api/dating'
    payload = {'token': '6947ddc0354913e7928f75ce2f42e5ed',
                'github': 'https://github.com/tyreest19/code2040_api',
               'datestamp': 5}
    post = requests.post(url,json = payload)
    print(post.content)
    time = time_incrementer(post.content)
    time = time.split(' ')
    time[0] += 'T'
    time[1] +='Z'
    time = ''.join(time)
    print(time)
    url = 'http://challenge.code2040.org/api/dating/validate'
    payload['datestamp'] = str(time)
    post = requests.post(url,json = payload)
    print(post.content)

def time_incrementer(time):
    time = str(time).split('"')
    interval = time[6]
    interval = int(interval[1:6])
    time = str(time[3]).split('T')
    date_and_year = str(time[0]).split('-')
    time = str(time[1]).split(':')
    time[2] = time[2][:-1]
    time = datetime.datetime(int(date_and_year[0]),int(date_and_year[1]),int(date_and_year[2]),
    int(time[0]),int(time[1]),int(time[2]))
    time += datetime.timedelta(seconds=interval)
    return str(time)
if __name__ == '__main__':
    main()

