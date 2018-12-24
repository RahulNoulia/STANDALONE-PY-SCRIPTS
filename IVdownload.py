from tkinter import *
import requests
import  os


class Action:
    counter = 0
    count = 0
    def ImageDownload(self):
        try:
            self.counter += 1
            """
            for test you can put this url as input 
            
            https://images.alphacoders.com/793/793242.jpg
            
            """
            iurl = et1.get()
            if iurl == "":
                Label(root, text="Input cann't empty !", font="sans-serif", bg="orange", fg="#192A56").place(x=40, y=80, height="40")
                return

            last = iurl[-3:]

            imageName = "image" + str(self.counter) + "." + last
            print(imageName)
            response = requests.get(iurl, stream=True)
            os.chdir("/root/Downloads")

            with open(imageName, 'wb') as fileObject:
                for chunk in response.iter_content(chunk_size=100):

                   if chunk:
                        fileObject.write(chunk)
            Label(root, text="Image Dowmloaded", font="sans-serif", bg="orange",fg="#192A56").place(x=40, y=80, height="40")

        except requests.exceptions.MissingSchema:
            Label(root, text="Oops ! error occured make sure url is correct ", font="sans-serif", bg="orange", fg="#192A56").place(x=40, y=80, height="40")



    def VideoDownload(self):
        try:
            self.count += 1
            vurl = et2.get()
            if vurl == "":
                Label(root, text="Input cann't empty !", font="sans-serif", bg="orange", fg="#192A56").place(x=40, y=200, height="40")
                return
            response = requests.get(vurl, stream=True)
            vlast = vurl[-3:]
            videoName = "video" + str(self.count) + vlast

            os.chdir("/root/Downloads")

            with open(videoName, "wb") as fileObject:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        fileObject.write(chunk)
            Label(root, text="Video Dowmloaded", font="sans-serif", bg="orange", fg="#192A56").place(x=40, y=200, height="40")

        except requests.exceptions.MissingSchema:
            Label(root, text="Oops ! error occured make sure url is correct ", font="sans-serif", bg="orange", fg="#192A56").place(x=40, y=200, height="40")

    def refresh(self):
        et1.set("")
        et2.set("")
        Label(root, text=" ", width="37", font="sans-serif", bg="orange", fg="#192A56").place(x=40, y=80, height="40")
        Label(root, text=" ", width="37", font="sans-serif", bg="orange", fg="#192A56").place(x=40, y=200, height="40")



if __name__ == "__main__":
    root = Tk()
    root.title("IVdownload")
    root.resizable(width=False ,height=False)
    root.configure(background="orange")
    root.geometry("690x300")

    """ for image """

    Label(root, text="Enter image url ", font="sans-serif" ,bg="orange").place(x=40, y=30, height="40")
    et1 = StringVar()
    Entry(root, textvariable=et1, width="40", state=NORMAL).place(x=200, y=30, height=35)

    """ Object """
    ac = Action()
    Button(root, text="Download", width="6", height="1", bg="#45CE30", activebackground="#45CE30", command=lambda: ac.ImageDownload()).place(x=550, y=30, height=35)

    """ for Video """

    Label(root, text="Enter video url ", font="sans-serif", bg="orange").place(x=40, y=150, height="40")
    et2 = StringVar()
    Entry(root, textvariable=et2, width="40", state=NORMAL).place(x=200, y=150, height=35)
    Button(root, text="Download", width="6", height="1", bg="#45CE30", activebackground="#45CE30", command=lambda: ac.VideoDownload()).place(x=550, y=150, height=35)


    """ Refresh """
    Button(root, text="Refresh", width="6", height="1", bg="#45CE30", activebackground="#45CE30",command=lambda: ac.refresh()).place(x=40, y=250, height=35)
    root.mainloop()



