# Public Rest API for Citex (2019-08-16)
# General API Information
* The base endpoint is: **Ask Citex support**.
* The auth key is: **Ask Citex support**.(Must include auth key in headers when request API)
* All endpoints return either a JSON object.
* Any endpoint can return an ERROR; The ERROR can be different. Only the message is successful would be went through:
```javascript
{
  "code": 0,
  "msg": "failed"
}
```
* Specific error codes and messages defined in another document.
* For `GET` endpoints, parameters must be sent as a `query string`.
* For `POST` endpoints, the parameters may be sent as a
  `json format`.
* Parameters may be sent in any order.

# LIMITS
* All API request rate limit is `600 times/min`. It will cause request failed if request more than 600 times/min. `Suggestion:` Every time to request, make sure the response status is success.
* The sum of request per auth key is 600 times/min. In another word, you can request in different IP at same time no more than 600 times per minute.

# OUTLOOK

[Public API Endpoints](#public-api-endpoints)

    1.Fetch contract information
    2.Fetch currency information
    3.Fetch system time
    4.Fetch order book
    5.Fetch quote information
    6.Fetch Candlestick data
    
[Private API Endpoints(need authentication)](#private-api-endpointsneed-authentication)

    1. Fetch Balance
    2. Place order
    3. Cancel order
    4. Fetch order information
    5. Open order information
    6. Fetch user order history based on contract ID
    
[Authentication](#authentication)

    Authentication request steps
    Authentication request process

# Public API Endpoints
## 1. Fetch contract information
* `Request` 

   GET /api/v1/common/symbols
* `Headers` 

   String Authorization : *******************************
   
* `Response` 
```javascript
{
  "code": 0,
  "msg": "success",
  "data": [
             {
                "contractId": 1,
                "symbol": "ETH-BTC",
	            "minOrderAmt":0.001  
                "priceTick": "0.000001",
                "lotSize": "0.001", 
                "takerFeeRatio": "0.002",
                "makerFeeRatio": "0.001",
             }
          ]
}
```
* `contractId`:contract ID
* `symbol`:symbol name
* `priceTick`:min price
* `lotSize`:min quantity
* `minOrderAmt`:min amount
* `takerFeeRatio`:Taker fee
* `makerFeeRatio`:Maker fee

## 2.	Fetch currency information
* `Request` 

   GET /api/v1/common/currencys
* `Headers` 

   String Authorization : *******************************
   
* `Response` 
```javascript
{
  "code": 0,
  "msg": "success",
  "data": [
             {
                "symbol": "ETH",
                "enable": "0",
             }
          ]
}
```
* `symbol`:currency name
* `enable`:0 is open,1 is close status

## 3.	Fetch system time
* `Request` 

   GET /api/v1/common/timestamp

* `Headers` 

   String Authorization : *******************************
   
* `Response` 
```javascript
{
  "code": 0,
  "msg": "success",
  "data": 1525531785618
}
```

## 4.	Fetch order book
* `Request` 

   GET /api/v1/common/snapshot/{symbol}
   
* `Headers` 

    String Authorization : *******************************
    
* `Param` 

   String symbol : ETH-BTC
* `Response` 
```javascript
{
  "code": 0,
  "msg": "success",
  "data": {
             "symbol": "ETH-BTC",
             "bids": [
                        {
                            "price": "0.082541",
                            "quantity": "1.439"
                        }, 
                     ],
             "asks": [
                        {
                            "price": "0.082461",
                            "quantity": "0.08019"
                        },
                     ],

           }

}
```
* `symbol`:symbol name
* `bids`:max 50 bids,price:price,quantity:quantity;bid1 to bid50 prices and quantities.
* `asks`:max 50 asks,price:price,quantity:quantity;ask1 to ask50 prices and quantities.

## 5.	Fetch quote information
* `Request` 

   GET /api/v1/common/allticker
   
* `Headers` 

    String Authorization : *******************************
    
* `Param` 

   (Optional)String symbol : ETH_BTC
    
* `Response` 
```javascript
{
  "code": 0,
  "msg": "success",
  "data": {
             {
                "date": 1564564848944
		        "ticker": [
			                {
				                "symbol": "eth_btc",
				                "high": "0.027637",
				                "vol": "-0.03",
				                "last": "0.027582",
				                "low": "0.027582",
				                "buy": "0.027582",
				                "sell": "0.0292",
				                "change": "0.100"
			                }
		                  ]

             }
          }
}
```
* `symbol`:symbol name

## 6.	Fetch Candlestick data
* `Request` 

   GET /api/v1/common/candlestick
   
* `Headers` 

    String Authorization : *******************************
    
* `Param` 

    String symbol : "eth_btc"
    
    Int type : Not required, default 1(1min). (1,3,5,15,30,60,120,240,360,1440)
    
    Int size : Not required, default 10, no limit
* `Response` 
```javascript
[
    [
        1569551400000, '0.020611', '0.020625', '0.020611', '0.020616', '29.804'
    ]
    ...
]
```
* `type`:candlestick type
* `size`:candlestick sizes you request
* Every list:timestamp, open, high, low, close, volume
* The first record in lists is the most recent data


# Private API Endpoints(need authentication)

## 1. Fetch Balance
* `Request` 

   GET /api/v1/account/balance
   
* `Headers` 

    String Authorization : *******************************

* `Response` 
```javascript
{
    "code": 0,
    "msg": "success",
    "data": [
                {
                    "currencyName": "ETH",
                    "totalBalance": "563.216"
                    "available": "563.216"
                    "frozenForTrade": "0", 
                }
            ]
}
```
* `available`:available balance
* `currencyName`:currency name
* `frozenForTrade`:frozen balance
* `totalBalance`:total balance

## 2.	Place order
* `Request` 

   POST /api/v1/order/orders/place
   
* `Headers` 

    String Authorization : *******************************
    
* `Param` 

    String contractId : "1", contract ID
    
    String side: buy:"1" sell:"-1"
    
    String price
    
    String quantity 
    
    String orderType:limit order:"1",market order:"3"
    
    String timeInForce:"1" 

* `Response` 
```javascript
{"code":0,"msg":"success","data":"156465841561468756"}
```
* `code`:0,order success;Not 0,order failed
* `msg`:0,order ID, or failed reason if order failed

## 3. Cancel order
* `Request` 

   POST /api/v1/order/orders/cancel

* `Headers` 

    String Authorization : *******************************
    
* `Param` 

    String contractId : "1", contract ID
    
    String orderId

* `Response` 
```javascript
{"code":0,"msg":success,”data”:None }
```
* `code`:0,order success;Not 0,order failed
* `msg`:None or failed reason if order failed

## 4. Fetch order information
* `Request` 

   GET /api/v1/order/orders/{orderId}
   
* `Headers` 

    String Authorization : *******************************

* `Response` 
```javascript
{   
    "code": 0,
    "msg":"success"
    "data": [
                {
                    "timestamp": 1525356828303793,
                    "contractId": 1,
                    "symbol": "ETH-BTC",
                    "side": "-1",
                    "price": "0.09",
                    "quantity": "0.001",
                    "orderType": "1",
                    "timeInForce": "1",
                    "orderStatus": "1",
                    "filledQuantity": "1",
                    "makerFeeRatio": "0.001",
                    "takerFeeRatio": "0.001"
                }
            ],
}
```
* `code`:0,order success;Not 0,order failed
* `timestamp`:timestamp
* `contractId`:contract ID
* `symbol`:symbol name
* `side`:side
* `price`:order price, 0 if market order
* `quantity`:order quantity
* `orderType`:order type, 1 limit order, 3 market order
* `orderStatus`:order status,0 is not an order,1 is placing order,2 is open order,3 is part open order,4 is closed order, 5 is part of open order, part of cancel,6 is canceled,7 is canceling,8 is unavailable.
* `filledQuantity`:executed quantity 
* `makerFeeRatio`:maker fee
* `takerFeeRatio`:taker fee

## 5. Open order information
* `Request` 

   GET /api/v1/order/list
 
* `Headers` 

    String Authorization : *******************************

* `Response` 
```javascript
[
    {
        "symbol": "LTC-BTC",
        "orderId": "134584156458", 
        "price": "0.1",
        "quantity": "1.0",
        "executedQty": "0.5",
        "matchStatus": "1",
        "orderType": "1",
        "side": "1",
        "orderTime": 1499827319559,
    }
]

```
* `symbol`:symbol name
* `orderId`:order id
* `price`:order price, 0 is market order
* `quantity`:order quantity
* `executedQty`:executed quantity
* `matchStatus`:order status,0 is not an order,1 is placing order,2 is open order,3 is part open order,4 is closed order, 5 is part of open order, part of cancel,6 is canceled,7 is canceling,8 is unavailable.
* `filledQuantity`:executed quantity .
* `orderType`:1 is limit order, 3 is market order
* `side`: order side
* `orderTime`: order time

## 6. Fetch user order history based on contract ID
* `Request` 

   GET /api/v1/order/{contract_id}/history
   
* `Headers` 

    String Authorization : *******************************

* `Response` 
```javascript
{
    "code": 0,
    "msg": "success",
    "data":
    		[
    		    {
        	        "orderId": "134584156458", 
                    "symbol": "LTC-BTC",
        		    "matchPrice": "0.1",
        		    "matchQty": "1.0",
        		    "fee": "0.5",
        		    "feeCurrency": "BTC",
        		    "matchTime": "15489419849",
        		    "side": "1",
        		    "orderType":”1”,
    		    }
    		]
}
```
* `code`:0,order success;Not 0,order failed
* `orderId`:order id
* `symbol`:symbol name
* `matchPrice`:match price
* `matchQty`:match quantity
* `fee`:fee
* `feeCurrency`: fee currency
* `matchTime`: match time
* `side`: order side
* `orderType`:order type
*  Order history has most recent 200 orders.The first order data is most recent one. 


# Authentication

So far, please contact CITEX workers to apply apiKey and Secret. AccessKey is API KEY, SecretKey is API SECRET KEY. (You will receive them in e-mail after applied successful)
(Warning: API KEY and SECRET is important with your account safety. It is important to keep KEY and Secret confidential: it shouldn't be disclosed to any third party, including CITEX support.).
Authentication request steps:

Base on account safety, API request that needs authentication must have HMAC-SHA256 for authentication. A right request is based on several parts below:

* request url: base url with request name,for example, base + /api/v1/order/orders/15485146161498.

* AcessKeyId: your applied AcessKey in your APIKEY.

* Signature Method: Based on HMAC-SHA256.

* Signature Version: 2

* Timestamp: The timestamp you request time. (UTC time). It helps to avoid third party to modify. For example: 2017-05-11T16:22:06. 

* Required and optional parameters. Every request has its required parameters and optional parameters. You can check the parameters in introduction. Attention: For GET request, every request signature must be generated by HMAC-SHA256 algorithm. For POST request, every request signature don’t need to be generated by HMAC-SHA256 algorithm. The parameters that need to be generated by HMAC-SHA256 algorithm only are AccessKeyId,SignatureMethod,SignatureVersion,Timestamp. Put other parameters in body. Body parameters need to change to json format. 

* Signature: signature is maker sure the data is not modified by third party.

For example:

    base + /api/v1/order/orders/15485146161498?AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&
    SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06&
    Signature=41OKsrDrG%2BizHgziwi00RbXjV3KURYXXp//7HqpciOc%3D
And add auth key in headers. 

## Authentication request process:

1.

    Because different data to generated by HAMC-SHA256 can have different result. First of all, we need to request in right way. Below is an example to check balance request:
        
        base + /api/v1/order/orders/15485146161498?AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&
        SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06&
        Signature=41OKsrDrG%2BizHgziwi00RbXjV3KURYXXp//7HqpciOc%3D
        
    Request method (GET or POST), add \n in the end:

        GET\n

2. 
    add \n after api.citex.io.(Warning: Must use 'api.citex.io', Not the base endpoint that CITEX Support provided)

        api.citex.io\n

3. Request method url, add \n in the end: (Warning: There is no '/api' in the beginning. Start with '/v1/....')

        /v1/order/orders/15485146161498\n

4. Group by parameters by ASCII. (Use UTF-8 encode, and URLENCODE encode, 16 binary character must be capital. For example, ':'will be encode to ‘%3A’. Space will be encode to ‘%20’). For example, original parameters:
        
        AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx
        SignatureMethod=HmacSHA256
        SignatureVersion=2
        Timestamp=2019-06-20T09%3A38%3A06
    After group by parameters:
    
        AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx
        SignatureMethod=HmacSHA256
        SignatureVersion=2
        Timestamp=2019-06-20T09%3A38%3A06
    As the parameters, connect the parameters with ‘&’:
    
        AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&
        SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06

    In the end, the data that need to be calculated is:

        GET\n
        api.citex.io\n
        /v1/order/orders/15485146161498\n
        AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06

5. By using HMAC-SHA256 algorithm, put two parameters in it:

    a.  character string
    
        GET\n
        api.citex.io\n
        /v1/order/orders/15485146161498\n
        AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06
    
    b. Secret Key
    
	    b0xxxxxx-c6xxxxxx-94xxxxxx-dxxxx
	    
    After get calculated result, use Based64 and URLENCODE to encode:
    
    The result would be: 
    
        41OKsrDrG%2BizHgziwi00RbXjV3KURYXXp//7HqpciOc%3D
        
    (attention, must to use Based-64 and URLENCODE to encode). Put the result as signature parameters in your API request.

6. In the end, the request would be:

        base + /api/v1/order/orders/15485146161498?AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&
        SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06&
        Signature=41OKsrDrG%2BizHgziwi00RbXjV3KURYXXp//7HqpciOc%3D
        
    And don't forgot to add auth key in headers.


* Another example:

    By using the parameters above, another request method(balance) to request balance is:
    
       base + /api/v1/account/balance?AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&
       SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06&
       Signature=ydOk2DwcpAcujVnfPmsJDXn8b7Wl9HCDay98Bs82pa0%3D
       
    And don't forgot to add auth key in the headers.
