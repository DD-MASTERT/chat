from chat.baidu import translate_ja_to_zh
from chat.baidut import translate_text
from chat.tenxun import txtra


TXSecretId = ''
TXSecretKey = ''
TXS = "ja"
TXT = "zh"
#TXSecretId和TXSecretKey是腾讯云机翻的一对api密钥，填写你自己的
#TXS是待翻译的语种
#TXT是翻译的目标语种

APPID = 
SECRET = ''
BDTS = "jp"
BDTT = "zh"
#APPID 和SECRET是百度机翻的appid和密钥，填写你自己的
#BDTS是待翻译的语种
#BDTT是翻译的目标语种


BDaccess_token = ''
BDS = "jp"
BDT = "zh"
#BDaccess_token是百度ai翻译的访问tooken，填写你自己的，这个不是机翻，是百度ai开放平台的ai翻译，1年内免费500w字符，质量略高
#BDS是待翻译的语种
#BDT是翻译的目标语种



out = "よかった。何かレムにお手伝いできることがあれば、いつでも言ってください。レムはいつでもあなたの味方です。"
out1 = translate_ja_to_zh(out, BDaccess_token, BDS, BDT)
print("百度AI翻译：", out1)
out2 = txtra(out, TXSecretId, TXSecretKey, TXS, TXT)
print("腾讯机翻：", out2)
out3 = translate_text(out, APPID, SECRET, BDTS, BDTT)
print ("百度机翻：", out3)


