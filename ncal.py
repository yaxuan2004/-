import PySimpleGUI as g


def cal(text):
    try:
        res=eval(text)
        return res
    except:
        print("算式输入错误")
        # return
        g.popup("算式输入错误")

layout=[
    [g.Text(text="请输入算式:",auto_size_text=True),
    g.InputText(focus=True,key="ss_in")],
    [g.Text(text="结果:",auto_size_text=True),
    
    g.Text("0",key="res_out",auto_size_text=False)],
    [g.Button('计算',key='cal_b'),
    g.Button('离开')]
]
99
window=g.Window("简便计算器",layout=layout,keep_on_top=True,
                auto_close=False,resizable=False, disable_close=True)

while True:
    event,values=window.read()
    if event=='离开':
        break
    elif event=='cal_b':
        text=values['ss_in']
        res=str(cal(text))
        print(res)
        window['res_out'].update(res)
        
window.close()      


