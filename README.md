# monero-price

> A simple example using IFTTT to get push notifications to your smart phone about monero (XMR) price.


## Install
- Clone the repository and enter the project directory.

- Create your virtual environment and install the required dependencies:

```
virtualenv -p `which python` venv
source venv/bin/activate
pip install requests
``` 

## Run
You will need to create and account to [IFTTT.com](https://ifttt.com) and then create a new applet.

To create a new applet follow these steps:

- Click on the big "this" button
- Search for the `WebHooks` service 
- Give a name to the event, e.g. `xmr_price`
- Select the big "that" button
- Search for the `Notifications` service
- Select "Send a notification from the IFTTT app"
- Change the message to: `The XMR usd price is {{Value1}}`
- Click "Finish"    

Then you need to download the IFTTT app to your smartphone and allow push notifications.

Now edit the `config.json` file and enter the `IFTTT event name` (`xmr_price` for instance) and edit your `IFTTT api key`. You may find those info if you visit this page: [https://ifttt.com/maker_webhooks](https://ifttt.com/maker_webhooks) and click on "Documentation".

Now you are ready to run the example:

```
python xmr.py
```

You will receive an initial notification to your smartphone with the monero price. If you keep the program running, you will be receiving a notification every time the xmp price changes by the percentage you defined in the `config.json` file.


## Support
If you're having any problem, please raise an issue on GitHub.


## License
The project is licensed under the Apache 2.0 license.
