import requests
import time
import json

with open('./config.json') as f:
    config=json.load(f)

XMR_PRICE_CHANGE_PERCENT=float(config['price_change_percent'])
XMR_API_URL='https://api.coinmarketcap.com/v1/ticker/monero/'
IFTTT_EVENT_NAME=config['ifttt_event_name']
IFTTT_KEY=config['ifttt_key']
IFTTT_WEBHOOK_URL='https://maker.ifttt.com/trigger/'+IFTTT_EVENT_NAME+'/with/key/'+IFTTT_KEY

def get_latest_xmr_price():
    response = requests.get(XMR_API_URL)
    response_json = response.json()
    return float(response_json[0]['price_usd'])

def post_ifttt_webhook(value):
    data = {'value1': value}
    requests.post(IFTTT_WEBHOOK_URL, json=data)

def main():
    latest_xmr_price=get_latest_xmr_price()
    # Send a starting notofication with the current price
    post_ifttt_webhook(latest_xmr_price)
    print 'XMR PRICE: %f' % latest_xmr_price
    
    while True:
        price=get_latest_xmr_price()
        difference=(float(price-latest_xmr_price)/latest_xmr_price)*100
        print 'CURRENT_XMR_PRICE: %f' % price
        print 'DIFFERENCE FROM INITIAL PRICE (percentage): %f' % difference

        # If there's a significant increase or drop, send notification
        if difference>=XMR_PRICE_CHANGE_PERCENT:
            post_ifttt_webhook(price)
            # and reset the latest price
            latest_xmr_price=price

        time.sleep(10 * 60) # sleep for 10 mins
        
if __name__ == '__main__':
    main()
