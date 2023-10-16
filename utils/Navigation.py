class Navigator:
    def __init__(self):
        self.__page_functions = {}
        self.__current_frame = None
        self.__current_page = None
        self.__main_app = None

    def register_page(self, page_name, page_function):
        self.__page_functions[page_name] = page_function

    def navigate_to_page(self, page_name):
        if page_name in self.__page_functions:
            self.__current_frame.pack_forget()  # Hide the current page
            self.__current_page = self.__page_functions[page_name]()

    def navigate_to_signin(self, current_page, tab):
        self.__current_page = self.__page_functions[current_page]
        if self.__current_page:
            print(self.__current_frame.pack_forget())
            print("page was destroyed")
        self.__current_page = self.__page_functions["SignIn"](tab)

    def set_main_app(self, main_app):
        self.__main_app = main_app

    def get_main_app(self):
        return self.__main_app

    def set_current_frame(self, frame):
        self.__current_frame = frame


navigator = Navigator()
