# -*- coding: utf-8 -*-
import pickle

shop_list_file = 'shop_list.data'

shop_list = ['apple', 'mango', 'morkow']

f = open(shop_list_file, 'wb')
pickle.dump(shop_list, f)
f.close()

f = open(shop_list_file, 'rb')
stored_list = pickle.load(f)
print(stored_list)
