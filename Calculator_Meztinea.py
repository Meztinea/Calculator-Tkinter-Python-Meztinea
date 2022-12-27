# @Meztinea
from tkinter import Frame, Tk, Label, Entry, Button


class Calculator(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.c_t = '#FFFFFF'  # Text color
        self.c_r = '#0C1633'  # Fill color
        self.c_r_e = '#BCB8B1'  # Entry fill color
        self.c_t_e = '#000000'  # Entry text color
        self.initial_value = ''
        self.create_gui()

    def create_gui(self):
        Label(self.master, text='Calculator by @Meztinea', fg=self.c_t, bg=self.c_r, anchor='w').place(relx=0.00, rely=0.00, relwidth=1, relheight=0.10)
        self.result = Entry(self.master, fg=self.c_t_e, bg=self.c_r_e, font=('Arial', 10), justify='right')
        self.result.place(relx=0.00, rely=0.10, relwidth=1, relheight=0.08)
        self.result.config(state='disabled')
        self.input = Entry(self.master, fg=self.c_t_e, bg=self.c_r_e, font=('Arial', 20), justify='right')
        self.input.place(relx=0.00, rely=0.18, relwidth=1, relheight=0.12)
        self.input.insert(0, '0')
        self.input.config(state='disabled')

        Button(self.master, text='AC', fg=self.c_t, bg=self.c_r, command=self.delete_all).place(relx=0.03, rely=0.32, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='%', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('%')).place(relx=0.2725, rely=0.32, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='/', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('/')).place(relx=0.515, rely=0.32, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='Del', fg=self.c_t, bg=self.c_r, command=self.delete_data).place(relx=0.7575, rely=0.32, relwidth=0.2125, relheight=0.116)

        Button(self.master, text='7', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('7')).place(relx=0.03, rely=0.456, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='8', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('8')).place(relx=0.2725, rely=0.456, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='9', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('9')).place(relx=0.515, rely=0.456, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='x', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('*')).place(relx=0.7575, rely=0.456, relwidth=0.2125, relheight=0.116)

        Button(self.master, text='4', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('4')).place(relx=0.03, rely=0.592, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='5', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('5')).place(relx=0.2725, rely=0.592, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='6', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('6')).place(relx=0.515, rely=0.592, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='-', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('-')).place(relx=0.7575, rely=0.592, relwidth=0.2125, relheight=0.116)

        Button(self.master, text='1', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('1')).place(relx=0.03, rely=0.728, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='2', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('2')).place(relx=0.2725, rely=0.728, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='3', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('3')).place(relx=0.515, rely=0.728, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='+', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('+')).place(relx=0.7575, rely=0.728, relwidth=0.2125, relheight=0.116)

        Button(self.master, text='0', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('0')).place(relx=0.03, rely=0.864, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='00', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('00')).place(relx=0.2725, rely=0.864, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='.', fg=self.c_t, bg=self.c_r, command=lambda: self.enter_data('.')).place(relx=0.515, rely=0.864, relwidth=0.2125, relheight=0.116)
        Button(self.master, text='=', fg=self.c_t, bg=self.c_r, command=self.calculate_result).place(relx=0.7575, rely=0.864, relwidth=0.2125, relheight=0.116)

    def update_input(self, variable, data):
        variable.config(state='normal')
        variable.delete(0, 'end')
        variable.insert(0, data)
        variable.config(state='disabled')

    def enter_data(self, number):
        if self.result != '':
            self.update_input(self.result, '')
        self.initial_value = self.initial_value + str(number)
        self.update_input(self.input, self.initial_value)

    def calculate_result(self):
        input = self.input.get()
        self.update_input(self.result, input)
        result = eval(self.input.get())
        self.update_input(self.input, result)
        self.initial_value = ''

    def delete_data(self):
        new_input = self.input.get()[0:-1]
        self.initial_value = new_input
        self.update_input(self.input, new_input)

    def delete_all(self):
        self.update_input(self.input, '0')
        self.update_input(self.result, '')


if __name__ == "__main__":
    window = Tk()
    window.title('Calculator')
    window.geometry('350x400')
    window.configure(background='#BCB8B1')
    window.minsize(height=400, width=350)
    window.maxsize(height=400, width=350)

    app = Calculator(window)
    app.mainloop()
