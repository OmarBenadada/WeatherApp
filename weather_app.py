import sys
import requests
from PyQt5.QtWidgets import QApplication,QLabel,QPushButton,QLineEdit,QVBoxLayout,QWidget
from PyQt5.QtCore import Qt
class WeatherWindow(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.setGeometry(400,400,500,600)
        self.Enter_cityname=QLabel("Enter The City Name :",self)
        self.button = QPushButton("Click Here", self)
        self.button.clicked.connect(self.on_click)        
        self.cityname=QLineEdit(self)
        self.cityname.setPlaceholderText("Enter the name...")
        self.temperarute=QLabel("60°C",self)
        self.Hala=QLabel("Sunny",self)
        self.emoji=QLabel("☀",self)
        self.initui()
        
    def initui(self):
        
        self.setWindowTitle("Weather App")
        
        names=[self.Enter_cityname,self.button,self.cityname,self.temperarute,self.emoji,self.Hala]
        sizes=[40,40,40,70,80,60]
        vbox=QVBoxLayout()
        self.setLayout(vbox)
        
        for i in names:
            vbox.addWidget(i)
        
        for j in names[:1] + names[2:]:
            j.setAlignment(Qt.AlignCenter)
            
        for y,size in zip(names,sizes):
            y.setStyleSheet(f"font-size:{size}px; ")
        
        self.button.setMaximumHeight(60)
        self.cityname.setMaximumHeight(60)
        
    def on_click(self):
        
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        input_text = self.cityname.text()
        para={"q":input_text,
              "appid":"f43e187881ffa1ef9623a04fb490b629",
              "units":"metric"}
        responce=requests.get(base_url,params=para)
        
        match responce.status_code:
            
            case 100 | 101 | 102 | 103:
                self.temperarute.setText("Informational Error")

            case 200 | 201 | 202 | 203 | 204 | 205 | 206 | 207 | 208 | 226:
                self.temperarute.setText(str(f'{responce.json()['main']['temp']}°C'))

            case 300 | 301 | 302 | 303 | 304 | 305 | 306 | 307 | 308:
                self.temperarute.setText('Redirection Responses Error')

            case 400 | 401 | 402 | 403 | 404 | 405 | 406 | 407 | 408 | 409 | 410 | 411 | 412 | 413 | 414 | 415 | 416 | 417 | 418 | 421 | 422 | 423 | 424 | 425 | 426 | 428 | 429 | 431 | 451:
                self.temperarute.setText('Client Errors')

            case 500 | 501 | 502 | 503 | 504 | 505 | 506 | 507 | 508 | 510 | 511:
                self.temperarute.setText('Server Errors')
                
        
           
class main():
    weatherapp=QApplication(sys.argv)
    Window=WeatherWindow()
    Window.show()
    sys.exit(weatherapp.exec_())

if __name__=="__main__":
    main()