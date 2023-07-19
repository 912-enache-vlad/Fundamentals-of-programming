# Functions to deal with complex numbers -- list representation - 5 + 7i --> [5, 7]


def get_real(a):
    return a[0]

def get_img(a):
    return a[1]

def set_real(a:list, r:float):
    a[0] = r
    return a

def set_rimg(a:list, i:float):
    a[0] = i
    return a

def create_complex(r, i: float):
    return [r, i]