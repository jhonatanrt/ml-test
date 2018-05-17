from __future__ import print_function

import json
import base64

print('loading function ...')

def lambda_handler(event, context):
    # result = serialize.decode('base64')
    # print('value', result)
    print('value 1 = ' + event.get('key1'))
    print('value 2 = ' + event.get('key2'))
    print('value 3 = ' + event.get('key3'))
    # print('encode' + str(base64.b64encode(bytes('your string', 'utf-8'))))
    return event.get('key1')

if __name__ == '__main__':
    class Event:
        def get(self, key):
            e = {
                'key1': 'value1',
                'key2': 'value2',
                'key3': 'value3',
            }
            return e[key]
    context = 'context'
    event = Event()

print(lambda_handler(event, context))

            
