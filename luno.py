#!/usr/bin/python3
import sys, os, urllib.request
from wget import download

class downloader:
    def downloadFile(self, url, location=""):
        download(url, out = location)

if not os.path.exists('downloads/'):
    print('no downloads folder! creating...')
    os.mkdir('downloads')

if not os.path.exists('repourl.txt'):
    print('no repo url file! creating...')
    open('repourl.txt', 'w').write('https://raw.githubusercontent.com/luneedev/luneedev/main/lunorepo.txt')

if not os.path.exists('repodata.txt'):
    print('no repo data file! you can type "luno update" to update repo data.')

if len(sys.argv) == 1:
    print(" _                         _\n| |_   _ _ __   ___  _ __ | | ____ _\n| | | | | '_ \ / _ \| '_ \| |/ / _` |\n| | |_| | | | | (_) | |_) |   | (_| |\n|_|\__,_|_| |_|\___/| .__/|_|\_\__, |\n                    |_|        |___/\nv0.1 by lunee.")

elif sys.argv[1] == 'get' and len(sys.argv) == 2:
    print('luno get [package_name] // luno get update')
elif sys.argv[1] == 'get' and len(sys.argv) >= 3:
    for pkg in sys.argv[2:]:
        print(f'trying to get a package {pkg}...')
        repodata = open('repodata.txt', 'r').read().split('\n')
        if pkg in repodata:
            print('found! downloading...')
            url = repodata[repodata.index(pkg) + 1]
            downloader().downloadFile(url, 'downloads/')
            print('\nsaved!')
        else:
            print('error! package not found!')

elif sys.argv[1] == 'repo' and len(sys.argv) == 2:
    print('luno repo change/update')
elif sys.argv[1:3] == ['repo', 'update']:
    print('trying to update repodata.txt...')
    try:
        urllib.request.urlretrieve(open('repourl.txt', 'r').readline(), 'repodata.txt')
        print('success!')
    except:
        print('error! check repo url and try again. you can change the repo url with "luno repo change [url]"')
elif sys.argv[1:3] == ['repo', 'change'] and len(sys.argv) == 4:
    print('\nOld: ' + open('repourl.txt', 'r').readline() + '\nNew: ' + str(sys.argv[3]))
    open('repourl.txt', 'w').write(sys.argv[3])
    print('\nchanged repo url in repourl.txt')
