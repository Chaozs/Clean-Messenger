#Source code from: https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
#!/usr/bin/env python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
from tkinter.messagebox import showinfo
import sys, WordChecker, Word2VecInterface, time, Filter

#for connecting to server
BUFSIZ = 1024
ADDR = ('localhost', 9999)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

sendMode = 0 # 0 = send message, 1 = add to filter
word2vec = Word2VecInterface.Word2VecInterface()

def filter(msg):
    filtered_msg = msg
    return filtered_msg

def receive():
    #infinite loop due for receiving messages non-deterministically
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(END, "\n" + filter(msg))
            print(msg)
        except OSError:  # Possibly client has left the chat.
            break

# Sending a message to connected server
def send(event=None):
    msg = my_msg.get() #input field on GUI
    my_msg.set("")  # Clears input field.
    if sendMode == 0:
        cleanMessage = Filter.filterMessage(msg)
        client_socket.send(bytes(cleanMessage, "utf8"))
        if msg == "{quit}": #client is closed
            client_socket.close()
            window.quit()
    elif sendMode == 1:
        #if word is already in list, give error message
        words = WordChecker.get_words_from_file('filter.txt')
        if WordChecker.check_word_exists_in(words, msg):
            popup_message("Word already exists")
        #otherwise add word to filter list
        else:
            WordChecker.add_word_to_file("filter.txt", msg)
            recommendedWords = word2vec.getWordsSimilarTo(msg)
            if len(recommendedWords) > 1:
                suggestionMessage = craft_suggestion_message(recommendedWords, msg)
                msg_list.insert(END, "\n" + suggestionMessage)
            else:
                msg_list.insert(END, "\n" + "No suggested words to filter were found")
            popup_message('"' + msg + '" has been added')
    elif sendMode == 2:
        words = WordChecker.get_words_from_file('filter.txt')
        if WordChecker.check_word_exists_in(words, msg):
            WordChecker.remove_string_from_file("filter", msg)
            popup_message(msg + " was removed from filter list")
        else:
            popup_message("That word was not found in filter list")

#close connection and exist
def on_closing(event=None):
    #cleanup function when client is closed
    my_msg.set("{quit}")
    global sendMode
    sendMode = 0
    send()

# Create message for filter suggestions
def craft_suggestion_message(wordList, word):
    suggestion = "Filter suggestions similar to " + word + ": "
    for word in wordList:
        suggestion = suggestion + word + ", "
    return suggestion[:-2]

#Display popup window with message
def popup_message(message):
   showinfo("Window", message)

def swapMode():
    global sendMode
    global modeMessage
    if sendMode == 0:
        sendMode = 1
        my_msg.set("Type word to filter here")
        mode.set("Adding to Filter")
    elif sendMode == 1:
        sendMode = 2
        my_msg.set("Type word to remove from filter here")
        mode.set("Removing from Filter")
    else:
        sendMode = 0
        my_msg.set("Type your messages here.")
        mode.set("Sending Message")

window = Tk()
window.title("Clean Messenger")
window.geometry('400x350')

mode = StringVar()
mode.set("Sending Message")

#frame for holding list of messages
messages_frame = Frame(window)
my_msg = StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = Scrollbar(messages_frame)  # To navigate through past messages.

#message list which will be stored in messages_frame
# Following will contain the messages.
msg_list = Text(messages_frame, height=15, width=50, wrap=WORD)
msg_list.config(yscrollcommand=scrollbar.set)
#msg_list = Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()
messages_frame.pack()

modeMessage = Label(window, textvariable=mode)
modeMessage.pack(anchor=N)

#input field for user to input message
entry_field = Entry(window, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack(fill=BOTH, expand=True)
send_button = Button(window, text="Send", command=send)
send_button.pack()

swap_button = Button(window, text="Swap mode", command=swapMode)
swap_button.pack(anchor=E)

window.protocol("WM_DELETE_WINDOW", on_closing)

receive_thread = Thread(target=receive)
receive_thread.start()
mainloop()  # Starts GUI execution.
