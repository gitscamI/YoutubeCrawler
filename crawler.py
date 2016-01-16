import re, random, urllib2

def data(link):
    response = urllib2.urlopen(link)
    data = response.read()
    return data

def matches(data):
    regex = r'\/watch\?v=([-\w]{11})'
    matches = re.findall(regex, data)
    return matches

def purify(dirtyList):
    cleanSet = set()

    for element in dirtyList:
        cleanSet.add(element)

    return list(cleanSet)

def logIds(iDs):
    with open('idLog.txt', 'a+') as File:
        for iD in iDs:
            File.write('%s\n' % iD)
    File.close()
                       
def linkLaunch(iDs): # for debug reasons, therefore the internal import
    import webbrowser
    
    pattern = 'https://www.youtube.com/watch?v=%s'
    
    for iD in iDs:
        link = pattern % iD
        webbrowser.open_new_tab(link)
        raw_input()
        
        
count = 1
pattern = 'https://www.youtube.com/watch?v=%s'
link = 'https://www.youtube.com/watch?v=hHUbLv4ThOo'

while True:    
    iDs = purify(matches(data(link)))
    print '%d iDs in iteration %d' % (len(iDs), count)
    logIds(iDs)

    link = pattern % (random.choice(iDs))
    count += 1
