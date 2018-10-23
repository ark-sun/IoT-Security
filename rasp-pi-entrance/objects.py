


objects = {'gateway_buttons':'2607:f2c0:e344:a02::3:2',
           'gateway_buttons_0':'2607:f2c0:e344:a03:3::1:0',
           'gateway_buttons_1':'2607:f2c0:e344:a03:3::1:1',
           'gateway_buttons_2':'2607:f2c0:e344:a03:3::1:2',
           'gateway_buttons_3':'2607:f2c0:e344:a03:3::1:3',
           'entrance_rfid':'2607:f2c0:e344:a02::2:2',
           'entrance_rfid_cards':'2607:f2c0:e344:a03:1::/88',
           'entrance_lock':'2607:f2c0:e344:a02::2:3',
           'light_relay':'2607:f2c0:e344:a02::2:2'}
objects_name_ip = objects
objects_ip_name = {v: k for k,v in objects.items()}

persons = {'anyone':'::',
           'ark':'2607:f2c0:e344:a03:2::1',
           'alice':'2607:f2c0:e344:a03:2::2',
           'bob':'2607:f2c0:e344:a03:2::3',
           'eve':'2607:f2c0:e344:a03:2::4'}
persons_name_ip = persons
persons_ip_name = {v: k for k,v in persons.items()}


what = {'nothing':2000,'push':2002,'scan':2003}
what_name_ip = what
what_ip_name = {v: k for k,v in what.items()}

how = {'nothing':1000,'on':1001,'off':1002,'unlock':1003}
how_name_ip = how
how_ip_name = {v: k for k,v in how.items()}





rule101 = [()]
rule102 = []

rules = { 101:rule101,
          102:rule102}
           
