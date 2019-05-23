import A20190506email
import A20190508email
import A20180508ImageEdit
import WeChatFind
import schedule
import time
import os
everyTime =5 #每隔多少分钟执行一次截图 单位：分钟，60*5 表示5分钟。
picName=''
def job():
    #第一步，获取time和设置照片名字
    TimeName=time.strftime("%Y%m%d_%H-%M-%S", time.localtime()) #命名问题，windows文件名不能出现“:”
    picName=TimeName+' '+os.environ['COMPUTERNAME']+'.jpg'
    #第1.1步，找到微信窗口是否在运行，并截图
    A20190508email.window_capture(picName,WeChatFind.getWechatWindow())
    #第二步，调整图片
    A20180508ImageEdit.compress_image(os.getcwd()+'\\'+picName)
    A20180508ImageEdit.resize_image(os.getcwd()+'\\'+picName)
    #第三步，发送邮件
    m = A20190506email.SendMail(
        username='27709351@qq.com',
        passwd='mozxglabsequbifi',#这里使用的是授权码，而不是QQ密码。
        recv=['fhxxx258@163.com'],
        title='自动发邮件截图电脑测试,今天是'+TimeName,
        content='今天是'+TimeName+'，这是自动截图测试报告',
        file=os.getcwd()+'\\'+picName,
        ssl=True,
        #授权码：mozxglabsequbifi
    )
    m.send_mail()

# pwd = os.getcwd()
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
#重复的关键词，没多少秒执行一次
schedule.every(everyTime).seconds.do(job)

if __name__ == '__main__': 
    while True:
        schedule.run_pending()
        time.sleep(1)