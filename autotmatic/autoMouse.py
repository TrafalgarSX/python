# from json.tool import main
from turtle import position
import pyautogui
import time
import xlrd

# 922 515


def main():
    pyautogui.moveTo(1149, 26)
    time.sleep(2)
    # pyautogui.doubleClick(1149,26,button='left')  # 单击键
    pyautogui.mouseDown()

    # time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    # 选择频道
    pyautogui.moveTo(1287, 834)
    pyautogui.mouseDown()
    pyautogui.click()
    print("a")
    time.sleep(2)
    # 切换频道
    pyautogui.moveTo(799, 912)
    pyautogui.mouseDown()
    pyautogui.click()
    time.sleep(10)
    # ESC 退出
    # pyautogui.moveTo(1278,965)
    pyautogui.keyDown("capslock")
    time.sleep(2)
    pyautogui.moveTo(1035, 758)
    pyautogui.mouseDown()
    pyautogui.click()
    time.sleep(5)

    # 退出确定   过期提示时的位置
    pyautogui.moveTo(776, 628)
    pyautogui.mouseDown()
    pyautogui.click()
    time.sleep(5)

    # 741 548 正常退出确定键位置
    pyautogui.moveTo(741, 548)
    pyautogui.mouseDown()
    pyautogui.click()
    time.sleep(2)
    print(pyautogui.position())  # 得到当前鼠标位置；输出：Point(x=200, y=800)


if __name__ == "__main__":
    main()
