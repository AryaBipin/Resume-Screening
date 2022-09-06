from asyncio.windows_events import NULL
from flask import Flask, redirect,request,render_template,flash,url_for,send_from_directory
import os
from PIL import Image,ImageDraw
import cgi, os
import cgitb; cgitb.enable()
import PyPDF2
import re
form = cgi.FieldStorage()
from tkinter import * 
from tkinter import messagebox
import re
from collections import Counter

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        fi = request.files['file']
        if request.values['include_area']:
            text_content=[]
            found_list=[]
            file_list=[]
            result=[]
            tmp=0
            temp=[]
            
            text_content_tmp = request.values['include_area']
            text_content = re.sub("[^\w]", " ",  text_content_tmp).split()
            #text_content.append["ffdkgj"]
           # temp=request.values['include_area'].split(" ")
            #text_content.append(temp)
            count=0
            fil = os.path.basename(fi.filename)
            file_list=fil
            fi.save(os.path.join("static/uploads",fil))
            object = PyPDF2.PdfFileReader("static/uploads//"+fil)
            NumPages = object.getNumPages()
            lenth=len(text_content)
             
            for i in range(0, NumPages):
                PageObj = object.getPage(i)
                print("this is page " + str(i)) 
                Text = PageObj.extractText() 
                for j in text_content :
                      ResSearch = re.search(j, Text,re.IGNORECASE)
                      if ResSearch:
                        found_list.append(j)
                        count=count+1  
              #findout the density of the words
              #  res = Counter(Text.split())   
              # assigning to list words
               # res = [res[sub] for sub in text_content] 
               #sum the count list
               # for j in range(0, len(res)):
               # tmp = tmp + res[i]
               #result.append(tmp)
# printing result
        return "The words to search"+str(text_content)+"<br>The list words frequency in pdf : " + str(found_list) +"<br>The count of words"+str(count)
        if found_list:
            return str(count)+"words found"
        else:
            return "No Keywords found"
        
        
            
if __name__ == "__main__":
    app.run(debug=True,port=5005)
   