import os.path


class UXElements:
    """The colors and images"""

    def __init__(self,sg):
        self.sg = sg
        self.button_color = ''
        self.title_image = 'title_image.png'
        self.button_font = 'Verdana'
        self.info_text_font = 'Courier'
        self.display_font = 'Verdana'
        self.size_button = (5,2)
        self.display_size = (20,2)
        self.background_color = '#051C2C'
        self.layout = [
            [self.sg.Image(self.title_image, background_color=self.background_color)
            ],
            [self.sg.InputText(key='-value-', font=(self.display_font,30), size=self.display_size)
             ], [
                self.sg.Text('© Peter Inc. 2021',background_color=self.background_color, pad=(6, 2), font=(
                    self.info_text_font), justification='left')
            ],
            [
                self.sg.Button('EXIT', font=self.button_font, size=self.size_button, key='-quit-'),
                self.sg.Button('AC', font=self.button_font, size=self.size_button, key='-clear-'),
                self.sg.Button('<', font=self.button_font, size=self.size_button, key='-backspace-'),
                self.sg.Button('/', font=self.button_font, size=self.size_button, key='-divide-')
            ],
            [
                self.sg.Button('7', font=self.button_font, size=self.size_button),
                self.sg.Button('8', font=self.button_font, size=self.size_button),
                self.sg.Button('9', font=self.button_font, size=self.size_button),
                self.sg.Button('x', font=self.button_font, size=self.size_button, key='-multiply-')
            ],
            [
                self.sg.Button('4', font=self.button_font, size=self.size_button),
                self.sg.Button('5', font=self.button_font, size=self.size_button),
                self.sg.Button('6', font=self.button_font, size=self.size_button),
                self.sg.Button('-', font=self.button_font, size=self.size_button, key='-subtract-')
            ],
            [
                self.sg.Button('1', font=self.button_font, size=self.size_button),
                self.sg.Button('2', font=self.button_font, size=self.size_button),
                self.sg.Button('3', font=self.button_font, size=self.size_button),
                self.sg.Button('+', font=self.button_font, size=self.size_button, key='-add-')
            ],
            [
                self.sg.Button('0', font=self.button_font, size=self.size_button),
                self.sg.Button('.', font=self.button_font, size=self.size_button),
                self.sg.Button('=', font=self.button_font, button_color='#2A6A9B', key='-equals-', size=(16, 2),
                               pad=(5, 1))
            ]
        ]
