import win32gui
import win32api

classname = "WeChatMainWndForPC"
titlename = "微信"
#获取句柄
hwnd = win32gui.FindWindow(classname, titlename)
#获取窗口左上角和右下角坐标
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(str(left)+' '+str(top)+' '+str(right)+' '+str(bottom))
#判断是否在前面