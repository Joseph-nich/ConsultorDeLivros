import requests as rs
from tkinter import *

def consultaLivro():

  def consultarApi():
    try:               
      lb1['text'] = ''
      url1 = f"https://www.googleapis.com/books/v1/volumes?q={ed1.get()}"
      url1.replace(" ", " +")
      reqUrl1 = rs.get(url1)  
      dados1 = reqUrl1.json()
      
      print(f"O livro Encontrado Foi:")
      print(f"##############################")
      print(f"titulo: {dados1['items'][0]['volumeInfo']['title']}")
      print(f"subtitulo: {dados1['items'][0]['volumeInfo']['subtitle']}")
      print(f"Autor: {dados1['items'][0]['volumeInfo']['authors']}")
      print(f"Ano de Publicação: {dados1['items'][0]['volumeInfo']['publishedDate']}")
      print(f"##############################")
     
    except:
      
      bt1 = Button(janela1, width = 8,            
      text="Consultar", command=consultaLivro)
      bt1.place(x = 50, y=90)
  
  janela1 = Tk()
  janela1.title('Livros')


  ed1 = Entry(janela1, width = 14)
  ed1.place(x=38 , y=60 )


  bt1 = Button(janela1, width = 8,             
  text="Consultar", command=consultarApi)
  bt1.place(x = 51, y=90)
             

  lb1 = Label(janela1, text='Pesquise seu livro...', justify=LEFT)
  lb1.place(x=38, y=125)
  janela1.mainloop()

consultaLivro()