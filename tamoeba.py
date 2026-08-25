from googletrans import Translator
from tkinter import *
from tkinter import messagebox

def trf():
    src_v = src_entry.get("1.0", "end-1c").strip().lower() or None
    dest_v = dest_entry.get("1.0", "end-1c").strip().lower() or None
    text_v = text_entry.get("1.0", "end-1c").strip()

    if not text_v:
        messagebox.showerror(message="Enter valid text")
        return

    try:
        if not src_v and not dest_v:
            translated_text = translator_object.translate(text_v)
        elif not src_v:
            translated_text = translator_object.translate(text_v, dest=dest_v)
        elif not dest_v:
            translated_text = translator_object.translate(text_v, src=src_v)
        else:
            translated_text = translator_object.translate(text_v, src=src_v, dest=dest_v)

        messagebox.showinfo(message="Translated text:\n" + translated_text.text)
    except Exception as e:
        messagebox.showerror(message=f"Translation failed: {str(e)}")

def clear():
    dest_entry.delete("1.0", "end-1c")
    src_entry.delete("1.0", "end-1c")
    text_entry.delete("1.0", "end-1c")

window = Tk()
window.geometry("550x300")
window.title("Translator")

translator_object = Translator()

# Title Label
Label(window, text="Language Translator using Python", font=("Calibri", 14, "bold")).pack(pady=10)

# Text to Translate
Label(window, text="Text to translate:").place(x=10, y=60)
text_entry = Text(window, width=40, height=3, font=("Calibri", 12))
text_entry.place(x=150, y=60)

# Source Language
Label(window, text="Translate from (e.g., 'en') :").place(x=10, y=140)
src_entry = Text(window, width=20, height=1, font=("Calibri", 12))
src_entry.place(x=250, y=140)

# Destination Language
Label(window, text="Translate to (e.g., 'fr') :").place(x=10, y=170)
dest_entry = Text(window, width=20, height=1, font=("Calibri", 12))
dest_entry.place(x=250, y=170)

# Buttons
Button(window, text='Translate', bg='gray', command=trf).place(x=160, y=220)
Button(window, text='Clear', bg='gray', command=clear).place(x=270, y=220)

window.mainloop()
