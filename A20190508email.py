import time
import os
import win32gui, win32ui, win32con, win32api
#文件名不能以数字开头，不然其他py文件识别不了。

def window_capture(filename,hwndt):
    #hwnd = hwndt  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwndt)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    #w = MoniterDev[0][2][2]
    #h = MoniterDev[0][2][3]
    # print w,h　　　#图片大小
    #print(w,h)
    left, top, right, bottom = win32gui.GetWindowRect(hwndt)
    w=right-left #图片大小，宽
    h=bottom-top #图片大小，高
    print(w,h)
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    # 释放内存，不然会造成资源泄漏
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()

# beg = time.time()
# for i in range(10):
#     print(i)
#     #print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"-PC-Name-.jpg")
#     window_capture("我的世界-PC-Name-.jpg")
# end = time.time()
# print(end - beg)


if __name__ == '__main__': 

    window_capture('haha.jpg',197202)
    