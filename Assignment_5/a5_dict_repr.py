# Functions to deal with complex numbers -- dict representation - 5 + 7i --> {'r': 5, 'i': 7}
def get_real(a:list):
    return a['real']

def get_img(a:list):
    return a['img']

def set_real(a:dict, r:float):
    a['real'] = r
    return a

def set_img(a:dict, i:float):
    a['img'] = i
    return a

def create_complex(r, i: float):
    return {'real': r, 'img': i}