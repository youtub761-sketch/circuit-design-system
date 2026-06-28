import schemdraw
from schemdraw.elements import Ic, IcPin
from schemdraw import logic

def get_circuit_drawing(equations):
    d = schemdraw.Drawing()
    d.config(color='white')
    
    # 建立 JK Flip-Flop
    jk = d.add(Ic(pins=[
        IcPin(name='J1', side='left', slot='1/8'),
        IcPin(name='K1', side='left', slot='3/8'),
        IcPin(name='J0', side='left', slot='5/8'),
        IcPin(name='K0', side='left', slot='7/8')
    ], name='JK-FF'))
    
    # ... (這裡保留你原本定義的 draw_logic 函數) ...
    
    # 執行繪製邏輯...
    # (確保這裡沒有 d.save() 或其他繪圖指令)
    
    return d  # 這裡只回傳 Drawing 物件，不要呼叫 draw()
