import pyttsx3
import random
import face_recognition
import numpy as np
import cv2
import smtplib
import webbrowser
import os
import wikipedia
import datetime
from tkinter import *
import tkinter.messagebox as tmsg


BG_GREY = '#ABB2B9'
BG_COLOR = '#17202A'
TEXT_COLOR = '#EAECEE'
FONT = 'Helvetica 14'
FONT_BOLD = 'Helvetica 13 bold'


def get_response(query):

    if query == 'what is the time' or query == 'whats the time' or query == 'what is the current time' or query == 'the current time' or query == 'whats the current time' or query == 'what is the time now' or query == 'whats the time now' or query == 'current time' or query == 'the time':
        strtime = datetime.datetime.now().strftime(('%I:%M:%S'))
        print(f'Time : {strtime}')
        #speak(f'sir, the time is {strtime}')
        return strtime

    elif query == 'I have to authentic yourself that you are praveen,if you are praveen say yes either no':
        inp = 'yes'
        return inp
    
    elif query in list:
        return (random.choice(list))
        
    elif query == 'play some music' or query == 'play some song' or query == 'play song' or query == 'play music' or query == 'play some romantic song' or query == 'play some romantic music' or query == 'music':
        music_dir = 'C:\\Users\\praveen solanki\\Desktop\\songs'
        songs = os.listdir(music_dir)
        a = random.randint(1, len(songs))
        return os.startfile(os.path.join(music_dir, songs[a]))

    elif 'wikipeida' in query:
        speak('searching')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        #speak("According to Wikipedia")
        #speak(results)
        return results

    elif 'email' in query:
        try:
            print('what should i say')
            content = takecommand()
            to = 'yahoo48pintu@gmai.com'
            sendEmail(to, content)
            speak("Email sent")
        except:
            print('Sorry i am not able to sent')
        get_response(query)

    elif 'open youtube' in query:
        oy = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome_proxy.exe'
        return os.startfile(oy)

    elif query == 'open google' or query == 'google.com'or query == 'launch google'or query == 'google':
        return webbrowser.open(
            'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --profile-directory="Profile 3')

    elif query == 'open stackoverflow' or query == 'open stack overflow' or query == 'open starkover flow' or query == 'open stack over flow' or query == 'launch stackoverflow' or query == 'launch stack overflow' or query == 'launch starkover flow' or query == 'launch stack over flow':
        return webbrowser.open('stackoverflow.com')

    elif 'open facebook' in query or query == 'open my facebook account' or query == 'open my fb account' or query == 'open my fb' or query == 'open my facebook' or query == 'open my fb' or query == 'launch my facebook account' or query == 'launch my fb account' or query == 'launch my fb' or query == 'launch my facebook' or query == 'open my fb':
        fb = 'https://www.facebook.com/'
        return Praveen(fb)

    elif query == 'open my linkedin' or query == 'open my linked account' or query == 'open linked in' or query == 'open linkedin'or query == 'launch my linkedin' or query == 'launch my linked account' or query == 'launch linked in' or query == 'launch linkedin':
        li = 'https://www.linkedin.com/feed/'
        return Praveen(li)

    elif query == 'open gmail' or query == 'open my gmail account' or query == 'open my gmail'or query == 'launch gmail' or query == 'launch my gmail account' or query == 'launch my gmail'or query == 'open gmail account':
        gmail = 'https://mail.google.com/mail/u/0/#inbox'
        return Praveen(gmail)

    elif query == 'open swayam central' or query == 'open swayamcentral' or query == 'open nptel'or query == 'launch swayam central' or query == 'launch swayamcentral' or query == 'launch nptel'or query == 'open swayam center' or query == 'open swayamcenter':
        lsc = 'https://swayam.gov.in/'
        return Praveen(lsc)

    elif query == 'open instagram' or query == 'open my instagram'or query ==  'launch instagram' or query == 'launch my instagram'or query == 'open insta gram' or query == 'open insta gram':
        ig = 'https://www.instagram.com/'
        return Praveen(ig)

    elif query == 'open greatlearning' or query == 'open great learning'or query == 'launch great learning'or query == 'launch greatlearning':
        gl = 'https://olympus.mygreatlearning.com/dashboard'
        return Praveen(gl)

    elif query =='open internshala' or query=='open intern shala'or query == 'launch internshala'or query == 'launch intern shala':
        ins = 'https://internshala.com/internships/matching-preferences'
        return Praveen(ins)

    elif query == 'open visual studio code' or query == 'open visualstudio code' or query == 'open vscode' or query == 'open visualstudiocode' or query == 'open visual studiocode' or query == 'open vs code' or query == 'open v s code' or query == 'open v scode':
        vspath = "C:\\Users\\praveen solanki\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        return os.startfile(vspath)

    elif query == 'open pycharm' or query == 'open py charm' or query == 'open pycharm ide'or query == 'launch pycharm'or query == 'launch pycharm ide':
        pcpath = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2\\bin\\pycharm64.exe'
        return os.startfile(pcpath)

    elif query == 'open typing master' or query == 'open typingmaster' or query == 'launch typing master'or query == 'launch typingmaster':
        tmpath = "C:\\Program Files (x86)\\TypingMaster10\\tmaster.exe"
        return os.startfile(tmpath)

    elif query == 'open vlc' or query == 'open media player' or query == 'open vlc media player':
        vlcpath = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
        return os.startfile(vlcpath)

    elif query == 'open excel' or query == 'open ms excel' or query == 'open microsoft excel' or query == 'open microsoftexcel' or query == 'open m s excel' or query == 'open m sexcel':
        mse = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        return os.startfile(mse)

    elif query == 'open powerpoint' or query == 'open pp ' or query == 'open ms pp' or query == 'open microsoft powerpoint' or query == 'open power point' or query == 'open p p':
        mspp = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        return os.startfile(mspp)

    elif query == 'open ms word' or query == 'open microsoft word' or query == 'open microsoftword' or query == 'open m s word' or query == 'open m sword' or query == 'open word':
        msw = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        return os.startfile(msw)

    elif query == 'open ms edge' or query == 'open msedge' or query == 'open microsoft edge' or query == 'open m s edge' or query == 'open microsoftbrowser' or query == 'open m sedge' or query == 'open microsoftedge' or query == 'open microsoft browser' or query == 'open ms browser':
        mseb = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        return os.startfile(mseb)

    elif query == 'open git bash' or query == 'open git cmd' or query == 'open git base command prompt'or query == 'open git' :
        gitb = "C:\\Program Files\\Git\\git-bash.exe"
        return os.startfile(gitb)

    elif query == 'open python ide' or query == 'open python cmd' or query == 'open pythoncmd' or query == 'opne python command prompt' or query == 'open pythonide':
        pcmd = "C:\\python 3.7\\python.exe"
        return os.startfile(pcmd)

    elif query == 'open my photo' or query == 'show my photos' or query == 'show my photo' or query == 'show me my photo' or query == 'show me my photos' or query == ' open my photos':
        omp = 'C:\\Users\\praveen solanki\\Desktop\\My-Photos'
        return os.startfile(omp)

    elif query == 'open my documents' or query == 'open my document' or query == 'open my personal documents' or query == 'open my all documents' or query == 'show my all documents' or query == 'open my documents' or query == 'show my document' or query == 'show me my all documents' or query == 'open me my all document' or query == 'show me my documents' or query == 'show me my document':
        omd = 'C:\\Users\\praveen solanki\\Desktop\\praveen documents'
        return os.startfile(omd)

    elif query == 'open my certificates' or query == 'open my certificate' or query == 'open my personal certificates' or query == 'open my all certificates' or query == 'show my all certificates' or query == 'open my certificates' or query == 'show my certificate' or query == 'show me my all certificates' or query == 'open me my all certificate' or query == 'show me my certificates' or query == 'show me my certificate':
        ocm = 'C:\\Users\\praveen solanki\\Desktop\\Certificates'
        return os.startfile(ocm)

    elif query == 'exit program' or query == 'exit chatbot' or query == 'close program' or query == 'exit code' or query == 'exit' or query == 'close the program' or query == 'exit the program' or query == 'break' or query =='quit' or query =='see you later' or query =='chat with you later' or query =='end the chat' or query =='bye' or query =='ok bye':
        pass

