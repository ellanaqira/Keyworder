from tkinter import *
from main_window_folder.main_frame import Main_frame
from login_window import Login_window
from aset import Aset

class Main_element:
        def __init__(self, root_window):
                self.root_window = root_window
                self.main_frame = Main_frame()
                self.aset = Aset()

                self.keyword_and_sentence = {}

#login button
        def login_button(self):
                self.login_btn = Button(self.main_frame.frame_top,
                                text="Log In",
                                pady=2,
                                command=self.open_login_window)
                self.login_btn.grid(row=0, column=0)

        #login button command
        def open_login_window(self):
                self.root_window.withdraw()
                Login_window(self.root_window, self.login_btn)

#image title
        def image_title(self):
                img_title = Label(self.main_frame.frame_title,
                                pady=0,
                                image=self.aset.title_img)
                img_title.grid(row=0, column=0)

#Mini underline class
        class Mini_Underline:
                def __init__ (self,frame,row,column,number,right_border, left_border, line_type):
                        self.frame = frame
                        self.row = row
                        self.column = column
                        self.number = number
                        self.right_border = right_border
                        self.left_border = left_border
                        self.line_type = line_type

                def mini_underline(self):
                        mini_udrline = Label(self.frame,
                                                text=f"{self.right_border}{self.line_type*self.number}{self.left_border}",
                                                font=('consolas',13,'bold'),
                                                pady=0,
                                                fg="#737373")
                        
                        mini_udrline.grid(row=self.row, column=self.column)

#mini underline 1
        def mini_underline_1(self):
                mini_underline1 = self.Mini_Underline(self.main_frame.frame_under_title, 0, 0, 43, "", "", self.aset.underline_sign)
                mini_underline1.mini_underline()

#big line class
        class Underline:
                def __init__(self,title,frame,row,column,row_text,column_text, long, line_type):
                        self.title = title
                        self.frame = frame
                        self.row = row
                        self.column = column
                        self.row_text = row_text
                        self.column_text = column_text
                        self.long = long
                        self.line_type = line_type
                        
                def under_line(self):
                        undr_line = Label(self.frame,
                                        text=self.line_type*self.long,
                                        relief="raised",
                                        fg="#C3C3C3",
                                        bg="#C3C3C3",
                                        font=('consolas', 1, 'bold'))
                        undr_line.grid(row=self.row, column=self.column)

                def menu_title(self):
                        menu_text = Label(self.frame,
                                        text=self.title,
                                        font=('consolas', 12, 'bold'))
                        menu_text.grid(row=self.row_text, column=self.column_text)

#big line 1
        def big_line_1(self):
                border_line1 = self.Underline("INPUT", self.main_frame.frame_big_line1, 0, 1, 0, 0, 375, self.aset.equal_sign)
                border_line1.under_line()
                border_line1.menu_title()

#big line 2
        def big_border_line_2(self):
                border_line_2 = self.Underline("OUTPUT", self.main_frame.frame_big_line2 ,0 ,1, 0, 0, 360, self.aset.equal_sign)
                border_line_2.under_line()
                border_line_2.menu_title()

#typebar title class
        class typebar_title_class:
                def __init__ (self, text_title, image_title, frame_title, row_title, column_title):
                        self.text_title = text_title
                        self.image_title = image_title
                        self.frame_title = frame_title
                        self.row_title = row_title
                        self.column_title = column_title

                def typebar_title(self):
                        title = Label(self.frame_title,
                                        text=self.text_title,
                                        font=('consolas', 10, 'italic'),
                                        fg="#000000",
                                        pady=1,
                                        bg="#cccccc",
                                        image=self.image_title,
                                        compound='right')
                        title.grid(row=self.row_title, column=self.column_title)
                        return title

#keyword title      
        def title_keyword(self):
                text_keyword = self.typebar_title_class("Keyword", self.aset.down_arow_icon, self.main_frame.frame_input , 0, 0)
                text_keyword.typebar_title()

#sentence title      
        def title_sentence(self):
                text_sentence = self.typebar_title_class("Sentence", self.aset.down_arow_icon, self.main_frame.frame_input , 3, 0)
                text_sentence.typebar_title()


