import win32gui
import win32api
import win32con
def getWechatWindow():
    classname = "WeChatMainWndForPC"
    titlename = "微信"
    #获取句柄
    hwnd = win32gui.FindWindow(classname, titlename)
    #win32gui.ShowWindow(hwnd,win32con.SW_RESTORE)       #强行显示界面
    #win32gui.SetForegroundWindow(hwnd)      #将窗口提到最前
    #获取窗口左上角和右下角坐标
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    print(str(left)+' '+str(top)+' '+str(right)+' '+str(bottom))
    return hwnd
    #判断是否在前面
if __name__ == '__main__': 
   a= getWechatWindow()
   print(a)