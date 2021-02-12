import pyttsx3
import PyPDF2
import pdftotext

book = open('book.pdf', 'rb')
pdfReader = pdftotext.PDF(book)
# pages = pdfReader.numPages

speaker = pyttsx3.init()


rate = speaker.getProperty('rate')
print(rate)
speaker.setProperty('rate', 140)


for page in range(11, 19):
    print(page)
    speaker.say(pdfReader[page])
    print(pdfReader[page])

    speaker.runAndWait()
