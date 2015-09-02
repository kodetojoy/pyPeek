#!/usr/local/bin/python

#              _____          _
#             |  __ \        | |
#  _ __  _   _| |__) |__  ___| | __
# | '_ \| | | |  ___/ _ \/ _ \ |/ /
# | |_) | |_| | |  |  __/  __/   <
# | .__/ \__, |_|   \___|\___|_|\_\  v0.0.1
# | |     __/ |
# |_|    |___/



import os, sys, httplib, urlparse

def unshorten_url(url):
    try:
        parsed = urlparse.urlparse(url)
        if parsed.scheme == "https":
            h = httplib.HTTPSConnection(parsed.netloc)
        else:
            h = httplib.HTTPConnection(parsed.netloc)
        resource = parsed.path
        if parsed.query != "":
            resource += "?" + parsed.query
        h.request('HEAD', resource )
        response = h.getresponse()
        if response.status/100 == 3 and response.getheader('Location'):
            return unshorten_url(response.getheader('Location')) # changed to process chains of short urls
        else:
            return url
    except:
        return url


def color(text, color):
    c = {
    'yellow':'\033[93m',
    'green':'\033[92m',
    'bold':'\033[1m',
    'end':'\033[0m',
    }
    return c['bold'] + c[color] + text + c['end']



if __name__ == "__main__":
    if len(sys.argv)>1:
        target = sys.argv[1]
        file_op = False or target.lower().endswith(".txt")
        if file_op:
            if not os.path.exists(target):
                print "ERROR: %s does not exist. Check the path and try again."%(target)
            else:
                print "Beginning batch processing of shortened URLs:"
                print "-"*100
                f = open(target, "r")
                lines = f.readlines()
                if len(sys.argv)>2:
                    output_file = sys.argv[2]
                    f2 = open(output_file, "w")
                else:
                    output_file = "output.txt"
                    f2 = open(output_file, "w")
                for i in lines:
                    f2.write(unshorten_url(i.replace("\n", ""))+"\n")
                    print "%s <-- forwards to --> %s"%(color(i.replace("\n", ""), 'yellow'), color(unshorten_url(i.replace("\n", "")), 'green'))
                f.close()
                f2.close()
                print "-"*100
                print "Unshortened links can be found here: %s"%(color(output_file, 'green'))
        else:
            #they are trying to plug in a single link to unshorten
            print "-"*100
            print "%s <-- forwards to --> %s"%(color(target, 'yellow'), color(unshorten_url(target), 'green'))
            print "-"*100
    else:
        print "ERROR: You must supply a URL (or path to a file full of URLs) to unshorten."
