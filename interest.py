from datetime import datetime
import re

def get_logs():
    #most recent logs are always saved under the same name, the location is changed for the sake of the presentation here. It can be pointed straight to \Documents\Neverwinter Nights\logs\nwclientLog1.txt to always get the latest log.
    with open(r"nwclientLog1.txt", "r") as f:
                log = f.read()
    f.close()
    #"ValidateGFFResource sent by user" is what the client-side logs show when logging in to a server. The last search entry will represent the last login.
    #The logs do not include the year, so current year is assumed.
    try:
        login = datetime.strftime(datetime.now(), "%Y ") + re.findall(r"(?:\bValidateGFFResource sent by user.\n)(?:[^\r\n]+)([A-z]{3} [A-z]{3} [0-9]{2} [0-9]{1}[0-9]{1,2}:[0-9]{2}:[0-9]{2})", log)[-1]
        login = datetime.strptime(login, "%Y %a %b %d %H:%M:%S")
    except:
        login = None
    try:
        #the client-side logs do not capture logging out, so the last log entry has to be used.
        left = datetime.strftime(datetime.now(), "%Y ") + re.findall(r"([A-z]{1,3} [A-z]{1,3} [0-9]{1,2} [0-9]{1,2}[0-9]{1,2}:[0-9]{2}:[0-9]{2})", log)[-1]
        left = datetime.strptime(left, "%Y %a %b %d %H:%M:%S")
    except:
        left = None
    return (login, left)

#login is required or the script has no purpose. If left is not supplied, it takes the current timestamp.
def get_increments(login, left = None):
    if login is None:
        print("Unable to return a result. Please check if your log contains timestamps.")
        return
    if left is None:
        now = datetime.now()
        diff = now - login
    else:
        diff = left - login
    #the interest accumulates every 48 minutes    
    times, remainder = divmod(diff.seconds, 60*48)
    remainder = (60*48) - remainder
    minutes, seconds = divmod(remainder, 60)
    if times == 1:
        print('The interest was accumulated{:2} time, {:02}:{:02} minutes until the next accumulation.'.format(int(times), int(minutes), int(seconds)))
        return 
    else:
        print('The interest was accumulated{:2} times, {:02}:{:02} minutes until the next accumulation.'.format(int(times), int(minutes), int(seconds)))
        return 
    
login, left = get_logs()
get_increments(login)
