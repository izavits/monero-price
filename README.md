# monero-price

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

> Push notifications to your smart phone about monero (XMR) price.

This is a simple example on how to use IFTTT to get push notifications to your smart phone when monero (XMR) price changes according to a given percentage.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)
- [License](#license)


## Install
- Clone the repository and enter the project directory.

- Create your virtual environment and install the required dependencies:

```
virtualenv -p `which python` venv
source venv/bin/activate
pip install requests
``` 

## Usage
You will need to create an account to [IFTTT.com](https://ifttt.com) and then create a new applet.

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

Now edit the `config.json` file and enter the `IFTTT event name` (`xmr_price` for instance) and edit your `IFTTT api key`. You may find these info if you visit this page: [https://ifttt.com/maker_webhooks](https://ifttt.com/maker_webhooks) and click on "Documentation".

Now you are ready to run the example:

```
python xmr.py
```

You will receive an initial notification to your smartphone with the Monero price at that time. If you keep the program running, you will be receiving a notification every time the xmp price changes by the percentage you defined in the `config.json` file.


## Support
If you're having any problem, please raise an issue on GitHub.

## Contributing
PRs accepted. Some general guidelines:

- Write a concise commit message explaining your changes.
- If applies, write more descriptive information in the commit body.
- Refer to the issue/s your pull request fixes (if there are issues in the github repo).
- Write a descriptive pull request title.
- Squash commits when possible.

Before your pull request can be merged, the following conditions must hold:

- All the tests passes (if any).
- The coding style aligns with the project's convention.
- Your changes are confirmed to be working.

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.


## License
The project is licensed under the Apache 2.0 license.
