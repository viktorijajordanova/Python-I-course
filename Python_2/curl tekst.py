import requests

curl -XPOST https://api.twilio.com/2010-04-01/Accounts/AC43c457eee9225fcfb23aed7ccfd542af/Messages.json \
--data-urlencode "To=+38978369330" \
--data-urlencode "From=+17346723629" \
--data-urlencode "MediaUrl=https://demo.twilio.com/owl.png" \
--data-urlencode "Body=Hello from my Twilio line!" \
-u 'AC43c457eee9225fcfb23aed7ccfd542af:eee49d37f8fbe7baf7823666f0df818a'