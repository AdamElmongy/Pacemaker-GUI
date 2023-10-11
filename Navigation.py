class Navigator:
    def __init__(self):
        self.page_functions = {}
        self.current_page = None

    def register_page(self, page_name, page_function):
        self.page_functions[page_name] = page_function

    def navigate_to_page(self, page_name):
        if page_name in self.page_functions:
            if self.current_page:
                self.current_page.destroy()
            self.current_page = self.page_functions[page_name]()


navigator = Navigator()
