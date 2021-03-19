# python-get-live-streaming
Get live streaming of each live platform (m3u8, flv, etc.)

## 获取各直播平台的视频直播流
通过ip代理形式爬取各直播平台直播流,防止ip被封,主要功能有:
1. 获取可用代理ip,分为单例模式和多例模式
2. 通过抖音,快手,淘宝等直播平台的分享链接,获取m3u8/flv直播流
3. redis储存可用代理ip
4. 通过ffmpeg将直播流转为视频保存在本地