#( SINGLE TYPEBAR AND SCROLLBAR CLASS )
        class single_typebar_class:
                def __init__ (self, frame_typebar, backspace_image, config_single_typebar):
                        self.frame_typebar = frame_typebar
                        self.backspace_image = backspace_image
                        self.width_typebar = config_single_typebar.get("width typebar", 47)
                        self.row_typebar = config_single_typebar.get("row typebar", 0)
                        self.column_typebar = config_single_typebar.get("column typebar", 0)
                        self.column_delete_btn = config_single_typebar.get("column delete btn", 0)
                        self.scrollbar_row = config_single_typebar.get("scrollbar row", 0)
                        self.scrollbar_column = config_single_typebar.get("scrollbar column", 0)

                def single_typebar_scrollbar(self):
                        self.scrollbar_input = Scrollbar(self.frame_typebar,
                                                bg="#cccccc",
                                                orient="horizontal")
                        self.scrollbar_input.grid(row=self.scrollbar_row, column=self.scrollbar_column, sticky=EW)

                        self.typebar = Entry(self.frame_typebar,
                                        bg="#d7d7d7",
                                        font=('consolas', 10),
                                        width=self.width_typebar,
                                        xscrollcommand=self.scrollbar_input.set)
                        self.typebar.grid(row=self.row_typebar, column=self.column_typebar)
                        self.scrollbar_input.config(command=self.typebar.xview)

                        self.del_btn = Button(self.frame_typebar,
                                                image=self.backspace_image,
                                                command=self.delete_input)
                        self.del_btn.grid(row=self.row_typebar, column=self.column_delete_btn)

                def delete_input(self):
                        self.typebar.delete(0,END)
                        return self.typebar

                def get(self):
                        if isinstance(self.typebar, Entry):
                                return self.typebar.get()
                        elif isinstance(self.typebar, Text):
                                return self.typebar.get("1.0", END).strip()
                        
#typebar keyword
        def typebar_keyword(self):
                self.config_single_typebar = {"row typebar" : 1,
                        "column typebar" : 0,
                        "column delete btn": 2,
                        "scrollbar row" : 2,
                        "scrollbar column" : 0}
                
                self.entry_keyword = self.single_typebar_class(self.main_frame.frame_input, self.aset.backspace_img, self.config_single_typebar)
                self.entry_keyword.single_typebar_scrollbar()

#search typebar
        def search_typebar(self):
                self.config_single_typebar = {"row typebar" : 0,
                        "width typebar" : 43,
                        "column typebar" : 0,
                        "column delete btn": 3,
                        "scrollbar row" : 1,
                        "scrollbar column" : 0}
                
                self.entry_search = self.single_typebar_class(self.main_frame.frame_search, self.aset.backspace_img, self.config_single_typebar)
                self.entry_search.single_typebar_scrollbar()

#( BIG TYPEBAR AND SCROLLBAR CLASS )
        class big_typebar_class:
                def __init__ (self, frame_typebar, backspace_image, config_big_typebar):
                        self.frame_typebar = frame_typebar
                        self.backspace_image = backspace_image
                        self.width_typebar = config_big_typebar.get("width typebar", 47)
                        self.height_typebar = config_big_typebar.get("height", 10)
                        self.row_typebar = config_big_typebar.get("row typebar", 0)
                        self.column_typebar = config_big_typebar.get("column typebar", 0)
                        self.column_delete_btn = config_big_typebar.get("column delete btn", 0)
                        self.scrollbar_row = config_big_typebar.get("scrollbar row", 0)
                        self.scrollbar_column = config_big_typebar.get("scrollbar column", 0)

                def big_typebar_scrollbar(self):
                        self.scrollbar_input = Scrollbar(self.frame_typebar,
                                                        bg="#cccccc",
                                                        orient="vertical")
                        self.scrollbar_input.grid(row=self.scrollbar_row, column=self.scrollbar_column, sticky=NS)

                        self.typebar = Text(self.frame_typebar,
                                                bg="#d7d7d7",
                                                font=('consolas', 10),
                                                width=self.width_typebar,
                                                height=self.height_typebar,
                                                yscrollcommand=self.scrollbar_input.set)
                        self.typebar.grid(row=self.row_typebar, column=self.column_typebar)
                        self.scrollbar_input.config(command=self.typebar.yview)

                        self.del_btn = Button(self.frame_typebar,
                                                image=self.backspace_image,
                                                command=self.delete_input)
                        self.del_btn.grid(row=self.row_typebar, column=self.column_delete_btn)

                def delete_input(self):
                        self.typebar.delete(1.0,END)
                        return self.typebar
                        
                def get(self):
                        if isinstance(self.typebar, Entry):
                                return self.typebar.get()
                        elif isinstance(self.typebar, Text):
                                return self.typebar.get("1.0", END).strip()
                
        def typebar_sentence(self):
                self.config_big_typebar = {"row typebar" : 4,
                        "column typebar" : 0,
                        "column delete btn": 2,
                        "scrollbar row" : 4,
                        "scrollbar column" : 1}
                
                self.entry_sentence = self.big_typebar_class(self.main_frame.frame_input, self.aset.backspace_img, self.config_big_typebar)
                self.entry_sentence.big_typebar_scrollbar()

#button class
        class button_action:
                def __init__ (self, frame, image_btn, row_btn, column_btn, command_btn, padx_btn):
                        self.frame = frame
                        self.image_btn = image_btn
                        self.row_btn = row_btn
                        self.column_btn = column_btn
                        self.command_btn = command_btn
                        self.padx_btn = padx_btn

                def btn_act(self):
                        btn_action = Button(self.frame,
                                                image=self.image_btn,
                                                command=self.command_btn)
                        btn_action.grid(row=self.row_btn, column=self.column_btn, padx= self.padx_btn)
                        return btn_action

