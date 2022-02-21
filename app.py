from tkinter import *
from chat import get_response, bot_name

BG_GREY = '#ABB2B9'
BG_COLOR = '#17202A'
TEXT_COLOR = '#EAECEE'

FONT = 'Helvetica 14'
FONT_BOLD = 'Helvetica 13 bold'

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

        # send button
        send_buttom = Button(bottom_label, text='Send', font=FONT_BOLD,
                             width=20, bg=BG_GREY, command=lambda: self._on_enter_pressed(None))
        send_buttom.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

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

        msg2 = f"{bot_name}:{get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
