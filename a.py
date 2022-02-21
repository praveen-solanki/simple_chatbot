
from Chatbot import query

def get_response(query):
    if query == 'what is the time' or query == 'whats the time' or query == 'what is the current time' or query == 'the current time' or query == 'whats the current time' or query == 'what is the time now' or query == 'whats the time now' or query == 'current time' or query == 'the time':
        strtime = datetime.datetime.now().strftime(('%I:%M:%S'))
        print(f'Time : {strtime}')
        speak(f'sir, the time is {strtime}')
        return strtime
        
    elif query in list:
        print(random.choice(list))
        
    elif query == 'play some music' or query == 'play some song' or query == 'play song' or query == 'play music' or query == 'play some romantic song' or query == 'play some romantic music' or query == 'music':
        music_dir = 'C:\\Users\\praveen solanki\\Desktop\\songs'
        songs = os.listdir(music_dir)
        a = random.randint(1, len(songs))
        os.startfile(os.path.join(music_dir, songs[a]))

    elif 'wikipeida' in query:
        speak('searching')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    elif 'email' in query:
        try:
            speak('what should i say')
            content = takecommand()
            to = 'yahoo48pintu@gmai.com'
            sendEmail(to, content)
            speak("Email sent")
        except:
            speak('Sorry i am not able to sent')
        takecommand()

    elif 'open youtube' in query:
        oy = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome_proxy.exe'
        os.startfile(oy)

    elif query == 'open google' or query == 'google.com'or query == 'launch google'or query == 'google':
        webbrowser.open(
            'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --profile-directory="Profile 3')

    elif query == 'open stackoverflow' or query == 'open stack overflow' or query == 'open starkover flow' or query == 'open stack over flow' or query == 'launch stackoverflow' or query == 'launch stack overflow' or query == 'launch starkover flow' or query == 'launch stack over flow':
        webbrowser.open('stackoverflow.com')

    elif 'open facebook' in query or query == 'open my facebook account' or query == 'open my fb account' or query == 'open my fb' or query == 'open my facebook' or query == 'open my fb' or query == 'launch my facebook account' or query == 'launch my fb account' or query == 'launch my fb' or query == 'launch my facebook' or query == 'open my fb':
        fb = 'https://www.facebook.com/'
        Praveen(fb)

    elif query == 'open my linkedin' or query == 'open my linked account' or query == 'open linked in' or query == 'open linkedin'or query == 'launch my linkedin' or query == 'launch my linked account' or query == 'launch linked in' or query == 'launch linkedin':
        li = 'https://www.linkedin.com/feed/'
        Praveen(li)

    elif query == 'open gmail' or query == 'open my gmail account' or query == 'open my gmail'or query == 'launch gmail' or query == 'launch my gmail account' or query == 'launch my gmail'or query == 'open gmail account':
        gmail = 'https://mail.google.com/mail/u/0/#inbox'
        Praveen(gmail)

    elif query == 'open swayam central' or query == 'open swayamcentral' or query == 'open nptel'or query == 'launch swayam central' or query == 'launch swayamcentral' or query == 'launch nptel'or query == 'open swayam center' or query == 'open swayamcenter':
        lsc = 'https://swayam.gov.in/'
        Praveen(lsc)

    elif query == 'open instagram' or query == 'open my instagram'or query ==  'launch instagram' or query == 'launch my instagram'or query == 'open insta gram' or query == 'open insta gram':
        ig = 'https://www.instagram.com/'
        Praveen(ig)

    elif query == 'open greatlearning' or query == 'open great learning'or query == 'launch great learning'or query == 'launch greatlearning':
        gl = 'https://olympus.mygreatlearning.com/dashboard'
        Praveen(gl)

    elif query =='open internshala' or query=='open intern shala'or query == 'launch internshala'or query == 'launch intern shala':
        ins = 'https://internshala.com/internships/matching-preferences'
        Praveen(ins)

    elif query == 'open visual studio code' or query == 'open visualstudio code' or query == 'open vscode' or query == 'open visualstudiocode' or query == 'open visual studiocode' or query == 'open vs code' or query == 'open v s code' or query == 'open v scode':
        vspath = "C:\\Users\\praveen solanki\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vspath)

    elif query == 'open pycharm' or query == 'open py charm' or query == 'open pycharm ide'or query == 'launch pycharm'or query == 'launch pycharm ide':
        pcpath = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2\\bin\\pycharm64.exe'
        os.startfile(pcpath)

    elif query == 'open typing master' or query == 'open typingmaster' or query == 'launch typing master'or query == 'launch typingmaster':
        tmpath = "C:\\Program Files (x86)\\TypingMaster10\\tmaster.exe"
        os.startfile(tmpath)

    elif query == 'open vlc' or query == 'open media player' or query == 'open vlc media player':
        vlcpath = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
        os.startfile(vlcpath)

    elif query == 'open excel' or query == 'open ms excel' or query == 'open microsoft excel' or query == 'open microsoftexcel' or query == 'open m s excel' or query == 'open m sexcel':
        mse = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(mse)

    elif query == 'open powerpoint' or query == 'open pp ' or query == 'open ms pp' or query == 'open microsoft powerpoint' or query == 'open power point' or query == 'open p p':
        mspp = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(mspp)

    elif query == 'open ms word' or query == 'open microsoft word' or query == 'open microsoftword' or query == 'open m s word' or query == 'open m sword' or query == 'open word':
        msw = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(msw)

    elif query == 'open ms edge' or query == 'open msedge' or query == 'open microsoft edge' or query == 'open m s edge' or query == 'open microsoftbrowser' or query == 'open m sedge' or query == 'open microsoftedge' or query == 'open microsoft browser' or query == 'open ms browser':
        mseb = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(mseb)

    elif query == 'open git bash' or query == 'open git cmd' or query == 'open git base command prompt'or query == 'open git' :
        gitb = "C:\\Program Files\\Git\\git-bash.exe"
        os.startfile(gitb)

    elif query == 'open python ide' or query == 'open python cmd' or query == 'open pythoncmd' or query == 'opne python command prompt' or query == 'open pythonide':
        pcmd = "C:\\python 3.7\\python.exe"
        os.startfile(pcmd)

    elif query == 'open my photo' or query == 'show my photos' or query == 'show my photo' or query == 'show me my photo' or query == 'show me my photos' or query == ' open my photos':
        omp = 'C:\\Users\\praveen solanki\\Desktop\\My-Photos'
        os.startfile(omp)

    elif query == 'open my documents' or query == 'open my document' or query == 'open my personal documents' or query == 'open my all documents' or query == 'show my all documents' or query == 'open my documents' or query == 'show my document' or query == 'show me my all documents' or query == 'open me my all document' or query == 'show me my documents' or query == 'show me my document':
        omd = 'C:\\Users\\praveen solanki\\Desktop\\praveen documents'
        os.startfile(omd)

    elif query == 'open my certificates' or query == 'open my certificate' or query == 'open my personal certificates' or query == 'open my all certificates' or query == 'show my all certificates' or query == 'open my certificates' or query == 'show my certificate' or query == 'show me my all certificates' or query == 'open me my all certificate' or query == 'show me my certificates' or query == 'show me my certificate':
        ocm = 'C:\\Users\\praveen solanki\\Desktop\\Certificates'
        os.startfile(ocm)

    elif query == 'exit program' or query == 'exit chatbot' or query == 'close program' or query == 'exit code' or query == 'exit' or query == 'close the program' or query == 'exit the program' or query == 'break' or query =='quit' or query =='see you later' or query =='chat with you later' or query =='end the chat' or query =='bye' or query =='ok bye':
        pass

def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}:{msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}:{get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

if __name__ == '__main__':
    get_response(query)
    bot_name = 'heiss'