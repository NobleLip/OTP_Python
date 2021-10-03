import random
import time

Special = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
random.seed('YourPassWord'+str(time.time())[:9])

OTP_PASS = ''

for i in range(6):
	OTP_PASS += Special[random.randint(0,len(Special)-1)]

print(OTP_PASS)