import win32gui
import win32api
import win32con
import time
import random
def getWechatWindow():
    classname = "WeChatMainWndForPC"
    titlename = "微信"
    #获取句柄,判定微信是否在运行
    while True:  
        hwnd = win32gui.FindWindow(classname, titlename)
        if(hwnd!=0):
            return hwnd
        else:
            print('微信没有打开，重新获取中 ,我是可爱的随机数： '+str(random.uniform(10, 20)))
            time.sleep(60) #如果没有打开微信，1分钟扫描一次后台
             
       
       
        
    
    #win32gui.ShowWindow(hwnd,win32con.SW_RESTORE)       #强行显示界面
    #win32gui.SetForegroundWindow(hwnd)      #将窗口提到最前
    #获取窗口左上角和右下角坐标
    #left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    #print(str(left)+' '+str(top)+' '+str(right)+' '+str(bottom))
    #return hwnd
    #判断是否在前面
if __name__ == '__main__': 
   a= getWechatWindow()
   print(a)