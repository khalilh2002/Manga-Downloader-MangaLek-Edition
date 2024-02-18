import os
import time

from bs4 import BeautifulSoup
import requests
from tkinter import filedialog

class cli:
    
    def __init__(self ,manga_name=None,ch=None, url = 'https://manga-like.net/manga/'):
        self.count = 1
        self.count_ch = 1
        
        self.url = url
        self.download_path= filedialog.askdirectory()
        if(manga_name==None and ch==None):
            manga_name = input('the name of manga :  ')
            self.ch = input("chapter number : ")
        else:
            self.ch=ch
        
        self.path_manga = f'{self.download_path}/{manga_name}/' 
        self.path_ch = self.path_manga + self.ch
        
       
        
        name = manga_name.strip().replace(" ", "-")
        
        self.new_url = url+name+"/"
        
        try:
            os.mkdir(f'{self.download_path}/{manga_name}/')
        except Exception:
            pass
        
        
        total = 10
        if self.ch == 'all':
            for i in range(1, total):
                self.operation(str(i))
                print(f"folder {i} end")
                time.sleep(5)
            self.count_ch += 1
        else:
            self.operation(self.ch)
            
    def get_request(self):
        r = requests.get( self.new_url  )
        if r.status_code in range(200, 301):
            return r.text
        else:
            print(f'error code : {r.status_code}')
    
    def save_image(self,src):
        os.chdir(self.path_ch)
        data = requests.get(src)
        data = data.content
        open(f"img_{self.count}.jpg", "wb").write(data) #create and write data in the image
        print(f'Download {self.count}')
        
    def operation(self,n):
        
        self.path_ch = self.path_manga + n
        try:
            os.mkdir(self.path_ch)
        except Exception:
            pass

        self.new_url = self.new_url + n
        
        html_data = self.get_request()
        
        soup = BeautifulSoup(html_data, 'lxml')
        
        all_images = soup.findAll("img")
        
        for img in all_images:
            try:
                self.save_image(img["src"])
            except Exception:
                break
            self.count += 1
        self.count = 1
    
if __name__ == "__main__":
    window = cli()