import tkinter as tk
import movie_success


class MovieSuccess:
    def __init__(self, master):
        self.master = master

        # Create a label to display the float number
        self.acc_label = tk.Label(master, text="")
        self.acc_label.pack()
        # generate accuracy
        self.gen_acc_button = tk.Button(master, text="Generate Accuracy", command=self.update_acc_label)
        self.gen_acc_button.pack()

        # self.confusion_matrix = movie_success.confusion_matrix
        self.accuracy = str(movie_success.accuracy)

    def update_acc_label(self):
        # Update the float number label with the float number
        self.acc_label.config(text=f"Accuracy Score: {self.accuracy}")


root = tk.Tk()
root.title("Random Forest Classification of Movie Success Data")
mov = MovieSuccess(root)
root.mainloop()
