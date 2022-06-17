from tkinter import *
import customtkinter
from tkinter.filedialog import askopenfile
import PyPDF2
from PIL import Image, ImageTk

# window = tk.Tk()
customtkinter.set_appearance_mode("")
customtkinter.set_default_color_theme("blue")
window = customtkinter.CTk()
window.iconbitmap("image\pdf.ico")
window.title("PDF TO TEXT EXTRACTOR")
canvas = customtkinter.CTkCanvas(window, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open("image/PDF-Editor.webp")
logo = ImageTk.PhotoImage(logo)
logo_label = customtkinter.CTkLabel(image=logo)
logo_label.Image = logo
logo_label.grid(column=1, row=0)

# Instructions
instrutions = customtkinter.CTkLabel(
    window,
    text="Select a PDF files on your computer to extract all its text",
    text_font="bold")
instrutions.grid(columnspan=3, column=0, row=1)

browse_text = StringVar()


def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=window, mode="rb",
                       title="Choose a file", filetypes=[("Pdf file", "*.Pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(1)
        page_content = page.extractText()
        text_box = Text(window, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.grid(column=1, row=3)
    else:
        browse_text.set("Browse")


# browse button
browse_btn = customtkinter.CTkButton(window, textvariable=browse_text,
                                     text_font="bold", command=lambda: open_file(),
                                     bg_color="#CB0038", fg_color="#CB0038",
                                     hover_color="#D6E2E7", height=2, width=10)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)


canvas = customtkinter.CTkCanvas(window, width=600, height=50)
canvas.grid(columnspan=3)
window.mainloop()
