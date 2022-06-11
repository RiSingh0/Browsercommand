import webbrowser

class StratBrowsure:
    def __init__(self,browsure,url):
        self.browsure = browsure
        self.url = url
        self.mapping = {"firefox":"C://Program Files//Mozilla Firefox//firefox.exe",
            "chrome":"C://Program Files//Google//Chrome//Application//chrome.exe"}
        
    
    def start(self):
        if self.browsure in self.mapping:
            webbrowser.register(self.browsure,
                None,
                webbrowser.BackgroundBrowser(self.mapping[self.browsure]))
        else:
            return False
        webbrowser.get(self.browsure).open_new_tab(self.url)
        return True