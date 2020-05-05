import pyautogui
import time
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import nar
import threading
from threading import Thread


class ExampleApp(QtWidgets.QMainWindow, nar.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.cnt = 0
		self.pushButton.clicked.connect(self.start)
		self.pushButton_2.clicked.connect(self.stop)


		
	
	def start(self):
		
		if self.cnt == 0:
			print("create thread")
			self.cnt = self.cnt + 1
			self.thread = Thread(target=self.start1, args=())
			pyautogui.alert('Skiper is stared!')
			self.thread.start()
		else:	
			pyautogui.alert('Skiper is already running!')

	def start1(arg):
		thread = threading.currentThread()

		while getattr(thread, "do_run", True):
			if pyautogui.pixelMatchesColor(12, 1000, (97, 97, 97)):
				x,y = pyautogui.position()
				pyautogui.click(12, 1000)
				pyautogui.moveTo(x, y)
				print("skip")
				#pyautogui.click(850, 810)
			elif pyautogui.pixelMatchesColor(1760, 998, (97, 97, 97),tolerance = 5):
				x,y = pyautogui.position()
				pyautogui.click(1760, 998)
				pyautogui.moveTo(x, y)
				print("next")
				time.sleep(5.0)
				x,y = pyautogui.position()
				pyautogui.click(850, 810)
				pyautogui.doubleClick(850, 810)
				pyautogui.moveTo(x, y)
				time.sleep(1.0)
				#pyautogui.click(850, 810)
				time.sleep(.5)
		print("Stopping as you wish.")


	def stop(self):	
		try:
			self.cnt = self.cnt - 1
			self.thread.do_run = False
			self.thread.join()
			pyautogui.alert('Skiper was stoped!')
		except AttributeError:
			pyautogui.alert('Skiper did not start!')		

	def closeEvent(self, event):
		try:
			self.cnt = self.cnt - 1
			self.thread.do_run = False
			self.thread.join()
		except AttributeError:
			pass

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

