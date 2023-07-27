import pyttsx3,PyPDF2

rootfolder = "C:\\Prueba\\"
destinationfolder= "C:\\Prueba\\"

#insert name of your pdf 
pdfreader = PyPDF2.PdfReader(open(rootfolder+'Lab.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
#name mp3 file whatever you would like
speaker.save_to_file(clean_text, destinationfolder+'story.mp3')
speaker.runAndWait()

speaker.stop()
