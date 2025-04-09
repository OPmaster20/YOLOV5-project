import pymysql
import re,time
import json

db = pymysql.connect(host="localhost",port=3306,user="root"
                     ,password="root",db="userwindows",charset="utf8mb4")

cursor = db.cursor()
tmp_username = ""
tmp_password = ""

def user_search(username = None, password = None):
    print(username + password)
    if username is None or password is None:
        return False

    search = "select idUser from user where nameUser = \'" + username + "\' and passwordUser = \'" + password + "\';"
    cursor.execute(search)
    if len(cursor.fetchall()) == 0:
        print("No any information")
        return False

    cursor.execute(search)
    if cursor.fetchall()[0][0] != 0:
        global tmp_username,tmp_password
        tmp_username = username
        tmp_password = password
        return True
    return False

def user_insert(username = None,password = None,email = None,turecode = None,usercode = None):
    if user_search(username,password):
        print("Same")
        return False

    if usercode is None or email is None:
        print("None")
        return False

    if str(turecode).upper() != str(usercode).upper():
        print("Incorrect")
        return False

    if len(username) > 15:
        print("Too longer")
        return False

    if not re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",email):
        print("Worry email")
        return False

    if not re.match("^[a-zA-Z0-9]{1,10}$",password):
        print("Invaild password")
        return False

    Insertuser = "insert into user(nameUser,passwordUser,EmailAddres) values(\'" + username + "\',\'" + password + "\',\'" + email + "\');"
    Insertsys = "insert into sys(loginin,loginout,power,times) values(\'" + str(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())) + "\',\'None\',1,0);"
    try:
        cursor.execute(Insertuser)
        db.commit()
        cursor.execute(Insertsys)
        db.commit()
        print("insert success")
    except:
        db.rollback()
        print("insert failed")
        return False

    userdict = {"Username": username, "Password": password, "E_mail": email}
    data = json.dumps(userdict)
    with open("user.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=4))
        return True



def user_modify(newpassword = None,useremail = None):
    global tmp_username,tmp_password
    modify_password = "update user set passwordUser = \'" + newpassword + "\' where EmailAddres = \'" + useremail + "\';"
    print(modify_password)
    try:
        cursor.execute(modify_password)
        db.commit()
        print("success")
    except:
        db.rollback()
        print("failed")


def user_verify(email = None,un = None,pw = None):
    global tmp_username, tmp_password
    if un is None and pw is None:
        search = "select EmailAddres from user where nameUser = \'" + tmp_username + "\' and passwordUser = \'" + tmp_password + "\';"
        cursor.execute(search)
        if email == cursor.fetchall()[0][0]:
            return True
        return False
    else:
        verify = "select idUser from user where nameUser = \'" + un + "\' and passwordUser = \'" + pw + "\';"
        cursor.execute(verify)
        if len(cursor.fetchall()) == 0:
            return False
        return True

def user_update(select_n = 0,User = "",Pass = ""):
    if not user_verify(un=User,pw=Pass):
        return

    if select_n == 0:
        topup1 = "update sys,user set power = 2,times = times + 15 where sys.sysid = user.idUser and user.nameUser = \'" + User + "\' and user.passwordUser = \'" + Pass + "\';"
        cursor.execute(topup1)
        db.commit()
    elif select_n == 2:
        topup2 = "update sys,user set power = 3,times = times + 30 where sys.sysid = user.idUser and user.nameUser = \'" + User + "\' and user.passwordUser = \'" + Pass + "\';"
        cursor.execute(topup2)
        db.commit()
    elif select_n == 4:
        topup3 = "update sys,user set power = 4,times = times + 50 where sys.sysid = user.idUser and user.nameUser = \'" + User + "\' and user.passwordUser = \'" + Pass + "\';"
        cursor.execute(topup3)
        db.commit()
    else:
        topup4 = "update sys,user set times = times + 10 where sys.sysid = user.idUser and user.nameUser = \'" + User + "\' and user.passwordUser = \'" + Pass + "\';"
        cursor.execute(topup4)
        db.commit()




def user_detecttimes():
    global tmp_username,tmp_password
    detect = "update sys,user set times = times - 1 where sys.sysid = user.idUser and user.nameUser = \'" + tmp_username + "\' and user.passwordUser = \'" + tmp_password + "\';"
    cursor.execute(detect)
    db.commit()

def user_infor_tranfer(n = 0):
    global tmp_username,tmp_password
    if n == 1:
        lookfortimes = ("select times from sys,user "
                        "where user.idUser = sys.sysid and user.nameUser = \'") + tmp_username +  "\' and user.passwordUser = \'" + tmp_password + "\';"
        cursor.execute(lookfortimes)
        return cursor.fetchall()[0][0]
    elif n == 2:
        return tmp_username
    elif n == 3:
        lookforlogin = ("select sys.loginin from sys,user "
                        "where user.idUser = sys.sysid and user.nameUser = \'") + tmp_username + "\' and user.passwordUser = \'" + tmp_password + "\';"
        cursor.execute(lookforlogin)
        return cursor.fetchall()[0][0]
    elif n == 4:
        lookforusetime = ("select times from sys,user "
                        "where user.idUser = sys.sysid and user.nameUser = \'") + tmp_username + "\' and user.passwordUser = \'" + tmp_password + "\';"
        cursor.execute(lookforusetime)
        return cursor.fetchall()[0][0]
    elif n == 5:
        lookfortype = ("select power from sys,user "
                          "where user.idUser = sys.sysid and user.nameUser = \'") + tmp_username + "\' and user.passwordUser = \'" + tmp_password + "\';"
        cursor.execute(lookfortype)
        type = int(cursor.fetchall()[0][0])
        if type == 1:
            return "Standard User"
        elif type == 2:
            return "Bronze Member"
        elif type == 3:
            return "Silver Member"
        elif type == 4:
            return "Gold Member"
        else:
            return "Standard User"

    else:
        return "None"

def user_isstandarduser():
    lookfortype = ("select power from sys,user "
                   "where user.idUser = sys.sysid and user.nameUser = \'") + tmp_username + "\' and user.passwordUser = \'" + tmp_password + "\';"
    cursor.execute(lookfortype)
    type = int(cursor.fetchall()[0][0])
    if type == 1:
        return True
    else:
        return False
def user_delete():
    global tmp_username,tmp_password
    if len(tmp_username) > 0:
        getuserid = "select idUser from user,sys where user.idUser = sys.sysid and user.nameUser = \'" + tmp_username + "\' and user.passwordUser = \'" + tmp_password + "\';"
        cursor.execute(getuserid)
        currentuserid = cursor.fetchall()[0][0]
        print(currentuserid)

        update = "set SQL_SAFE_UPDATES = 0;"
        cursor.execute(update)
        db.commit()

        delsys = "delete from sys where sysid = " + str(currentuserid) + ";"
        deluser = "delete from user where nameUser = \'" + tmp_username + "\' and passwordUser = \'" + tmp_password + "\';"
        cursor.execute(delsys)
        db.commit()

        cursor.execute(deluser)
        db.commit()

def user_exit():
    print("Exit successfully")
    db.close()

user_delete()