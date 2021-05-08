from tkinter import *
from tkinter import filedialog
from PIL import Image
import piexif

root = Tk()
root.title("Exif_Scrambler")
root.geometry("800x600")


def delete_exif():
    print("Finish it later!")


def scramble_exif():
    print("Finish it later!")


def quit_exit():
    root.destroy()


def select_image():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    print(root.filename)


def save_image():
    root.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                 filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    print(root.filename)


# im = Image.open(filename)
# exif_dict = piexif.load(im.info["exif"])
# # process im and exif_dict...
# w, h = im.size
# exif_dict["0th"][piexif.ImageIFD.XResolution] = (w, 1)
# exif_dict["0th"][piexif.ImageIFD.YResolution] = (h, 1)
# exif_bytes = piexif.dump(exif_dict)
# im.save(new_file, "jpeg", exif=exif_bytes)


delete_exif = Button(root, text="Delete exif data", command=delete_exif)
delete_exif.grid(row=0, column=0, padx=15)

scramble_exif = Button(root, text="Scramble exif data", command=scramble_exif)
scramble_exif.grid(row=0, column=1, padx=15)

quit_button = Button(root, text="Quit", command=quit_exit)
quit_button.grid(row=0, column=2, padx=15)

select_image = Button(root, text="Select image", command=select_image)
select_image.grid(row=0, column=3, padx=15)

save_image = Button(root, text="Save image", command=save_image)
save_image.grid(row=0, column=4, padx=15)

root.mainloop()
