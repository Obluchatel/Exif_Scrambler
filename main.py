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
    root.newfile = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                 filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    print(root.newfile)


def show_exif():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    im = Image.open(root.filename)
    exif_dict = piexif.load(im.info["exif"])
    # process im and exif_dict...
    # w, h = im.size
    # exif_dict["0th"][piexif.ImageIFD.XResolution] = (w, 1)
    # exif_dict["0th"][piexif.ImageIFD.YResolution] = (h, 1)
    # exif_bytes = piexif.dump(exif_dict)
    # print(exif_bytes)
    print(exif_dict)
    print("printing EXIF's 0th")
    print(exif_dict['0th'])
    print("printing EXIF's Exif")
    print(exif_dict['Exif'])
    print("printing EXIF's GPS")
    print(exif_dict['GPS'])
    print("printing EXIF's Interop")
    print(exif_dict["Interop"])
    print("printing EXIF's 1st")
    print(exif_dict["1st"])
    print("printing EXIF's Thumbnails")
    print(exif_dict["thumbnail"])

    # im.save(new_file, "jpeg", exif=exif_bytes)



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

show_exif_data = Button(root, text="Show EXIF data", command=show_exif)
show_exif_data.grid(row=0, column=5, padx=15)

root.mainloop()
