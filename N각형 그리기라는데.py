from tkinter import *  #모듈들을 임포트해주고
import math
 
root = Tk()
root.title(u"n각형 그리는 법이라네") #파일 제목을 써준다
 
N=600 #canvas의 크기

mypaper = Canvas(root, width=N,height=N, background ="light blue")  #그리고 창(캔버스)의 색과 크기
 
def draw_N(ox,oy,r,n):  #ox,oy는 원점좌표, r은 반지름, n은 n각형
    mypaper.create_text(ox,oy,font=(u"맑은고딕",20), fill="blue",text=str(n)+u"각형")  #n각형이라는 글자 폰트와 사이즈, 색 등
    total_angle_sum = (n-2)*math.pi #N각형에서 내각의 총합
    a=ox+r
    b =oy
    for i in range(n):
        #기준점(a,b)에서 삼각함수로 다음 점을 계산하여 서로 잇는다.
        mypaper.create_line(a,b,ox+r*math.cos((i+1)*(math.pi-total_angle_sum/n)),
        oy+r*math.sin((i+1)*(math.pi-total_angle_sum/n)),width=3)
 
        #a, b를 갱신
        a=ox+r*math.cos((i+1)*(math.pi-total_angle_sum/n))
        b=oy+r*math.sin((i+1)*(math.pi-total_angle_sum/n))
 
draw_N(300,300,200,3) # ox,oy,r,n순. 마지막 숫자가 n각형
mypaper.grid(row=0,column=0)
 
root.mainloop()

