import tkinter as tk

x = 1024
y = 720
zoom_size = 24
subsample_size = 30

size = str(x) + "x" + str(y)
root = tk.Tk()
root.title('DHL')
root.geometry(size)
root.resizable(False, False)
frame = tk.Frame(root, bd = 5, bg='white', relief = 'groove')
frame.pack()

b_frame = tk.Frame(frame, width = x * 1, height = y * 0.166)
b_frame.grid(row = 0, column = 0, columnspan = 5)

jon = 10
si = 6
b1_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166, bg='red')
b1_frame.pack(side = tk.LEFT)

b1_btn = tk.Button(b1_frame, text="선택", width = jon, height = si).pack()

b2_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='orange')
b2_frame.pack(side = tk.LEFT)
tk.Button(b2_frame, text="선택", width = jon, height = si).pack()

b3_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='yellow')
b3_frame.pack(side = tk.LEFT)
tk.Button(b3_frame, text="선택", width = jon, height = si).pack()

b4_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='green')
b4_frame.pack(side = tk.LEFT)
tk.Button(b4_frame, text="선택", width = jon, height = si).pack()

b5_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='blue')
b5_frame.pack(side = tk.LEFT)
tk.Button(b5_frame, text="선택", width = jon, height = si).pack()

b6_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='navy')
b6_frame.pack(side = tk.LEFT)
tk.Button(b6_frame, text="선택", width = jon, height = si).pack()

b7_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='blue')
b7_frame.pack(side = tk.LEFT)
tk.Button(b7_frame, text="선택", width = jon, height = si).pack()

b8_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='green')
b8_frame.pack(side = tk.LEFT)
tk.Button(b8_frame, text="선택", width = jon, height = si).pack()

b9_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='yellow')
b9_frame.pack(side = tk.LEFT)
tk.Button(b9_frame, text="선택", width = jon, height = si).pack()

b10_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='orange')
b10_frame.pack(side = tk.LEFT)
tk.Button(b10_frame, text="선택", width = jon, height = si).pack()

global select_user, l1_btn
select_user = -1
def test(num):
    global select_user
    select_user = num
l1_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
l1_frame.grid(row = 1, column = 0)
l1_btn = tk.Button(l1_frame, text = "선택", width = 10, height = 5, command=lambda: test(1))
l1_btn.pack(side=tk.LEFT)
l1_line = tk.Label(l1_frame, width = 5, height = 5, text="1번").pack(side=tk.LEFT)

l2_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
l2_frame.grid(row = 2, column = 0)
l2_btn = tk.Button(l2_frame, text = "선택", width = 10, height = 5, command=lambda: test(2))
l2_btn.pack(side=tk.LEFT)
l2_line = tk.Label(l2_frame, width = 5, height = 5, text="2번").pack(side=tk.LEFT)

l3_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
l3_frame.grid(row = 3, column = 0)
l3_btn = tk.Button(l3_frame, text = "선택", width = 10, height = 5, command=lambda: test(3))
l3_btn.pack(side=tk.LEFT)
l3_line = tk.Label(l3_frame, width = 5, height = 5, text="3번").pack(side=tk.LEFT)

l4_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
l4_frame.grid(row = 4, column = 0)
l4_btn = tk.Button(l4_frame, text = "선택", width = 10, height = 5, command=lambda: test(4))
l4_btn.pack(side=tk.LEFT)
l4_line = tk.Label(l4_frame, width = 5, height = 5, text="4번").pack(side=tk.LEFT)

l5_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
l5_frame.grid(row = 5, column = 0)
l5_btn = tk.Button(l5_frame, text = "선택", width = 10, height = 5, command=lambda: test(5))
l5_btn.pack(side=tk.LEFT)
l5_line = tk.Label(l5_frame, width = 5, height = 5, text="5번").pack(side=tk.LEFT)

m_frame = tk.Frame(frame, width = x * 0.6, height = y * 0.668, bg='purple')
m_frame.grid(row = 1, column = 1, rowspan = 4)

