from tkinter import *
from tkinter import messagebox, ttk
from typing import Union

class DataStructureGUI:
    def __init__(self):
        self.window = None
        self.input_entry = None
        self.result_label = None
        self.set_data = set()
        self.tuple_data = ()
        self.current_mode = None
        self.create_main_window()

    def create_main_window(self):
        self.window = Tk()
        self.window.title("Data Structure Operations GUI")
        self.window.geometry("800x600")
        self.window.configure(bg="#f0f0f0")
        
        # Create main container with padding
        main_container = Frame(self.window, bg="#f0f0f0", padx=20, pady=20)
        main_container.pack(fill=BOTH, expand=True)
        
        # Header
        header_frame = Frame(main_container, bg="#f0f0f0")
        header_frame.pack(fill=X, pady=(0, 20))
        
        try:
            photo = PhotoImage(file="python-GUI/rv new logo.png").subsample(2, 2)
            logo_label = Label(header_frame, image=photo, bg="#f0f0f0")
            logo_label.image = photo  # Keep a reference
            logo_label.pack(side=LEFT, padx=(0, 20))
        except:
            # Gracefully handle missing image
            pass
        
        # Title and description
        title_label = Label(
            header_frame,
            text="Data Structure Operations",
            font=("Helvetica", 24, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(fill=X)
        
        description = """
        This application allows you to perform operations on Sets and Tuples.
        • Set Operations: Add elements, remove specific items
        • Tuple Operations: Add elements, clear entire tuple
        Select an operation type below to begin.
        """
        desc_label = Label(
            main_container,
            text=description,
            font=("Helvetica", 12),
            bg="#f0f0f0",
            fg="#666666",
            justify=LEFT
        )
        desc_label.pack(fill=X, pady=(0, 20))
        
        # Buttons container
        button_frame = Frame(main_container, bg="#f0f0f0")
        button_frame.pack(fill=X, pady=20)
        
        # Style for buttons
        button_style = {
            "font": ("Helvetica", 12, "bold"),
            "width": 15,
            "height": 2,
            "borderwidth": 0,
            "cursor": "hand2"
        }
        
        set_button = Button(
            button_frame,
            text="Set Operations",
            command=self.setup_set_operations,
            bg="#4CAF50",
            fg="white",
            **button_style
        )
        set_button.pack(side=LEFT, padx=10)
        
        tuple_button = Button(
            button_frame,
            text="Tuple Operations",
            command=self.setup_tuple_operations,
            bg="#2196F3",
            fg="white",
            **button_style
        )
        tuple_button.pack(side=LEFT, padx=10)
        
        exit_button = Button(
            button_frame,
            text="Exit",
            command=self.window.quit,
            bg="#f44336",
            fg="white",
            **button_style
        )
        exit_button.pack(side=LEFT, padx=10)
        
        # Operations frame
        self.operations_frame = Frame(main_container, bg="#f0f0f0")
        self.operations_frame.pack(fill=BOTH, expand=True)
        
        # Result label
        self.result_label = Label(
            main_container,
            text="",
            font=("Helvetica", 14),
            bg="#f0f0f0",
            wraplength=700
        )
        self.result_label.pack(fill=X, pady=20)

    def clear_operations_frame(self):
        for widget in self.operations_frame.winfo_children():
            widget.destroy()
        self.result_label.config(text="")

    def setup_set_operations(self):
        self.clear_operations_frame()
        self.current_mode = "set"
        
        # Input frame
        input_frame = Frame(self.operations_frame, bg="#f0f0f0")
        input_frame.pack(fill=X, pady=20)
        
        Label(
            input_frame,
            text="Enter element:",
            font=("Helvetica", 12),
            bg="#f0f0f0"
        ).pack(side=LEFT, padx=5)
        
        self.input_entry = Entry(input_frame, font=("Helvetica", 12))
        self.input_entry.pack(side=LEFT, padx=5)
        
        # Operation buttons
        Button(
            input_frame,
            text="Add Element",
            command=self.add_element,
            bg="#4CAF50",
            fg="white",
            font=("Helvetica", 10)
        ).pack(side=LEFT, padx=5)
        
        Button(
            input_frame,
            text="Remove Element",
            command=self.remove_element,
            bg="#f44336",
            fg="white",
            font=("Helvetica", 10)
        ).pack(side=LEFT, padx=5)
        
        self.update_result()

    def setup_tuple_operations(self):
        self.clear_operations_frame()
        self.current_mode = "tuple"
        
        # Input frame
        input_frame = Frame(self.operations_frame, bg="#f0f0f0")
        input_frame.pack(fill=X, pady=20)
        
        Label(
            input_frame,
            text="Enter element:",
            font=("Helvetica", 12),
            bg="#f0f0f0"
        ).pack(side=LEFT, padx=5)
        
        self.input_entry = Entry(input_frame, font=("Helvetica", 12))
        self.input_entry.pack(side=LEFT, padx=5)
        
        # Operation buttons
        Button(
            input_frame,
            text="Add Element",
            command=self.add_element,
            bg="#2196F3",
            fg="white",
            font=("Helvetica", 10)
        ).pack(side=LEFT, padx=5)
        
        Button(
            input_frame,
            text="Clear Tuple",
            command=self.clear_tuple,
            bg="#f44336",
            fg="white",
            font=("Helvetica", 10)
        ).pack(side=LEFT, padx=5)
        
        self.update_result()

    def add_element(self):
        value = self.input_entry.get().strip()
        if not value:
            messagebox.showwarning("Warning", "Please enter a value")
            return
            
        if self.current_mode == "set":
            self.set_data.add(value)
        else:  # tuple
            self.tuple_data += (value,)
            
        self.input_entry.delete(0, END)
        self.update_result()

    def remove_element(self):
        value = self.input_entry.get().strip()
        if not value:
            messagebox.showwarning("Warning", "Please enter a value")
            return
            
        if value in self.set_data:
            self.set_data.remove(value)
            self.input_entry.delete(0, END)
            self.update_result()
        else:
            messagebox.showwarning("Warning", "Element not found in set")

    def clear_tuple(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear the tuple?"):
            self.tuple_data = ()
            self.update_result()

    def update_result(self):
        if self.current_mode == "set":
            self.result_label.config(
                text=f"Current Set: {self.set_data}",
                fg="#4CAF50"
            )
        else:  # tuple
            self.result_label.config(
                text=f"Current Tuple: {self.tuple_data}",
                fg="#2196F3"
            )

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = DataStructureGUI()
    app.run()
