import PyPDF2
from tkinter import *
from tkinter import filedialog

def browseFile(file, pdfFiles):
    global no_of_files, lbl
    file = filedialog.askopenfilename(title="Browse Pdf files to merge")
    if file != "":
        pdfFiles.append(file)
        no_of_files+=1
        lbl = Label(window, text=f"[{no_of_files}] {file}")
        lbl.pack()
    if no_of_files>1:
        mrgBtn["command"] = merge

def flashBtn(btn):
    btn.config(bg="red")
    window.after(100, lambda: btn.config(bg="white"))
    window.after(200, lambda: btn.config(bg="red"))
    window.after(300, lambda: btn.config(bg="white"))


def merge():
    global merger, pdfFiles, lbl1, lbl2
    if len(pdfFiles)>1:
        lbl1 = Label(window, text="Merging...")
        lbl1.pack()
        for file in pdfFiles:
            pdfFile = open(file, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFile)
            merger.append(pdfReader)
        pdfFile.close()
        lbl2 = Label(window, text="Merged")
        lbl2.pack()

    svBtn['bg'] = "red"
    svBtn['fg'] = "white"
    svBtn['command'] = save
    pdfFiles.clear()

def save():
    global lbl, lbl1, lbl2, pdfFiles, no_of_files
    destinatin = filedialog.askdirectory(title="Choose Folder or Directory to save Your merged PDF")
    file = destinatin+"/mergedPDF.pdf"
    merger.write(file)
    window.destroy()
    prompt()    

def prompt():
    pw = Tk()
    pw.minsize(300, 90)
    pw.title("Prompt")
    lbl = Label(pw, text = "Your pdf files have been merged and saved succesfully. Do you want to merge more pdf files?")
    lbl.pack()
    noBtn = Button(pw, text="No", command=lambda:[pw.destroy()])
    noBtn.pack(side=LEFT, padx=100)
    yesBtn = Button(pw, text="Yes", command=lambda:[pw.destroy(), main()])
    yesBtn.pack(side=RIGHT, padx=100)
    pw.mainloop()

def main():
    global pdfFiles, no_of_files, file, merger, window, brsBtn, mrgBtn, svBtn
    pdfFiles = []
    no_of_files = 0
    file = ""
    merger = PyPDF2.PdfMerger()
    window = Tk()
    frame = Frame(window)
    frame.pack()
    window.minsize(600, 600)
    window.title('PDF File Merger')
    brsBtn = Button(text="Choose Files", command=lambda:[browseFile(file, pdfFiles)], bg="white")
    brsBtn.pack()

    mrgBtn = Button(text="Merge", command=lambda:[flashBtn(brsBtn)], bg="white")
    mrgBtn.pack()

    svBtn = Button(text="Save", command=lambda:[flashBtn(mrgBtn)], bg="white")
    svBtn.pack()
    window.mainloop()

main()
