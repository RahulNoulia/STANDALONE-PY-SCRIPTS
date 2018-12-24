import requests
from bs4 import BeautifulSoup
from tkinter import *
import os

class SCRAP:
    counter = 0
    def all_links(self, page_url):
        try:
            if page_url == "":
                Label(root, text="Input cann't be empty !!", font="sans-serif", width="30", height="2", bg="#0A79DF").place(x=44, y=150)
                return
            r = requests.get(page_url)
            '''
                   html5lib is a  HTML parser library which is most powerfull one
            '''
            soup = BeautifulSoup(r.text, 'html5lib')
            selected_links = []
            links = soup.find_all('a', href=True)
            for link in links:
                if  not (link['href'].startswith('#') or link['href'].startswith('/') or link['href'].startswith('.') or link['href'].startswith('j')):
                    selected_links.append(link['href'])
            return selected_links

        except requests.exceptions.MissingSchema:

            Label(root, text="wrong format of url", font="sans-serif", width="30", height="2" ,bg="#0A79DF").place(x=28 , y=150)

    def Store(self, all_links):
        self.counter += 1
        os.chdir("/root/Documents")
        fileName = "file" + str(self.counter) + ".txt"
        for link in all_links:
            with open(fileName, 'a') as file_object:
                file_object.write(str(link))
                file_object.write("\n")

        Label(root, text="All Links are safe in file ({0})".format(fileName), font="sans-serif", width="30", height="2", bg="#0A79DF").place(x=80 , y=150)
        return


    def Click(self):
        page_url = st.get()
        links = s_obj.all_links(page_url)
        if links !=None:
            s_obj.Store(links)

    def refresh(self):
        Label(root, text="" , width="50", height="2", bg="#0A79DF").place(x=30, y=150)
        st.set("")

if __name__ == "__main__":

    root = Tk()
    root.title("Downloader")
    root.resizable(width=False, height=False)
    root.configure(background='#0A79DF')
    Label(root, text="Enter page url  ->", font="sans-serif", bg="#0A79DF").place(x=100, y=40, height=35)
    root.geometry("600x300")
    st = StringVar()
    s_obj = SCRAP()
    entry_obj = Entry(root, textvariable=st, width="57", state=NORMAL).place(x=100, y=100, height=35)
    Button(root, text="Download", width="6", height="1", bg="#45CE30", activebackground="#45CE30", command=lambda : s_obj.Click()).place(x=100, y=220)
    Button(root, text="Refresh", width="6", height="1", bg="#45CE30", activebackground="#45CE30", command=lambda: s_obj.refresh()).place(x=220, y=220)
    root.mainloop()

