```
  ___ _____ ____            ____        _   _                 
 / _ \_   _|  _ \          |  _ \ _   _| |_| |__   ___  _ __  
| | | || | | |_) |         | |_) | | | | __| '_ \ / _ \| '_ \ 
| |_| || | |  __/          |  __/| |_| | |_| | | | (_) | | | |
 \___/ |_| |_|      _____  |_|    \__, |\__|_| |_|\___/|_| |_|
                   |_____|        |___/                       

```

# OTP Password (disposable password)

Today i was signing on Steam and came a cross the SteamGuard system used to secure all the steam accounts , soo i whanted to replicate the same thing as simple as possible, making it possible to share passwords between people the safest way possible.

* How to use:
	* Change 'YourPassWord' to what you whant```py
	random.seed('YourPassWord')
	```
	
	* Done
	
	
The password changes every 10 seconds, making it possible to login it the 6 digit password.
