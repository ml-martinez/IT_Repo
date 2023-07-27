import os

downloadsFolder = "C:\\Prueba\\"

imageFolder = "C:\\Prueba\\Images\\"
AudioFolder = "C:\\Prueba\\Audio\\"
VideoFolder = "C:\\Prueba\\Video\\"
pdfFolder = "C:\\Prueba\\PDF\\"
xlsFolder = "C:\\Prueba\\Excel\\"


if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            os.rename(downloadsFolder + filename, imageFolder + filename)

        if extension in [".mp4"]:
            os.rename(downloadsFolder + filename, VideoFolder + filename)

        if extension in [".mp3"]:
            os.rename(downloadsFolder + filename, AudioFolder + filename)

        if extension in [".xls",".xlsx",".csv"]:
            os.rename(downloadsFolder + filename, xlsFolder + filename)

        if extension in [".pdf"]:
            os.rename(downloadsFolder + filename, pdfFolder + filename)


