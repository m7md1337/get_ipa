# coding=utf-8
# بسم الله
# thanks dracula711
import lxml
import requests
import re
import wget
import json
import os
from bs4 import BeautifulSoup



def clearr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def download(idapp):
    req = requests.get("https://m7md1337.000webhostapp.com/2.php?id={}".format(idapp),headers={"m7md1337":"102"},verify=False)
    soo = json.loads(req.content)
    if soo["cc"] == "true":
        wget.download(soo["url"], soo["filename"])
        print("file has been downloaded", soo["filename"])
        exit()
    elif soo["cc"] == "false":
        print(soo["massage"],"try another version")
    else:
        print("error : something happens ")
        exit()


def get_versions(idd):
    url = "https://tools.lancely.tech/apple/app-version/US/{}".format(idd,verify=False)

    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    check = soup.find_all('code')[0].get_text()
    finda = soup.find_all('tr', attrs={'style': 'cursor:auto;'})
    version = re.findall(r'(?:(\d+\.(?:\d+\.)*\d+))', str(finda))
    reee = re.findall('>([0-9.]+)<\/td><\/tr>', str(finda))
    leng = len(version)
    count = 0
    if int(check) > 0:
        while count < int(leng):
            print("-{} : ({}) v{}".format(count, reee[count], version[count]))
            count += 1

        askme = input("\n\nplease Enter number : ")
        req = requests.get("https://m7md1337.000webhostapp.com/2.php?id={}&version={}".format(idd,reee[int(askme)]),headers={"m7md1337":"102"})
        soo = json.loads(req.content)
        if soo["cc"] == "true":
            wget.download(soo["url"], "v-"+version[int(askme)]+"-"+soo["filename"])

            print("\n\n\n","file has been downloaded", "v-"+version[int(askme)]+"-"+soo["filename"])
            exit()
        elif soo["cc"] == "false":

            print(soo["massage"])
        else:
            print("error : something happens ")
            exit()
    elif check == "0":
        clearr()
        print("no versions available for this app go again chose last version")


def byid(byyidd):
    req1 = requests.get("https://itunes.apple.com/lookup?id={}".format(byyidd),verify=False)
    bbo22 = json.loads(req1.content)
    if bbo22["resultCount"] == 0:
        print("you but a wrong id try again or another way")
    elif bbo22["resultCount"] == 1:
        for zz11 in bbo22["results"]:
            print("name: {} - bundel id: ({}) id: {}".format( zz11["trackName"], zz11["bundleId"], zz11["trackId"]))
        print("""
            1.download last version 
            2.download specific version 
            """)
        bb6 = input("1 or 2 ?: ")
        if bb6 == "1":
            download(zz11["trackId"])
        elif bb6 == "2":
            get_versions(zz11["trackId"])
        else:
            clearr()
            print("\n Not Valid Choice Try again or another way")




def seacrh(terms):
    re = requests.get("https://itunes.apple.com/search?term=" + terms + "&media=software")
    dataseach = json.loads(re.content)
    if dataseach["resultCount"] == 0:
        print("we can't find it try again or another way ")
    else:
        times = dataseach["resultCount"]
        count = 0
        mylist = []
        for zz in dataseach["results"]:
            print("{} - name:{} - bundel id:({}) id:{}".format(count, zz["trackName"], zz["bundleId"], zz["trackId"]))
            mylist.append(zz["trackId"])
            count += 1

        ask = int(input("\n\nplease Enter A number : "))
        clearr()
        print("""
    1.download last version 
    2.download specific version 
    """)
        bb6 = input("1 or 2 ?: ")
        if bb6 == "1":
            download(mylist[ask])
        elif bb6 == "2":
            clearr()
            print("wait")
            clearr()
            get_versions(mylist[ask])
        else:
            clearr()
            print("\n Not Valid Choice Try again")

def bybundel(bundel):
    req = requests.get("https://itunes.apple.com/lookup?bundleId={}".format(bundel))
    bbo = json.loads(req.content)
    if bbo["resultCount"] == 0:
        print("you but a wrong bundelid")
    elif bbo["resultCount"] == 1:
        for zz in bbo["results"]:
            print("name: {} - bundel id: ({}) id: {}".format( zz["trackName"], zz["bundleId"], zz["trackId"]))
        print("""
            1.download last version 
            2.download specific version 
            """)
        bb6 = input("1 or 2 ?: ")
        if bb6 == "1":
            download(zz["trackId"])
        elif bb6 == "2":
            clearr()
            get_versions(zz["trackId"])
        else:
            clearr()
            print("\n Not Valid Choice Try again")


mmm1 = True
while mmm1:
    print ("""
    1.get the app ipa by search 
    2.get the app ipa by bundleId 
    3.get the app by id
    4.Exit/Quit
    """)
    mmm = input("What would you like to do? ")
    if mmm == "1":
        clearr()
        c = input("what the name the app: ")
        clearr()
        seacrh(c)
    elif mmm == "2":
        clearr()
        p = input("what the bundelid for app: ")
        clearr()
        bybundel(p)
    elif mmm == "3":
        clearr()
        q = input("what the id for app: ")
        clearr()
        byid(q)
    elif mmm == "4":
        exit()
    elif mmm != "":
        print("\n Not Valid Choice Try again")
