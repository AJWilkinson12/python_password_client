class Password:
    
    def __init__(self, author, text, site):
        
        self.__author = author
        self.__text = text
        self.__site = site

    def get_author(self):
        
        return self.__author

    def get_text(self):
        
        return self.__text

    def get_site(self):

        return self.__site
