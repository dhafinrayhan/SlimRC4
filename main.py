from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import chipers


class SlimRC4:

    def __init__(self, root):

        root.title('SlimRC4')

        self.mainframe = ttk.Frame(root, padding='3 3 12 12')
        self.mainframe.grid(column=0, row=0)

        self.draw_input_frame()
        self.draw_key_frame()
        self.draw_task_frame()
        self.draw_action_frame()
        self.draw_output_frame()

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=4, pady=4)

    def draw_input_frame(self):

        self.input_frame = ttk.Labelframe(self.mainframe, text='Input')
        self.input_frame.grid(row=5, column=10)

        self.input_buttons_frame = ttk.Frame(self.input_frame)
        self.input_buttons_frame.grid(row=5, column=10, sticky='we')

        self.open_file_button = ttk.Button(
            self.input_buttons_frame, text="Open file...", command=self.open_file)
        self.open_file_button.grid(row=5, column=10, sticky='w')

        self.clear_input_button = ttk.Button(
            self.input_buttons_frame, text="Clear input", command=self.update_input)
        self.clear_input_button.grid(row=5, column=20, sticky='w')

        self.input_text = Text(self.input_frame, height=5, width=64)
        self.input_text.grid(row=10, column=10, sticky='we')

        for child in self.input_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def open_file(self):
        self.open_file = filedialog.askopenfile()

        if self.open_file is None:
            return

        self.update_input(content=self.open_file.read())
        self.open_file.close()

    def draw_key_frame(self):

        self.key_frame = ttk.Labelframe(self.mainframe, text='Key')
        self.key_frame.grid(row=7, column=10)

        self.key_text = Text(self.key_frame, height=2, width=64)
        self.key_text.grid(row=10, column=10, sticky='we')

        for child in self.key_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def draw_task_frame(self):

        self.task_frame = ttk.Labelframe(self.mainframe, text='Task')
        self.task_frame.grid(row=20, column=10)

        self.task_var = StringVar()
        self.task_var.set('encrypt')

        self.encrypt_radio = ttk.Radiobutton(
            self.task_frame, text='Encrypt', variable=self.task_var, value='encrypt')
        self.decrypt_radio = ttk.Radiobutton(
            self.task_frame, text='Decrypt', variable=self.task_var, value='decrypt')

        self.encrypt_radio.grid(row=0, column=0, sticky='nw')
        self.decrypt_radio.grid(row=0, column=1, sticky='nw')

        for child in self.task_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def draw_action_frame(self):
        self.action_frame = ttk.Frame(self.mainframe)
        self.action_frame.grid(row=40, column=10)

        ttk.Separator(self.action_frame).grid(row=10, column=10, pady=16)

        self.start_button = ttk.Button(
            self.action_frame, text='START', command=self.action_start)
        self.start_button.grid(row=20, column=10)

    def draw_output_frame(self):

        self.output_frame = ttk.Labelframe(self.mainframe, text='Output')
        self.output_frame.grid(row=80, column=10)

        self.output_buttons_frame = ttk.Frame(self.output_frame)
        self.output_buttons_frame.grid(row=5, column=10, sticky='we')

        self.output_text = Text(self.output_frame, height=5, width=64)
        self.output_text.grid(row=10, column=10, sticky='we')

        self.save_button = ttk.Button(
            self.output_frame, text='Save to file', command=self.save_to_file)
        self.save_button.grid(row=20, column=10, sticky='w')

        for child in self.output_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def update_input(self, content='', enabled=True):
        self.input_text.delete('1.0', END)
        self.input_text.insert('1.0', content)

    def update_output(self, content='', enabled=True):
        self.output_text.delete('1.0', END)
        self.output_text.insert('1.0', content)

    def action_start(self):
        self.input_content = self.input_text.get('1.0', END)
        self.key = self.key_text.get('1.0', END)

        decrpyt = self.task_var.get() == 'decrypt'

        self.output_content = chipers.slimrc4(
            self.input_content, self.key, decrpyt)

        self.update_output(content=self.output_content)

    def save_to_file(self):
        self.save_file = filedialog.asksaveasfile(
            mode='w', defaultextension='.txt')

        if self.save_file is None:
            return

        try:
            self.save_file.write(self.output_content)
        finally:
            self.save_file.close()


root = Tk()
SlimRC4(root)
root.mainloop()
