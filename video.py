import subprocess

# 通过ffmpeg将直播流转为视频保存在本地
def runcmd(command):
    ret = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    ret.wait(2)
    if ret.poll() == 0:
        print(ret.communicate()[1])
    else:
        print("失败")


subprocess.call(['ffmpeg', '-i', 'https://ali-adaptive.hlspull.yximgs.com/gifshow/BHTMqv83Z3s_sd1000.m3u8?auth_key=1615663260-0-0-3d5706395d06c2aec84ed2971476d726&tsc=origin&oidc=txhd','-fs','30M','-c','copy','-bsf:a','aac_adtstoasc' ,'kuaishou1.mp4'])
# runcmd('ffmpeg -i "https://ali-adaptive.hlspull.yximgs.com/gifshow/BHTMqv83Z3s_sd1000.m3u8?auth_key=1615663260-0-0-3d5706395d06c2aec84ed2971476d726&tsc=origin&oidc=txhd" -fs 30M -c copy -bsf:a aac_adtstoasc   "~/Movies/Videos/lives/kuaishou1.mp4"')#序列参数
# runcmd(['cd ~/Movies/Videos/lives','ls'])
# runcmd("ls")
# subprocess.run(["ffmpeg -i 'https://ali-adaptive.hlspull.yximgs.com/gifshow/BHTMqv83Z3s_sd1000.m3u8?auth_key=1615663260-0-0-3d5706395d06c2aec84ed2971476d726&tsc=origin&oidc=txhd' -fs 30M -c copy -bsf:a aac_adtstoasc '~/Movies/Videos/lives/kuaishou1.mp4'"])
# runcmd("java -version")
