from tkinter import *
from tkinter import messagebox, ttk
import math

class PrimeFactorCalculator:
    def __init__(self):
        self.window = Tk()
        self.setup_window()
        self.create_widgets()
        self.history = []

    def setup_window(self):
        self.window.title("Prime Factor Calculator")
        self.window.geometry("1200x800")
        self.window.configure(bg="#f5f5f5")
        
        # Configure style
        style = ttk.Style()
        style.configure("Title.TLabel", 
                       font=("Helvetica", 24, "bold"), 
                       background="#f5f5f5")
        style.configure("Description.TLabel", 
                       font=("Helvetica", 12), 
                       background="#f5f5f5",
                       wraplength=800)

    def create_widgets(self):
        # Main container
        main_frame = Frame(self.window, bg="#f5f5f5", padx=40, pady=20)
        main_frame.pack(fill=BOTH, expand=True)

        # Header with logo
        try:
            photo = PhotoImage(file="python-GUI/rv new logo.png").subsample(2, 2)
            logo_label = Label(main_frame, image=photo, bg="#f5f5f5")
            logo_label.image = photo
            logo_label.pack(pady=(0, 20))
        except:
            pass

        # Title and Description
        title_frame = Frame(main_frame, bg="#f5f5f5")
        title_frame.pack(fill=X, pady=(0, 20))

        title = Label(
            title_frame,
            text="Largest Prime Factor Calculator",
            font=("Helvetica", 28, "bold"),
            bg="#f5f5f5",
            fg="#2c3e50"
        )
        title.pack()

        description = Label(
            title_frame,
            text="""A prime factor is a prime number that divides another number without leaving a remainder.
            \nFor example, the prime factors of 18 are 2×3×3, where 3 is the largest prime factor.
            \nNote: Numbers 0 and 1 are not valid inputs as they don't have prime factors.""",
            font=("Helvetica", 14),
            bg="#f5f5f5",
            fg="#7f8c8d",
            justify=LEFT,
            wraplength=800
        )
        description.pack(pady=(10, 20))

        # Input Frame
        input_frame = Frame(main_frame, bg="#f5f5f5")
        input_frame.pack(fill=X, pady=20)

        self.input_label = Label(
            input_frame,
            text="Enter a number:",
            font=("Helvetica", 16, "bold"),
            bg="#f5f5f5",
            fg="#2c3e50"
        )
        self.input_label.pack(side=LEFT, padx=(0, 10))

        self.entry = Entry(
            input_frame,
            font=("Helvetica", 16),
            width=20,
            bd=2,
            relief=SOLID
        )
        self.entry.pack(side=LEFT, padx=10)
        self.entry.bind('<Return>', lambda e: self.calculate())

        # Buttons Frame
        buttons_frame = Frame(main_frame, bg="#f5f5f5")
        buttons_frame.pack(fill=X, pady=20)

        button_style = {
            "font": ("Helvetica", 14, "bold"),
            "width": 12,
            "height": 1,
            "bd": 0,
            "cursor": "hand2"
        }

        self.calculate_btn = Button(
            buttons_frame,
            text="Calculate",
            command=self.calculate,
            bg="#2ecc71",
            fg="white",
            **button_style
        )
        self.calculate_btn.pack(side=LEFT, padx=5)

        self.clear_btn = Button(
            buttons_frame,
            text="Clear",
            command=self.clear,
            bg="#e74c3c",
            fg="white",
            **button_style
        )
        self.clear_btn.pack(side=LEFT, padx=5)

        self.history_btn = Button(
            buttons_frame,
            text="Show History",
            command=self.show_history,
            bg="#3498db",
            fg="white",
            **button_style
        )
        self.history_btn.pack(side=LEFT, padx=5)

        # Result Frame
        result_frame = Frame(main_frame, bg="#f5f5f5")
        result_frame.pack(fill=X, pady=20)

        self.result_label = Label(
            result_frame,
            text="",
            font=("Helvetica", 20),
            bg="#f5f5f5",
            fg="#2c3e50"
        )
        self.result_label.pack()

        # Steps Frame
        self.steps_frame = Frame(main_frame, bg="#f5f5f5")
        self.steps_frame.pack(fill=X, pady=20)

        self.steps_label = Label(
            self.steps_frame,
            text="",
            font=("Helvetica", 14),
            bg="#f5f5f5",
            fg="#7f8c8d",
            justify=LEFT
        )
        self.steps_label.pack()

    def largest_prime_factor(self, n):
        steps = [f"Finding largest prime factor of {n}:"]
        max_prime = -1
        
        # Handle 2 separately
        while n % 2 == 0:
            max_prime = 2
            n = n // 2
            steps.append("Found factor 2")
        
        # Check odd numbers up to sqrt(n)
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                max_prime = i
                n = n // i
                steps.append(f"Found factor {i}")
        
        # If n is still greater than 2, it's prime
        if n > 2:
            max_prime = n
            steps.append(f"Final prime factor {n}")
        
        return int(max_prime), steps

    def calculate(self):
        try:
            num = int(self.entry.get())
            if num <= 1:
                messagebox.showwarning(
                    "Invalid Input",
                    "Please enter a number greater than 1"
                )
                return
                
            result, steps = self.largest_prime_factor(num)
            
            # Update result
            self.result_label.config(
                text=f"Largest Prime Factor of {num} is {result}",
                fg="#27ae60"
            )
            
            # Show steps
            self.steps_label.config(text="\n".join(steps))
            
            # Add to history
            self.history.append(f"{num} → {result}")
            
        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter a valid integer"
            )

    def clear(self):
        self.entry.delete(0, END)
        self.result_label.config(text="")
        self.steps_label.config(text="")

    def show_history(self):
        history_window = Toplevel(self.window)
        history_window.title("Calculation History")
        history_window.geometry("400x500")
        history_window.configure(bg="#f5f5f5")
        
        Label(
            history_window,
            text="Calculation History",
            font=("Helvetica", 16, "bold"),
            bg="#f5f5f5",
            fg="#2c3e50"
        ).pack(pady=20)
        
        if not self.history:
            Label(
                history_window,
                text="No calculations yet",
                font=("Helvetica", 12),
                bg="#f5f5f5",
                fg="#7f8c8d"
            ).pack()
        else:
            for calc in reversed(self.history):
                Label(
                    history_window,
                    text=calc,
                    font=("Helvetica", 12),
                    bg="#f5f5f5",
                    fg="#2c3e50"
                ).pack(pady=5)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = PrimeFactorCalculator()
    app.run()
