import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main():
    class downloadhandler(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示：', '下载完成！')
            butuon1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        butuon1.config(state=tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程（主程序退出就不再保留执行）
        # 在线程中处理耗时间的下载任务
        downloadhandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者：marebm')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('512x234')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    panel.pack(side='bottom')
    butuon1 = tkinter.Button(panel, text="下载", command=download)
    butuon1.pack(side='left')
    butuon2 = tkinter.Button(panel, text="关于", command=show_about)
    butuon2.pack(side='right')

    tkinter.mainloop()


if __name__ == '__main__':
    main()
