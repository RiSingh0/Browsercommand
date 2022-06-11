import sqlite3
import shutil
import os

def clear_history_chrome():
    try:
        # location
        location = "C:\\Users\\risha\\AppData\\Local\\Google\\Chrome\\User Data\\"
        
        # directory
        dir = "Profile 2"
        
        # path
        path = os.path.join(location, dir)
        
        # removing directory
        shutil.rmtree(path)
        return True
    except:
        print("somthing wromg")
        return False



   

def clear_history_firefox():
    try:
        # location
        location = r"C:\Users\risha\AppData\Roaming\Mozilla\Firefox\Profiles\70ih2wsf.default-1654018328652"
        
        # removing directory
        shutil.rmtree(os.path.join(location, "bookmarkbackups"))
        shutil.rmtree(os.path.join(location, "storage"))
        shutil.rmtree(os.path.join(location, "shader-cache"))
        shutil.rmtree(os.path.join(location, "sessionstore-backups"))


        #deleting from histroy
        conn = sqlite3.connect(r"C:\Users\risha\AppData\Roaming\Mozilla\Firefox\Profiles\70ih2wsf.default-1654018328652\places.sqlite")
        c = conn.cursor()
        c.execute("Delete from moz_anno_attributes")
        c.execute("Delete from moz_annos ")
        c.execute("Delete from moz_bookmarks ")
        c.execute("Delete from moz_historyvisits ")
        c.execute("Delete from moz_items_annos  ")
        c.execute("Delete from moz_keywords ")
        c.execute("Delete from moz_places ")
        print("done")
        conn.commit()
        conn.close()
    except:
        print("somthing wromg")
        return False
    return True