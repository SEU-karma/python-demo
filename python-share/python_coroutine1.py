def consumer():
    r = 'init'
    while True:
        n = yield r
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    print c.send(None)
    # print c.next()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)