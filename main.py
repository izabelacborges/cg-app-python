from tkinter import *
from math import pow, sqrt

class graphics_app:
    
    # ---------- DRAW LINES ----------
    
    def draw_dda(self):
        
        x1 = int(self.x1_value.get())
        y1 = int(self.y1_value.get())
        x2 = int(self.x2_value.get())
        y2 = int(self.y2_value.get())

        self.object_lst = [x1, y1, x2, y2]

        dx = x2 - x1
        dy = y2 - y1

        steps, x, y = 0, x1, y1

        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)
        
        x_increment = dx/steps
        y_increment = dy/steps

        for i in range(steps):
            x = x + x_increment
            y = y + y_increment

            self.canvas.create_rectangle(round(x), round(y), round(x)+1, round(y)+1)
    
    def draw_bresenham(self):
        
        x1 = int(self.x1_value.get())
        y1 = int(self.y1_value.get())
        x2 = int(self.x2_value.get())
        y2 = int(self.y2_value.get())

        self.object_lst = [x1, y1, x2, y2]

        x, y = x1, y1
        
        self.canvas.create_rectangle(x, y, x+1, y+1)
        
        dx = x2 - x1
        dy = y2 - y1
        x_increment, y_increment = 0, 0
        
        if dx < 0:
            dx = dx * -1
            x_increment = -1
        else:
            x_increment = 1

        if dy < 0:
            dy = dy * -1
            y_increment = -1
        else:
            y_increment = 1

        if dx > dy:
            p = 2*dy - dx
            c1 = 2*dy
            c2 = 2*(dy-dx)

            for i in range(dx):
                x = x + x_increment
                if p < 0:
                    p = p + c1
                else:
                    p = p + c2
                    y = y + y_increment

                self.canvas.create_rectangle(x, y, x+1, y+1)
        else:
            p = 2*dx - dy
            c1 = 2*dx
            c2 = 2*(dx-dy)

            for i in range(dx):
                y = y + y_increment
                if p < 0:
                    p = p + c1
                else:
                    p = p + c2
                    x = x + x_increment

                self.canvas.create_rectangle(x, y, x+1, y+1)

    def draw_parametric(self):
        pass

    # ---------- DRAW CIRCUMFERENCE ----------
 
    def draw_circle(self):
        
        cx = int(self.x1_value.get())
        cy = int(self.y1_value.get())
        x = int(self.x2_value.get())
        y = int(self.y2_value.get()) 
        radius = sqrt(pow((x - cx), 2) + pow((y - cy), 2))

        self.object_lst = [x1, y1, x2, y2]

        x = 0
        y = int(radius)
        p = 3 - 2*radius
        self.draw_symmetric(x, y, cx, cy)

        while x < y:
            if p < 0:
                p += 4 * x + 6
            else:
                p += 4 * (x - y) + 10
                y = y - 1
            x = x + 1
            self.draw_symmetric(x, y, cx, cy)

    def draw_symmetric(self, x, y, cx, cy):

        self.canvas.create_rectangle((cx + x), (cy + y), (cx + x)+1, (cy + y)+1)
        self.canvas.create_rectangle((cx + x), (cy - y), (cx + x)+1, (cy - y)+1)
        self.canvas.create_rectangle((cx - x), (cy + y), (cx - x)+1, (cy + y)+1)
        self.canvas.create_rectangle((cx - x), (cy - y), (cx - x)+1, (cy - y)+1)
        self.canvas.create_rectangle((cx + y), (cy + x), (cx + y)+1, (cy + x)+1)
        self.canvas.create_rectangle((cx + y), (cy - x), (cx + y)+1, (cy - x)+1)
        self.canvas.create_rectangle((cx - y), (cy + x), (cx - y)+1, (cy + x)+1)
        self.canvas.create_rectangle((cx - y), (cy - x), (cx - y)+1, (cy - x)+1)

    # ---------- MODIFICATIONS ----------
 
    def translate(self):
        self.canvas.delete(ALL)

    def scale(self):
        self.canvas.delete(ALL)

    def rotate(self):
        self.canvas.delete(ALL)

    def crop(self):
        pass

    # ---------- CLEAR CANVAS ----------
 
    def clear_canvas(self):
        self.object_lst = []
        self.canvas.delete(ALL)


    def __init__(self):

        # ---------- SETTING VARIABLES ----------

        win_width = 800
        win_height = 630
        canvas_width = 700
        canvas_height = 500

        self.object_lst = []

        # ---------- SETTING WINDOW ----------

        window = Tk()
        window.title("Computer Graphics App")
        window.resizable(width=False, height=False)
        window.geometry('{}x{}'.format(win_width, win_height))

        # ---------- SETTING CANVAS AND IMAGE ----------

        self.canvas = Canvas(window, width=canvas_width, height=canvas_height, bg="#ffffff")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        # ---------- TEXT INPUTS ----------

        label_one = Label(frame, text="Insira os valores de x1 e y1: ").grid(row = 1, column = 2)
        self.x1_value = StringVar()
        Entry(frame, textvariable = self.x1_value).grid(row = 1, column = 3)
        self.y1_value = StringVar()
        Entry(frame, textvariable = self.y1_value).grid(row = 1, column = 4)

        label_two = Label(frame, text="Insira os valores de x2 e y2: ").grid(row = 2, column = 2)
        self.x2_value = StringVar()
        Entry(frame, textvariable = self.x2_value).grid(row = 2, column = 3)
        self.y2_value = StringVar()
        Entry(frame, textvariable = self.y2_value).grid(row = 2, column = 4)

        # ---------- ACTIONS FOR BUTTONS ----------

        dda_button = Button(frame, text="DDA", command = self.draw_dda)
        dda_button.grid(row = 3, column = 1)
        
        bresenham_button = Button(frame, text="Bresenham", command = self.draw_bresenham)
        bresenham_button.grid(row = 3, column = 2)
        
        parametric_button = Button(frame, text="Equação Paramétrica", command = self.draw_parametric)
        parametric_button.grid(row = 3, column = 3)
        
        circumference_button = Button(frame, text="Circunferência", command = self.draw_circle)
        circumference_button.grid(row = 3, column = 4)

        clear_button = Button(frame, text="Apagar", command = self.clear_canvas)
        clear_button.grid(row = 3, column = 5)

        crop_button = Button(frame, text="Recorte", command = self.crop)
        crop_button.grid(row = 4, column = 1)

        translation_button = Button(frame, text="Translação", command = self.translate)
        translation_button.grid(row = 4, column = 2)
        
        scale_button = Button(frame, text="Escala", command = self.scale)
        scale_button.grid(row = 4, column = 3)
        
        rotation_button = Button(frame, text="Rotação", command = self.rotate)
        rotation_button.grid(row = 4, column = 4)

        # ---------- EVENT LOOP ----------

        window.mainloop()

cg_app = graphics_app()