r1_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
r1_frame.grid(row = 1, column = 4)
r1_btn = tk.Button(r1_frame, text = "선택", width = 10, height = 5, command=lambda: test(6))
r1_btn.pack(side=tk.RIGHT)
r1_line = tk.Label(r1_frame, width = 5, height = 5, text="1번").pack(side=tk.RIGHT)

r2_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
r2_frame.grid(row = 2, column = 4)
r2_line = tk.Label(r2_frame, width = 5, height = 5, text="2번").pack(side=tk.LEFT)
r2_btn = tk.Button(r2_frame, text = "선택", width = 10, height = 5, command=lambda: test(7))
r2_btn.pack(side=tk.LEFT)

r3_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
r3_frame.grid(row = 3, column = 4)
r3_line = tk.Label(r3_frame, width = 5, height = 5, text="3번").pack(side=tk.LEFT)
r3_btn = tk.Button(r3_frame, text = "선택", width = 10, height = 5, command=lambda: test(8))
r3_btn.pack(side=tk.LEFT)

r4_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
r4_frame.grid(row = 4, column = 4)
r4_line = tk.Label(r4_frame, width = 5, height = 5, text="4번").pack(side=tk.LEFT)
r4_btn = tk.Button(r4_frame, text = "선택", width = 10, height = 5, command=lambda: test(9))
r4_btn.pack(side=tk.LEFT)

r5_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
r5_frame.grid(row = 5, column = 4)
r5_line = tk.Label(r5_frame, width = 5, height = 5, text="5번").pack(side=tk.LEFT)
r5_btn = tk.Button(r5_frame, text = "선택", width = 10, height = 5, command=lambda: test(10))
r5_btn.pack(side=tk.LEFT)

option_frame = tk.Frame(frame, width = x * 0.6, height = y * 0.166, bg='white')
option_frame.grid(row = 5, column = 1)

line_frame = tk.Frame(option_frame, width = x * 0.61, height = y * 0.066, bg = "orange")
line_frame.grid(row = 1, column = 0)

CheckVariety = tk.IntVar()
top_btn = tk.Radiobutton(line_frame, text="탑", value = 0, width = 10, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)
jg_btn = tk.Radiobutton(line_frame, text="정글", value = 1, width = 10, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)
mid_btn = tk.Radiobutton(line_frame, text="미드", value = 2, width = 10, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)
ad_btn = tk.Radiobutton(line_frame, text="원딜", value = 3, width = 10, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)
sp_btn = tk.Radiobutton(line_frame, text="서폿", value = 4, width = 10, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)

choice_frame = tk.Frame(option_frame, width=x * 0.6, height=y * 0.1, bg="yellow")
choice_frame.grid(row=2, column=0)

rec_frame = tk.Frame(choice_frame, width=x * 0.6 * 0.33, height=y * 0.1, bg="green")
rec_frame.grid(row=0, column=0)
button_recommend = tk.Button(rec_frame, width=21, height=3, text="추천받기")
button_recommend.pack()

select_frame = tk.Frame(choice_frame, width=x * 0.6 * 0.34, height=y * 0.1, bg="yellow")
select_frame.grid(row=0, column=1)
button_pick = tk.Button(select_frame, width=26, height=3, text="선택하기")
button_pick.pack()

rec_text_frame = tk.Frame(choice_frame, width=x * 0.6 * 0.328, height=y * 0.1, bg="navy")
rec_text_frame.grid(row=0, column=2)
button_request = tk.Button(rec_text_frame, width=21, height=3, text="추천챔피언")
button_request.pack()

