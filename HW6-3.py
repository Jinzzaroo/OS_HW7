#두 개의 탭화면과 윈도우 아이콘 바꾸기

from tkinter import*
from tkinter import ttk    #확장 모듈

##2019038030 김진영

window = Tk()
#윈도우 창의 왼쪽 상단에 뜨는 아이콘 바꾸기
#이 때 해당 아이콘 파일이 같은 파일에 있어야 한다.
window.iconbitmap('python.ico')

#탭을 만들 수 있게 설정
baseTab = ttk.Notebook(window)

#강아지와 고양이 탭 생성
tabDog = ttk.Frame(baseTab)
baseTab.add(tabDog, text='강아지')
tabCat = ttk.Frame(baseTab)
baseTab.add(tabCat, text = '고양이')

#탭 표시
baseTab.pack(expand=1, fill="both")

#강아지 사진 레이블을 강아지 탭에 붙임
photoDog = PhotoImage(file = "gif/dog7.gif")
labelDog = Label(tabDog, image = photoDog)
labelDog.pack()

#고양이 사진 레이블을 고양이 탭에 붙임
photoCat = PhotoImage(file = "gif/cat5.gif")
labelCat = Label(tabCat, image = photoCat)
labelCat.pack()

window.mainloop()
