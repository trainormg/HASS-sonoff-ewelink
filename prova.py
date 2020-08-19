import sonoff

# from homeassistant.const import (
#     EVENT_HOMEASSISTANT_STOP, CONF_SCAN_INTERVAL,
#     CONF_EMAIL, CONF_PASSWORD, CONF_USERNAME,
#     HTTP_MOVED_PERMANENTLY, HTTP_BAD_REQUEST,
#     HTTP_UNAUTHORIZED, HTTP_NOT_FOUND)


config = sonoff.CONFIG_SCHEMA({sonoff.CONF_EMAIL: "giuseppe.margiotta@gmail.com",
          sonoff.CONF_USERNAME: "giuseppe.margiotta@gmail.com",
          sonoff.CONF_PASSWORD: "4707qmbAWBFG",
          sonoff.CONF_API_REGION: "eu",
          sonoff.CONF_ENTITY_PREFIX: True,
          sonoff.CONF_SCAN_INTERVAL: 60,
          sonoff.CONF_GRACE_PERIOD: 600,
          sonoff.CONF_DEBUG: True,
          })

print(config)

import code
code.interact(local=locals())

s = sonoff.Sonoff({}, config)

r = [
    {'settings': 
        {'opsNotify': 1, 'opsHistory': 1, 'alarmNotify': 1, 'wxAlarmNotify': 0, 'wxOpsNotify': 0, 'wxDoorbellNotify': 0, 'appDoorbellNotify': 1}, 
    'family': {'id': '5e99bc5c422432000831df65', 'index': 0}, 
        'group': '', 'online': True, 'shareUsersInfo': [], 'groups': [], 'devGroups': [], 
    '_id': '5e1238a5cc5b290008443c30', 'name': 'Lavastoviglie', 'type': '10', 'deviceid': '1000645f36', 'apikey': '04fc6d09-dfb0-404c-ab44-0b3652b391e1', 
    'extra': {'extra': {'uiid': 32, 'description': 'WO1881982', 'brandId': '58e5f344baeb368720e25469', 'apmac': 'd0:27:00:c8:bb:bd', 
    'mac': 'd0:27:00:c8:bb:bc', 'ui': '功率检测插座过载告警', 'modelInfo': '5a2e1ae50cf772f92c342ef6', 'model': 'PSC-B67-GL', 
    'manufacturer': '深圳松诺技术有限公司', 'staMac': '80:7D:3A:33:44:F7', 'chipid': '003344F7'}, '_id': '5bf3a8617e41f93e4319616f'}, 
    'createdAt': '2020-01-05T19:27:33.393Z', '__v': 0, 'onlineTime': '2020-08-18T17:50:15.798Z', 'ip': '87.21.227.21', 'location': '', 
    'params': {'init': 1, 'staMac': '80:7D:3A:33:44:F7', 'rssi': -48, 'alarmCValue': [-1, -1], 'alarmVValue': [-1, -1], 
    'switch': 'on', 'voltage': '230.72',
    'oneKwh': 'stop', 'current': '0.00', 'alarmType': 'pcv', 'fwVersion': '3.5.0', 
    'power': '0.00', 'alarmPValue': [-1, -1], 'uiActive': 60, 'version': 8, 'sledOnline': 'on', 'startup': 'stay', 'pulse': 'off', 
    'pulseWidth': 500, 'timeZone': 1, 'endTime': '2020-04-17T16:53:41.006Z', 'startTime': '2020-04-17T15:14:40.186Z', 
    'hundredDaysKwh': 'get', 
    'timers': [{'mId': '339d7983-aef1-4eda-b848-e1b69fe2e5c4', 'type': 'once', 'at': '2020-05-05T22:44:00.514Z', 
    'coolkit_timer_type': 'delay', 'enabled': 1, 'do': {'switch': 'on'}, 'period': '30'}], 'only_device': {'ota': 'success'}, 
    'ssid': 'b7lz7b7', 'bssid': '44:4e:6d:e1:96:54'}, 'offlineTime': '2020-08-16T17:05:35.577Z', 
    'tags': {'m_91e1_gius': 'on', 'disable_timers': []}, 
    'deviceStatus': '', 'sharedTo': [], 'devicekey': 'c4e93882-3a05-455b-81b7-b9f848f5545f', 
    'deviceUrl': 'https://eu-api.coolkit.cc/api/detail/5a2e1ae50cf772f92c342ef6_en.html', 'brandName': 'Sonoff', 'showBrand': True, 
    'brandLogoUrl': 'https://eu-ota.coolkit.cc/logo/m6N8zJB0O3EVvhCei6zCPStFeKYKAzSa.png', 'productModel': 'Pow_R2', 'devConfig': {}, 'uiid': 32}]


