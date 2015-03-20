from io import StringIO
from StringIO import StringIO
import sys
import re
import string
import json
from langdetect import detect


#----------------------------------------------------------------------------------------------
# main
#----------------------------------------------------------------------------------------------
def main():

    reviews = open(sys.argv[1])

    for x in reviews:
    	temp = x.replace("fresh", "").replace("rotten", "").replace("none", "")
    	
        try:
            language = detect(temp)
            if language:
                if language == 'en':
                    print x.strip()
                else:
                    pass
        except:
            pass
                    
if __name__ == '__main__':
    main()