champion_list = ['가렌', '갈리오', '갱플랭크', '그라가스', '그레이브즈', '나르', '나미', '나서스', '노틸러스', '녹턴', '누누', '니달리', '니코', '다리우스',
                 '다이애나', '드레이븐', '라이즈', '라칸', '람머스', '럭스', '럼블', '레넥톤', '레오나', '렉사이', '렝가', '루시안', '룰루', '르블랑', '리 신',
                 '리븐', '리산드라', '릴리아', '마스터이', '마오카이', '말자하', '말파이트', '모데카이저', '모르가나', '문도 박사', '미스 포츈', '바드', '바루스',
                 '바이', '베이가', '베인', '벨코즈', '볼리베어', '브라움', '브랜드', '블라디미르', '블리츠크랭크', '빅토르', '뽀삐', '사미라', '사이온', '사일러스',
                 '샤코', '세나', '세라핀', '세주아니', '세트', '소나', '소라카', '쉔', '쉬바나', '스웨인', '스카너', '시비르', '신 짜오', '신드라', '신지드',
                 '쓰레쉬', '아리', '아무무', '아우렐리온 솔', '아이번', '아지르', '아칼리', '아트록스', '아펠리오스', '알리스타', '애니', '애니비아', '애쉬', '야스오',
                 '에코', '엘리스', '오공', '오른', '오리아나', '올라프', '요네', '요릭', '우디르', '우르곳', '워윅', '유미', '이렐리아', '이블린', '이즈리얼',
                 '일라오이', '자르반 4세', '자야', '자이라', '자크', '잔나', '잭스', '제드', '제라스', '제이스', '조이', '직스', '진', '질리언', '징크스',
                 '초가스', '카르마', '카밀', '카사딘', '카서스', '카시오페아', '카이사', '카직스', '카타리나', '칼리스타', '케넨', '케이틀린', '케인', '케일',
                 '코그모', '코르키', '퀸', '클레드', '키아나', '킨드레드', '타릭', '탈론', '탈리야', '탐 켄치', '트런들', '트리스타나', '트린다미어',
                 '트위스티드 페이트', '트위치', '티모', '파이크', '판테온', '피들스틱', '피오라', '피즈', '하이머딩거', '헤카림']

image_m = []
button_m = []

for i in range(len(champion_list)):
    image_m.append(tk.PhotoImage(file=champion_list[i] + '.png').zoom(zoom_size - 2).subsample(subsample_size))

canvas = tk.Canvas(m_frame)
canvas.grid(row=0, column=0, sticky="news")

scroll = tk.Scrollbar(m_frame, orient="vertical", command=canvas.yview)
scroll.grid(sticky='news', row=0, column=7)

canvas.configure(yscrollcommand=scroll.set)

frame_buttons = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')
selected = 0

for i in range(len(champion_list)):
    button_m.append(tk.Button(frame_buttons, image=image_m[i]))
    button_m[i].grid(row=int(i / 6), column=int(i % 6))

frame_buttons.update_idletasks()

firstcolumns_width = sum([button_m[i].winfo_width() for i in range(0, 6)])
firstrows_height = sum([button_m[i].winfo_height() for i in range(0, 5)])
m_frame.config(width=firstcolumns_width + scroll.winfo_width(), height=firstrows_height)
canvas.configure(width=firstcolumns_width + scroll.winfo_width(), height=firstrows_height)
canvas.config(scrollregion=canvas.bbox("all"))

line = ["탑", "정글", "미드", "원딜", "서폿"]
global select_champion_num, select_line_num
select_champion_num = -1
select_line_num = -1

def click_champion(num):
    global select_champion_num
    select_champion_num = num

for i, v in enumerate(champion_list):
    button_m[i].config(command=lambda idx=i: click_champion(idx))

def click_pick():
    global select_champion_num, select_line_num, select_user
    select_line_num = CheckVariety.get()
    if (select_user == -1):
        print('유저를 선택해주세요.')
    if (select_champion_num == -1):
        print('챔피언을 선택해주세요.')
    if (select_line_num == -1):
        print('라인을 정해주세요.')
    else:
        print('유저 : {0}   라인 : {1}   챔피언 : {2} 으로 선택되었습니다.'.format(select_user, line[select_line_num], champion_list[select_champion_num]))
        temp = tk.PhotoImage(tk.PhotoImage(file='가렌.png').zoom(zoom_size - 2).subsample(subsample_size))
        l1_btn.config(text = "안녕하세요.")
    ## pick 확정시 다른 챔피언 선택 가능하도록 다시 활성화.
button_pick.config(command=lambda: click_pick())

root.mainloop()