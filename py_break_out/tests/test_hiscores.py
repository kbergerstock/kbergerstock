# test functonsliity for hiscores

from hiscores import Hiscores

def test_file_not_found():
    hs = Hiscores('cat.txt')
    assert hs.read() == False
    
    
def test_create():
    hs = Hiscores('cat.csv')    
    assert hs.create() == True  
    assert hs.write() == True
    
    
def test_read():
    hs = Hiscores('cat.csv')
    assert hs.read() == True
    table = hs.get()
    assert table[0][2] == 368
    assert table[9][2] == 269
    
    
def test_update_top():   
    hs = Hiscores('cat.csv')
    assert hs.read() == True
    hs.update('brk', 401)
    table = hs.get()
    assert table[0][2] == 401
    assert table[1][2] == 368
    hs.update('mse', 399)
    table = hs.get()
    assert table[0][2] == 401
    assert table[1][2] == 399
    assert table[2][2] == 368
    hs.update('mse', 399)
    table = hs.get()
    assert table[0][2] == 401
    assert table[1][2] == 399
    assert table[2][2] == 399
    assert table[3][2] == 368

def test_update_bottom():   
    hs = Hiscores('cat.csv')
    assert hs.read() == True
    hs.update('brk', 314)
    table = hs.get()
    assert table[7][2] == 314
    assert table[8][2] == 305
    assert table[9][2] == 288
    hs.update('mse', 310)
    table = hs.get()
    assert table[7][2] == 314
    assert table[8][2] == 310
    assert table[9][2] == 305
    
def test_check():
    hs = Hiscores('cat.csv')
    assert hs.read() == True
    assert hs.check(1) == False
    assert hs.check(200) == False
    assert hs.check(350) == True
    assert hs.check(400) == True