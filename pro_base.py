import time
import openpyxl
import sys

def progress_bar(finish_tasks_number, tasks_number):
    """
    进度条

    :param finish_tasks_number: int, 已完成的任务数
    :param tasks_number: int, 总的任务数
    :return:
    """

    percentage = round(finish_tasks_number / tasks_number * 100)
    print("\r进度: {}%: ".format(percentage), "▓" * (percentage // 2), end="")
    sys.stdout.flush()


if __name__ == '__main__':
    for i in range(0, 101):
        progress_bar(i, 100)
        time.sleep(0.05)

def today_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
def today_day():
    return time.strftime("%Y-%m-%d", time.localtime())
def open_xlsx(xlsx):
    # 读取 Excel 文件
    wb = openpyxl.load_workbook(xlsx)
    ws = wb.active
    return ws
