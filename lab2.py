#lab2 = Python HTTP-inspector for several webpages
#using Requests, Python 3.13.12

import requests

#These variables needed in analytics at the end of the program
succesful = 0
http_error = 0
network_error = 0

total_time = []

urls = [
    "https://google.com",
    "https://github.com",
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/404",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/redirect/2"
] #Some of them will have 404 status, 3-second delay etc.

with requests.session() as session: #use the session to make the procedure
    for i in urls: #use 'for' to check each webpage
        try:

            response = session.get(i, timeout=5)
            print('URL: '+str(response.url))
            print('Status code: '+str(response.status_code))
            print('Time: '+str(response.elapsed))
            print('History: '+str(response.history))
            print('')
            print('') #Just for design and good result in Terminal ^_^
            print('')
            if 200 <= response.status_code < 300:
                succesful += 1

            response.raise_for_status()
            total_time.append(response.elapsed.total_seconds())

            #Here is some exceptions: 
        except requests.exceptions.HTTPError as http:
            print(f'Error: {http}')
            http_error += 1

        except requests.exceptions.Timeout:
            network_error += 1

        except requests.exceptions.ConnectionError:
            network_error += 1

        except requests.exceptions.RequestException as e:
            print('Error! Code: '+str(e))

#Analytics process

print('') #Just for design in terminal
print('Conclusion: ')
print(f'Succesful requests: {succesful}')
print(f'Server errors: {http_error}')
print(f'Network errors: {network_error}')
if total_time:
    print(f'Average time: {sum(total_time) / len(total_time)} seconds')
else:
    print('Average time: No succesful requests :(')