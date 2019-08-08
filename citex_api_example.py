import requests
import hmac
import hashlib
from datetime import datetime
import base64
from urllib.parse import quote


#Please enter the base url first

#And enter access key and secret key if want request private API

base = ''
access_key = 'e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx'   #example
secret_key = 'b0xxxxxx-c6xxxxxx-94xxxxxx-dxxxx'     #example

u = 'api.citex.io'

def get_symbols():
    url = base + '/v1/common/symbols'
    r = requests.get(url)
    detail = r.json()
    return detail
# print(get_symbols())

def get_currencys():
    url = base + '/api/v1/common/currencys'
    r = requests.get(url)
    detail = r.json()
    return detail
# print(get_currencys())

def get_server_time():
    url = base + '/api/v1/common/timestamp'
    r = requests.get(url)
    detail = r.json()
    return detail
# print(get_server_time())

def get_order_book(symbol):
    url = base + '/api/v1/common/snapshot/%s'%symbol
    r = requests.get(url=url)
    detail = r.json()
    return detail
# print(get_order_book('ETH-USDT'))

def get_order_history(id):
    url = base + '/mapi/quot/queryTickTrade'
    r = requests.get(url, params = {'contractId':id})
    detail = r.json()
    return detail
# print(get_order_history(1))

def get_tickers():
    url = base + '/api/v1/common/allticker'
    r = requests.get(url)
    detail = r.json()
    return detail
# print(get_tickers())
#
def get_kline(contract_id, range):
    url = base + '/mapi/quot/queryCandlestick'
    r = requests.get(url, params={'symbol':contract_id, 'range':range})
    detail = r.json()
    return detail
# print(get_kline(1, '60000'))


#Need verification
def createHash(dataJsonStr):
    key = bytes(secret_key, 'utf-8')
    # print(key)
    jsonBytes = bytes(dataJsonStr, 'utf-8')
    # print(jsonBytes)
    hmac_result = hmac.new(key, jsonBytes, hashlib.sha256).digest()
    return base64.b64encode(hmac_result).decode()

def get_balance():
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    # timestamp = '2019-06-20T09%3A38%3A06'
    url = base + '/api/v1/account/balance'
    # print(timestamp)
    dataJsonStr = 'GET\n'+ u +'\n'+ '/v1/account/balance\n'
    add_data = 'AccessKeyId=%s'%access_key + '\n' + 'SignatureMethod=HmacSHA256'+ '\n' + 'SignatureVersion=2'+ '\n' + 'Timestamp=%s'%timestamp

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + add_data.split('\n')[3]
    # print(added_data)
    dataJsonStr = dataJsonStr + added_data
    # print(dataJsonStr)
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    # print(signature)
    r = requests.get(url=url + '?' + added_data + '&' + 'Signature=' + signature)
    # print(url + '?' + added_data + '&' + 'Signature=' + signature)
    detail = r.json()
    return detail
# print(get_balance())


def place_order(contractId, price, quantity, side, orderType):
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))

    # timestamp = '2019-06-20T09%3A38%3A06'
    url = base + '/api/v1/order/orders/place'

    dataJsonStr = 'POST\n'+ u +'\n'+ '/v1/order/orders/place' +'\n'
    add_data = 'AccessKeyId=%s'%access_key + '\n' + 'SignatureMethod=HmacSHA256'+ '\n' + 'SignatureVersion=2'+ '\n' + 'Timestamp=%s'%timestamp

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + add_data.split('\n')[3]
    # print(added_data)
    dataJsonStr = dataJsonStr + added_data
    # print(dataJsonStr)
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    # print(signature)

    data = {"orderType":orderType,"side":side,"quantity":quantity,"price":price,"contractId":contractId,"timeInForce":"1"}
    # print(data)
    r = requests.post(url=url + '?' + added_data + '&' + 'Signature=' + signature, json = data)
    # print(url + '?' + added_data + '&' + 'Signature=' + signature)
    detail = r.json()
    return detail
# print(place_order('134','0.02','1','1','1'))

def cancel_order(contractId, orderId):
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/api/v1/order/orders/cancel'

    dataJsonStr = 'POST\n'+ u +'\n'+ '/v1/order/orders/cancel' +'\n'
    add_data = 'AccessKeyId=%s'%access_key + '\n' + 'SignatureMethod=HmacSHA256'+ '\n' + 'SignatureVersion=2'+ '\n' + 'Timestamp=%s'%timestamp

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + add_data.split('\n')[3]
    # print(added_data)
    dataJsonStr = dataJsonStr + added_data
    # print(dataJsonStr)
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    # print(signature)
    data = {"contractId":contractId,"orderId":orderId}
    r = requests.post(url=url + '?' + added_data + '&' + 'Signature=' + signature, json = data)

    detail = r.json()
    return detail
# print(cancel_order('134', '1564804341159861'))

def list_orders(orderId):
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/api/v1/order/orders/%s'%int(orderId)

    dataJsonStr = 'GET\n'+ u +'\n'+ '/v1/order/orders/%s'%int(orderId) +'\n'
    add_data = 'AccessKeyId=%s'%access_key + '\n' + 'SignatureMethod=HmacSHA256'+ '\n' + 'SignatureVersion=2'+ '\n' + 'Timestamp=%s'%timestamp

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + add_data.split('\n')[3]
    # print(added_data)
    dataJsonStr = dataJsonStr + added_data
    # print(dataJsonStr)
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    # print(signature)
    r = requests.get(url=url + '?' + added_data + '&' + 'Signature=' + signature)
    # print(url + '?' + added_data + '&' + 'Signature=' + signature)
    detail = r.json()
    return detail
# print(list_orders("1564264397180590"))

def open_orders():
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/api/v1/order/list'

    dataJsonStr = 'GET\n'+ u +'\n'+ '/v1/order/list' +'\n'
    add_data = 'AccessKeyId=%s'%access_key + '\n' + 'SignatureMethod=HmacSHA256'+ '\n' + 'SignatureVersion=2'+ '\n' + 'Timestamp=%s'%timestamp

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + add_data.split('\n')[3]
    # print(added_data)
    dataJsonStr = dataJsonStr + added_data
    # print(dataJsonStr)
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    # print(signature)
    r = requests.get(url=url + '?' + added_data + '&' + 'Signature=' + signature)
    # print(url + '?' + added_data + '&' + 'Signature=' + signature)
    detail = r.json()
    return detail
# orders = open_orders()
# print(orders)

def order_history(contractId):
    contId = str(contractId)
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/api/v1/order/%s/history'%contId

    dataJsonStr = 'GET\n'+ u +'\n'+ '/v1/order/%s/history'%contId +'\n'
    add_data = 'AccessKeyId=%s'%access_key + '\n' + 'SignatureMethod=HmacSHA256'+ '\n' + 'SignatureVersion=2'+ '\n' + 'Timestamp=%s'%timestamp

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + add_data.split('\n')[3]
    # print(added_data)
    dataJsonStr = dataJsonStr + added_data
    # print(dataJsonStr)
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    # print(signature)
    r = requests.get(url=url + '?' + added_data + '&' + 'Signature=' + signature)
    # print(url + '?' + added_data + '&' + 'Signature=' + signature)
    detail = r.json()
    return detail
# print(order_history(14))

# if __name__ == '__main__':
#     n = 1
#     while True:
#         po = place_order('98','0.00000999','0.1','1','1')
#         if 'msg' in po and po['msg'] == 'success':
#             print(n, datetime.now())
#             n = n+1

        # print(get_balance())
        # print(datetime.now())
        # time.sleep(0.1)