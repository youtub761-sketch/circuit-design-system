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
    
    def draw_logic(d, target_pin, eq):
        eq = eq.replace(' ', '')
        if '&' in eq:
            parts = eq.split('&')
            g = d.add(logic.And(inputs=2).right().at(target_pin).anchor('out'))
            d.add(logic.Line().at(g.in1).left().label(parts[0], loc='left', color='white'))
            d.add(logic.Line().at(g.in2).left().label(parts[1], loc='left', color='white'))
        elif '|' in eq:
            parts = eq.split('|')
            g = d.add(logic.Or(inputs=2).right().at(target_pin).anchor('out'))
            d.add(logic.Line().at(g.in1).left().label(parts[0], loc='left', color='white'))
            d.add(logic.Line().at(g.in2).left().label(parts[1], loc='left', color='white'))
        else:
            d.add(logic.Line().at(target_pin).left().label(eq, loc='left', color='white'))

    draw_logic(d, jk.J1, equations.get('J1', '0'))
    draw_logic(d, jk.K1, equations.get('K1', '0'))
    draw_logic(d, jk.J0, equations.get('J0', '0'))
    draw_logic(d, jk.K0, equations.get('K0', '0'))
    
    return d  # 【關鍵修改】：回傳 drawing 物件給網頁