class ChatApplication:

    def __init__(self):
        self.root = Tk()
        self._setup_main_window()
        self.root.wm_iconbitmap('Mag1cwind0w-O-Sunny-Day-Osd-sun.ico')

    def run(self):
        self.root.mainloop()


    def _setup_main_window(self):
        self.root.title("Chatbot")
        self.root.resizable(FALSE, FALSE)
        self.root.configure(width=470, height=550, bg=BG_COLOR)

        # head label
        head_label = Label(self.root, bg=BG_COLOR, fg=TEXT_COLOR,
                           text='Welcome', font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.root, width=450, bg=BG_GREY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Text widget
        self.text_widget = Text(self.root, width=20, height=2,
                                bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=4, pady=4)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.root, bg=BG_GREY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # nessage entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50",
                               fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06,
                             rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Menu and Submenu
        self.mymenu = Menu(self.root)
        self.m1 = Menu(self.mymenu,tearoff=0)
        self.m1.add_command(label='Facebook',command=self.fb_login)
        self.m1.add_separator()
        self.m1.add_command(label='Instagram',command=self.insta_login)
        self.m1.add_separator()
        self.m1.add_command(label='Linkedin',command=self.Linkedin_login)
        self.m1.add_separator()
        self.m1.add_command(label='GitHub',command=self.github_login)
        self.m1.add_separator()
        self.m1.add_command(label='StackOverFlow',command=self.sof_login)
        self.m1.add_separator()
        self.m1.add_command(label='Coursera',command=self.coursera_login)
        self.m1.add_separator()
        self.m1.add_command(label='Internshala',command=self.internshala_login)
        self.m1.add_separator()
        self.root.config(menu=self.mymenu)
        self.mymenu.add_cascade(label="Login",menu=self.m1)

        # Message box


        # send button
        send_buttom = Button(bottom_label, text='Send', font=FONT_BOLD,
                             width=20, bg=BG_GREY, command=lambda: self._on_enter_pressed(None))
        send_buttom.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _myfunc(self):
        print('hi')

    def fb_login(self):
        self.answer = tmsg.askquestion('yes or no',"for login you have to authienticate")
        if self.answer == 'yes':
            self.fb = 'https://www.facebook.com/'
            self.Praveen(self.fb)
    def insta_login(self):
        self.answer = tmsg.askquestion('yes or no',"for login you have to authienticate")
        print(self.answer)
        if self.answer == 'yes':
            self.ig = 'https://www.instagram.com/'
            self.Praveen(self.ig)
    def coursera_login(self):
        self.answer = tmsg.askquestion('yes or no',"for login you have to authienticate")
        print(self.answer)
        if self.answer == 'yes':
            self.Praveen()
    def Linkedin_login(self):
        self.answer = tmsg.askquestion('yes or no',"for login you have to authienticate")
        print(self.answer)
        if self.answer == 'yes':
            self.li = 'https://www.linkedin.com/feed/'
            self.Praveen(self.li)
    def sof_login(self):
        self.answer = tmsg.askquestion('yes or no',"for login you have to authienticate")
        if self.answer == 'yes':
            self.sof = 'stackoverflow.com'
            self.Praveen(self.sof)
    def internshala_login(self):
        self.answer = tmsg.askquestion('yes or no',"for login you have to authienticate")
        print(self.answer)
        if self.answer == 'yes':
            self.ins = 'https://internshala.com/internships/matching-preferences'
            self.Praveen(self.ins)
    def github_login(self):
        self.answer = tmsg.askquestion('yes or no',"for login you have to authienticate")
        print(self.answer)
        if self.answer == 'yes':
            self.Praveen()


    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "Me")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}:{msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        if msg is not  None:
         msg2 = f"{bot_name}:{get_response(msg)}\n\n"
         self.text_widget.configure(state=NORMAL)
         self.text_widget.insert(END, msg2)
         self.text_widget.configure(state=DISABLED)
         self.text_widget.see(END)

    def Praveen(self,webname):
        path = 'C:\\Users\\praveen solanki\\Desktop\\c\\images'
        images = []
        className = []
        myList = os.listdir(path)
        for c1 in myList:
            curImg = cv2.imread(f'{path}/{c1}')
            images.append(curImg)
            className.append(os.path.splitext(c1)[0]) 
        def findEncoding(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList
        encodeListKnown = findEncoding(images)
        print('Detecting')
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            faceFrame = face_recognition.face_locations(img1)
            encodeFrame = face_recognition.face_encodings(img1, faceFrame)
            for encodeFace, faceLoc in zip(encodeFrame, faceFrame):
                matches = face_recognition.compare_faces(
                    encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(
                    encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)
                if matches[matchIndex]:
                    print('opening')
                if cv2.waitKey(1) == webbrowser.open(webname):
                    break

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        #speak("good morning")
        print("good morning")
    elif hour >= 12 and hour <= 17:
        #speak('good afternoon')
        print('good afternoon')
    else:
        #speak('good evening')
        print('good evening')
    #speak('what can i do for you')

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('praveenthesoftwareengineer@gmail.com',
                 'softwareengineer@praveen')
    server.sendmail('praveenthesoftwareengineer@gmail.com', to, content)
    server.close()


    

def fopen(event=None):
    global file_path, filename
    file_path = filedialog.askopenfilename(defaultextension=".txt")
    try:
        filename = os.path.basename(file_path)
        root.title(f"Chat Bot - {filename}")
        text_widget = root.nametowidget(textcon)
        with open(file_path, "r") as file:
            content = file.read()
            textcon.delete('1.0', 'end-1c')
            text_contents[str(textcon)] = hash(content)
            text_widget.insert(END, content)
            print("Operation successfull")
    except(FileNotFoundError):
        print("Operation not successfull")
        return None

list = ['hi', 'hii', 'hello', 'how are you', 'hey', "What's up?", 'Sup?']
bot_name = 'chatyyy'

if __name__ == '__main__':
    wishme()

    app = ChatApplication()
    app.run()
    while True:
        query = msg
        query = query.lower()
    #query = takecommand()
