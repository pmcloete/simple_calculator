import PySimpleGUI as sg
from ux_elements import UXElements


class Calculator:
    """Simple calculator"""

    def __init__(self):
        self.display_value = ''
        self.current_value = ''
        self.saved_value = ''
        self.operation = ''
        self.result = 0
        self.result_pressed = False
        self.function = ''
        self.sg = sg
        self.ux = UXElements(self.sg)

        self.window = self.sg.Window('Calculator', self.ux.layout, background_color=self.ux.background_color,
                                     finalize=True,grab_anywhere=True)

    def main(self):
        """The main method"""

        count = 0
        decimal_allowed = True
        while True:
            event, value = self.window.read()
            print(event, value)
            if event == self.sg.WIN_CLOSED or event == '-quit-':
                break
            elif event == '1':
                self.current_value += event
            elif event == '2':
                self.current_value += event
            elif event == '3':
                self.current_value += event
            elif event == '4':
                self.current_value += event
            elif event == '5':
                self.current_value += event
            elif event == '6':
                self.current_value += event
            elif event == '7':
                self.current_value += event
            elif event == '8':
                self.current_value += event
            elif event == '9':
                self.current_value += event
            elif event == '0':
                self.current_value += event
            elif event == '.':
                if not self.current_value:
                    self.current_value += '0.'
                if self.current_value.endswith('.'):
                    continue
                if '.' in self.current_value:
                    continue
                self.current_value += '.'
            #  Clear the display
            elif event == '-clear-':
                self.current_value = ''
                self.saved_value = ''
                self.result = ''
                #  Backspace
            elif event == '-backspace-':
                #  TODO: Fix this.!
                if self.result_pressed:
                    self.current_value = self.saved_value
                    self.result_pressed = False
                else:
                    length = len(self.current_value) - 1
                    self.current_value = self.current_value[:length]
                #  Return/ Send data to where it needs to go

            elif event == '-divide-':
                self.operation = 'divide'
                self.display_value = self.current_value
                self.saved_value = self.current_value
                self.current_value = ''
            elif event == '-multiply-':
                self.operation = 'multiply'
                self.display_value = self.current_value
                self.saved_value = self.current_value
                self.current_value = ''
            elif event == '-subtract-':
                self.operation = 'subtract'
                self.display_value = self.current_value
                self.saved_value = self.current_value
                self.current_value = ''
            elif event == '-add-':
                self.operation = 'add'
                self.display_value = self.current_value
                self.saved_value = self.current_value
                self.current_value = ''

            elif event == '-equals-':
                if not self.current_value:
                    continue
                elif self.operation == 'add':
                    if self.result:
                        self.result = float(self.result) + float(self.current_value)
                    else:
                        self.result = float(self.current_value) + float(self.saved_value)
                elif self.operation == 'subtract':
                    if self.result:
                        self.result = float(self.result) - float(self.current_value)
                    else:
                        self.result = float(self.saved_value) - float(self.current_value)
                elif self.operation == 'multiply':
                    if self.result:
                        self.result = float(self.result) * float(self.current_value)
                    else:
                        self.result = float(self.current_value) * float(self.saved_value)
                elif self.operation == 'divide':
                    try:
                        if self.result:
                            self.result = float(self.result) / float(self.current_value)
                        else:
                            self.result = float(self.saved_value) / float(self.current_value)
                    except ZeroDivisionError:
                        self.result = 0
                self.saved_value = self.result
                self.result_pressed = True
                #  No more data in the display, reset the count
            #  Update the display field on every pass
            self._update_calculator()
        self.window.close()

    def _update_calculator(self):
        """Update the text display for the values entered on the keypad"""
        if self.result_pressed:
            self.window['-value-'].update(self.result)
            self.result_pressed = False
            self.current_value = ''
            return
        else:
            if self.current_value:
                self.display_value = self.current_value
            elif self.result:
                self.display_value = self.result
            else:
                self.display_value = self.saved_value
        self.window['-value-'].update(self.display_value)
        # self.window['-value-'].update(self.current_value)


if __name__ == '__main__':
    calc = Calculator()
    calc.main()
