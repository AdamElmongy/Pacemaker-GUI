class Navigator:
    def __init__(self):
        self.page_functions = {}
        self.current_frame=None
        self.current_page = None
        self.main_app = None

    def register_page(self, page_name, page_function):
        self.page_functions[page_name] = page_function

    def navigate_to_page(self, page_name):
        if page_name in self.page_functions:
            if self.current_frame:
                self.current_frame.pack_forget()  # Hide the current page
            self.current_page = self.page_functions[page_name]()
            

    def navigate_to_signin(self, current_page, tab):
        print(self.current_page)
        self.current_page = self.page_functions[current_page]
        if self.current_page:
            print(self.current_frame.pack_forget()) 
            print("page was destroyed")
        self.current_page = self.page_functions["SignIn"](tab)


navigator = Navigator()
