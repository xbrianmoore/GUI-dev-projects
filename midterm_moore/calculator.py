# Brian Moore
import tkinter as tk
from tkinter import font

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # icon
        self.iconbitmap('calculator.ico')
        self.title("Calculator")
        self.geometry("400x500")
        self.resizable(False, False)
        
        # color scheme
        self.input_bg = "#E8F4F8"      
        self.input_fg = "#1A1A1A"      
        self.button_bg = "#C27272"     
        self.button_fg = "#FCC3C3"     
        self.clear_del_bg = "#FF0000"  
        self.equal_bg = "#FFC000"      
        
        # Arial, 12pt, bold font
        self.input_font = font.Font(family="Arial", size=12, weight="bold")
        self.button_font = font.Font(family="Arial", size=10, weight="bold")
        
        self.input_text = tk.StringVar()
        self.input_field = tk.Entry(
            self,
            textvariable=self.input_text,
            justify='right',
            font=self.input_font,
            bg=self.input_bg,
            fg=self.input_fg,
            borderwidth=2,
            relief="solid"
        )
        self.input_field.grid(row=0, column=0, columnspan=4, padx=5, pady=10, ipady=10, sticky="nsew")
        
        
        self.grid_rowconfigure(0, weight=1)
        for i in range(1, 6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['(', ')', 'C', 'DEL'],
        ]
        
        
        for row_idx, row in enumerate(buttons, start=1):
            for col_idx, button in enumerate(row):
                self.create_button(button, row_idx, col_idx)
        
        
        self.bind('<Key>', self.keyboard_input)
        
    def create_button(self, button_text, row, col):
        """Create a button with appropriate styling"""
        # button color
        if button_text in ['C', 'DEL']:
            bg_color = self.clear_del_bg
            fg_color = self.button_fg
        elif button_text == '=':
            bg_color = self.equal_bg
            fg_color = "#000000"  # Black text for gold background
        else:
            bg_color = self.button_bg
            fg_color = self.button_fg
        
        btn = tk.Button(
            self,
            text=button_text,
            font=self.button_font,
            bg=bg_color,
            fg=fg_color,
            activebackground="#404040",
            activeforeground=fg_color,
            borderwidth=2,
            relief="raised",
            command=lambda x=button_text: self.button_click(x)
        )
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew", ipadx=15, ipady=15)

    def button_click(self, button):
        """Handle button clicks"""
        current_text = self.input_text.get()
        
        if button == '=':
            try:
                result = eval(current_text)
                self.input_text.set(result)
            except:
                self.input_text.set('ERROR')
        elif button == 'C':
            self.clear_input()
        elif button == 'DEL':
            self.delete_char()
        else:
            new_text = current_text + button
            self.input_text.set(new_text)

    def clear_input(self):
        """Clear the input field"""
        self.input_text.set('')
    
    def delete_char(self):
        """Delete the last character from the input field"""
        current_text = self.input_text.get()
        new_text = current_text[:-1]
        self.input_text.set(new_text)
    
    def keyboard_input(self, event):
        """Handle keyboard input"""
        current_text = self.input_text.get()
        
        # numbers
        if event.char in '0123456789':
            self.button_click(event.char)
        # operators
        elif event.char in '+-*/':
            self.button_click(event.char)
        # decimal point
        elif event.char == '.':
            self.button_click('.')
        # parentheses
        elif event.char in '()':
            self.button_click(event.char)
        # equals
        elif event.char == '=':
            self.button_click('=')
        # Enter/Return as equal sign
        elif event.keysym == 'Return':
            self.button_click('=')
        # Backspace for delete
        elif event.keysym == 'BackSpace':
            self.delete_char()
        # 'c' or 'C' for clear
        elif event.char.upper() == 'C':
            self.clear_input()
        else:
            return "break"

if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()