#search button        
        def search_button_button(self):
                search_button = self.button_action(self.main_frame.frame_search, self.aset.search_img, 0, 1, self.search_button_command, 0)
                search_button.btn_act()

        #search button command
        def search_button_command(self):
                self.search_input = self.entry_search.get()
                self.found = False

                self.output_box1.write_output(f'\n\n{self.aset.equal_sign*20}[ SEARCH ]{self.aset.equal_sign*20}')

                for key, val in self.keyword_and_sentence.items():
                        if self.search_input in key or self.search_input in val:
                                self.output_box1.write_output(f'\n# KEYWORD  :\n{key}\n')
                                self.output_box1.write_output(f'# SENTENCE :\n{val}\n')
                                self.found = True

                if not self.found:
                        self.output_box1.write_output('\nno item in list\n')

#delete keyword & sentence button
        def delete_keyword_sentence_button(self):
                del_KnS_button = self.button_action(self.main_frame.frame_search, self.aset.trash_icon, 0, 2, self.delete_keyword_sentence_command, 2)
                del_KnS_button.btn_act()

        #delete keyword & sentence button command
        def delete_keyword_sentence_command(self):
                search_input = self.entry_search.get()
                if search_input in self.keyword_and_sentence:
                        del self.keyword_and_sentence[search_input]
                        self.output_box1.write_output(f"\n( {search_input} ) and the Sentence is deleted")

                else:
                        self.output_box1.write_output(f"\n( {search_input} ) Not found/Wrong keyword")

#delete all input typebar   
        def delete_all_input_typebar(self):
                delete_all_button = self.button_action(self.main_frame.frame_menu_button, self.aset.red_cross_img, 0, 0, self.delete_all, 0)
                delete_all_button.btn_act()

        #delete all input typebar command
        def delete_all(self):
                self.entry_keyword.delete_input()
                self.entry_sentence.delete_input()

#add button
        def add_keyword_sentence_button(self):
                add_button = self.button_action(self.main_frame.frame_menu_button, self.aset.plus_img, 0, 1, self.add_all, 5)
                add_button.btn_act()

        #add button command
        def add_all(self):
                keyword = self.entry_keyword.get()
                sentence = self.entry_sentence.get()

                if not keyword or not sentence:
                        self.output_box1.write_output("\nplease add your keyword and sentence!")

                else:
                        self.keyword_and_sentence[keyword] = sentence
                        self.output_box1.write_output('\nkeyword & sentence added')

#show all keyword & sentence button
        def show_all_keyword_sentence_button(self):
                show_all_button = self.button_action(self.main_frame.frame_menu_button, self.aset.show_all_img, 0, 2, self.show_all, 5)
                show_all_button.btn_act()

        #show all keyword & sentence command
        def show_all(self):
                if not self.keyword_and_sentence:
                        self.output_box1.write_output("\nyou haven't added anything yet!")
                        
                else:
                        self.output_box1.write_output(f'\n\n{self.aset.equal_sign*14}[ KEYWORD & SENTENCE ]{self.aset.equal_sign*14}')
                        for keyword, sentence in self.keyword_and_sentence.items():
                                self.output_box1.write_output(f'\n# KEYWORD  :\n{keyword}\n')
                                self.output_box1.write_output(f'# SENTENCE :\n{sentence}\n')

#clear button
        def clear_output_box_button(self):
                clear_button = self.button_action(self.main_frame.frame_menu_button, self.aset.clear_img, 0, 3, self.clear_text_box, 0)
                clear_button.btn_act()

        #clear outputbox command
        def clear_text_box(self):
                self.output_box1.text_container.delete(1.0,END)

#output box class
        class OutputBox:
                def __init__(self, frame, height, width, row, column, rowsb, columnsb):
                        self.frame = frame
                        self.height = height
                        self.width = width
                        self.row = row
                        self.column = column
                        self.rowsb = rowsb
                        self.columnsb = columnsb

                def output_box(self):
                        self.scrollbar = Scrollbar(self.frame,
                                                bg="#cccccc",
                                                orient="vertical")
                        self.scrollbar.grid(row=self.rowsb, column=self.columnsb, sticky=NS)

                        self.text_container = Text(self.frame,
                                        width = self.width,
                                        bd=2,
                                        bg="#cccccc",
                                        height = self.height,
                                        yscrollcommand=self.scrollbar.set)
                        self.text_container.grid(row=self.row, column=self.column)
                        self.scrollbar.config(command=self.text_container.yview)

                def write_output(self,message):
                        self.text_container.insert(END,f"{message}")
                        self.text_container.see(END)

#output box 1
        def output_box_information_1(self):
                self.output_box1 = self.OutputBox(self.main_frame.frame_outputbox, 17, 50, 1, 0, 1, 1)
                self.output_box1.output_box()