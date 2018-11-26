from datetime import datetime
from model import rekening as RekeningModel

# cari sebuah rekening
print (RekeningModel.find_one_by_id('03081170007'))

# contoh transfer
my_rekening_1 = RekeningModel.find_one_by_id('03081170007')
my_rekening_2 = RekeningModel.find_one_by_id('03081170008')
my_rekening_1['saldo'] -= 500000
my_rekening_2['saldo'] += 500000
RekeningModel.update_one_by_id('03081170007', my_rekening_1)
RekeningModel.update_one_by_id('03081170008', my_rekening_2)

# contoh setor
my_rekening = RekeningModel.find_one_by_id('03081170007')
my_rekening['saldo'] += 700000
RekeningModel.update_one_by_id('03081170007', my_rekening)
