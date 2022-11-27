import pytest
from redislab import Redis_Client
from traceback import print_stack

testr = Redis_Client()

def test_redisconnect():
    result = testr.connect()
    assert result is not None        

def test_loadusers():
   testr.connect()
   result = testr.load_users("../datasets/users.txt")
   assert(result!=None)
   assert(len(result)==5996)    

def test_loadscores():
   testr.connect()    
   result = testr.load_scores()
   assert(result!=None)
   assert(len(result)==5996)    

def test_query1():
    testr.connect()
    result = testr.query1(299)
    assert(result=={'first_name': 'Susie', 'last_name': 'Jendrys', 'email': 'sjendrys8a@webmd.com', 'gender': 'female', 'ip_address': '30.157.248.216', 'country': 'China', 'country_code': 'CN', 'city': 'Xuetian', 'longitude': '120.568856', 'latitude': '29.00091', 'last_login': '1571176806'})

def test_query2():
    testr.connect()
    result = testr.query2(2836)
    assert(result==[ "1.9638715", "47.9035673"])

# def test_query3():
#     testr.connect()
#     result = testr.query3()
#     assert(result==(['user:2370', 'user:2658', 'user:287'], ['Ruse', 'Hamor', 'Rewbottom']))

def test_query3supp():
    testr.connect()
    urskey_result, usrname_result = testr.query3()
    correct = 0
    for i in range(len(urskey_result)):
        usrkey = urskey_result[i].split(":")[1]
        prefix = ['2','4','6','8','0']
        if usrkey.startswith(tuple(prefix)):
            if usrname_result[i].isalpha():
                correct+=1
    assert(correct>=3)


# def test_query4():
#     testr.connect()
#     result = testr.query4()
#     answer = ("[Document {'id': 'user:1576', 'payload': None, 'first_name': 'Auguste', 'last_name': 'Relfe', 'email': 'arelfefz@tamu.edu', 'gender': 'female', 'ip_address': '116.141.9.64', 'country': 'Russia', 'country_code': 'RU', 'city': 'Divnoye', 'longitude': '43.3478599', 'latitude': '45.8697083', 'last_login': '1583966461'},"
#             +" Document {'id': 'user:1698', 'payload': None, 'first_name': 'Allix', 'last_name': 'Angier', 'email': 'aangierjd@cbc.ca', 'gender': 'female', 'ip_address': '208.35.28.88', 'country': 'Russia', 'country_code': 'RU', 'city': 'Krasnaya Polyana', 'longitude': '41.1051314', 'latitude': '45.05426', 'last_login': '1590203283'},"
#             +" Document {'id': 'user:1708', 'payload': None, 'first_name': 'Korrie', 'last_name': 'Riggey', 'email': 'kriggeyjn@scribd.com', 'gender': 'female', 'ip_address': '185.162.212.86', 'country': 'Russia', 'country_code': 'RU', 'city': 'Dinskaya', 'longitude': '39.3719039', 'latitude': '45.1242818', 'last_login': '1596064545'},"
#             +" Document {'id': 'user:1952', 'payload': None, 'first_name': 'Aline', 'last_name': 'Jedras', 'email': 'ajedrasqf@reverbnation.com', 'gender': 'female', 'ip_address': '246.189.60.56', 'country': 'Russia', 'country_code': 'RU', 'city': 'Novoaleksandrovsk', 'longitude': '41.1600688', 'latitude': '45.4885295', 'last_login': '1576576265'},"
#             +" Document {'id': 'user:5276', 'payload': None, 'first_name': 'Fancie', 'last_name': 'Gowers', 'email': 'fgowers7r@ovh.net', 'gender': 'female', 'ip_address': '103.144.195.63', 'country': 'Russia', 'country_code': 'RU', 'city': 'Korenovsk', 'longitude': '39.5186898', 'latitude': '45.4401623', 'last_login': '1575054324'},"
#             +" Document {'id': 'user:5280', 'payload': None, 'first_name': 'Eirena', 'last_name': 'McGunley', 'email': 'emcgunley7v@histats.com', 'gender': 'female', 'ip_address': '229.160.70.207', 'country': 'Russia', 'country_code': 'RU', 'city': 'Syktyvkar', 'longitude': '41.1199008', 'latitude': '45.0052663', 'last_login': '1586164090'},"
#             +" Document {'id': 'user:5698', 'payload': None, 'first_name': 'Carmella', 'last_name': 'Beevor', 'email': 'cbeevorjh@issuu.com', 'gender': 'female', 'ip_address': '207.31.141.104', 'country': 'Russia', 'country_code': 'RU', 'city': 'Temryuk', 'longitude': '37.3986836', 'latitude': '45.294498', 'last_login': '1579159273'},"
#             +" Document {'id': 'user:3944', 'payload': None, 'first_name': 'Hedda', 'last_name': 'Scamwell', 'email': 'hscamwellq9@bizjournals.com', 'gender': 'female', 'ip_address': '156.84.80.3', 'country': 'China', 'country_code': 'CN', 'city': 'Jiujianfang', 'longitude': '128.219871', 'latitude': '45.360768', 'last_login': '1572681083'},"
#             +" Document {'id': 'user:5655', 'payload': None, 'first_name': 'Goldarina', 'last_name': 'Bruford', 'email': 'gbrufordia@rakuten.co.jp', 'gender': 'female', 'ip_address': '241.213.113.136', 'country': 'China', 'country_code': 'CN', 'city': 'Da’an', 'longitude': '124.292626', 'latitude': '45.506995', 'last_login': '1581713762'}]")
#     assert(str(result.docs) == answer)

def test_query4supp():
    testr.connect()
    result = testr.query4()
    assert(len(result.docs)>=9)
    for doc in result.docs:
        assert(doc.country == "China" or doc.country == "Russia")
        assert(doc.gender == "female")
        lat = float(doc.latitude)
        assert(lat <= 46.0 and lat >= 45.0)


def test_query5():
    testr.connect()
    result = testr.query5()
    assert(result == ['hkarlolako0@arizona.edu', 'rpalleskelx@wikia.com', 'dpriddlecz@wp.com', 'ubouldn5@icio.us', 'tgerlerli@nymag.com', 'mrehmdw@bravesites.com', 'hcleggqd@imageshack.us', 'lmcvitty8t@typepad.com', 'cyoungsqy@acquirethisname.com', 'pslorancedm@ask.com'])
