import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from time import sleep
import random

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Snake Xenzia")
        self.n = 50
        self.setFixedSize(15*self.n+60,15*self.n+60)
        
        self.move(100,10)
        
        self.snake = [(int(self.n/2), int(self.n/2)-1),(int(self.n/2), int(self.n/2)),(int(self.n/2), int(self.n/2)+1)]
        
        self.dirn = 0     #0 Right, 1 Down, 2 Left, 3 Up
        self.timer = QBasicTimer()
        self.timer.start(100, self)

        self.score = 0
        self.arena()
        self.food=(-1,-1)
        self.give_food()

    def arena(self):
       
        

        ground = QLabel("", self)
        ground.move(0,0)
        ground.resize(15*self.n+60,15*self.n+60)
        ground.setStyleSheet("background-color: black")
        
        self.pixels = [[QLabel("",self) for i in range(self.n)] for i in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.n):
                self.pixels[i][j].move(15*(j+2),15*(i+2))
                self.pixels[i][j].setFixedHeight(15)
                self.pixels[i][j].setFixedWidth(15)

                if((i,j) in self.snake):
                    self.pixels[i][j].setStyleSheet("background-color: red")
                else:
                    self.pixels[i][j].setStyleSheet("background-color: white")
        
        
        self.points = QLabel("Score: "+str(self.score), self)
        self.points.move(30,0)
        self.points.setStyleSheet("color:white; font-family: Consolas; font-size:20px")

        self.show()
        
    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.refresh_snake()

    def refresh_snake(self):
        temp = self.snake.pop(0)

        self.pixels[temp[0]][temp[1]].setStyleSheet("background-color: white")
        temp = self.snake[-1]

        temp = self.next_step(temp)
        
        
        if(temp in self.snake):
            self.gameover()
        
        else:
            self.snake.append(temp)
            self.pixels[temp[0]][temp[1]].setStyleSheet("background-color: red")
        
        if(temp == self.food):
            temp = self.next_step(temp)
            self.snake.append(temp)
            self.pixels[temp[0]][temp[1]].setStyleSheet("background-color: red")
            self.give_food()
            self.score+=1
            self.points.setText("Score: "+str(self.score))

    
    def next_step(self,temp):
        if(self.dirn==0):
            temp = (temp[0], temp[1]+1)

        elif(self.dirn==1):
            temp = (temp[0]+1, temp[1])
        
        elif(self.dirn==2):
            temp = (temp[0], temp[1]-1)

        elif(self.dirn==3):
            temp = (temp[0]-1, temp[1])
        
        if(temp[0]>=50 or temp[0]<0 or temp[1]>=50 or temp[1]<0 ):
            temp = (temp[0]%self.n, temp[1]%self.n)

        return temp

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Left:
            if self.dirn != 0:
                self.dirn = 2
        if key == Qt.Key_Right:
            if self.dirn != 2:
                self.dirn = 0
        if key == Qt.Key_Up:
            if self.dirn != 1:
                self.dirn = 3
        if key == Qt.Key_Down:
            if self.dirn != 3:
                self.dirn = 1
        
    def give_food(self):
        self.food = self.random_pixel()
        self.pixels[self.food[0]][self.food[1]].setStyleSheet("background-color: green")

    def random_pixel(self):
        x = random.randint(0, self.n-1)
        y = random.randint(0, self.n-1)
        if((x,y) in self.snake):
            return self.random_pixel()
        else:
            return (x,y)

    def gameover(self):
        self.timer.stop()
        ret = QMessageBox.question(self, 'Game', "Wanna Play Again?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
            self.__init__()
        else:
            self.close()
            
        


app = QApplication(sys.argv)
app.setStyleSheet("QLabel{font-size: 14pt;}")
app.setStyle("fusion")
custom_font = QFont()
custom_font.setWeight(12)
QApplication.setFont(custom_font, "QLabel")
win = Window()
sys.exit(app.exec_())



'''

                '''