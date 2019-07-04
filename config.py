import os
import re

# 配置文件，用来读取手机分辨率
readDevice_Info = os.popen('adb shell wm size').read()
# print(readDevice_Info.rstrip())
Pattern = re.compile('[0-9]+x[0-9]+')
res = Pattern.findall(readDevice_Info.rstrip())
# print(res)
ans = res[len(res)-1]
# print(ans)
tmp = ans.split('x')
XSize = tmp[0]
YSize = tmp[1]
# print(XSize,YSize)

