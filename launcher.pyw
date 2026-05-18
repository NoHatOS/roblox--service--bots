import tkinter as tk
import math

class ElegantMatrix:
    def __init__(self, root):
        self.root = root
        self.root.title("Resonance")
        self.root.configure(bg="black")
        
        # Setup canvas
        self.size = 600
        self.canvas = tk.Canvas(root, width=self.size, height=self.size, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Animation variables
        self.angle = 0
        self.lines = 36
        self.center = self.size // 2
        
        # Window sizing and centering
        self.root.geometry(f"{self.size}x{self.size}")
        self.root.resizable(False, False)
        
        self.animate()

    def animate(self):
        self.canvas.delete("all")
        self.angle += 0.015
        
        # Dynamic pulse based on a sine wave
        pulse = (math.sin(self.angle * 2) + 1) / 2  # Normalizes to 0-1
        radius = 100 + (pulse * 120)
        
        for i in range(self.lines):
            # Calculate rotation angles for interconnected lines
            theta1 = (i * 2 * math.pi / self.lines) + self.angle
            theta2 = (i * 2 * math.pi / self.lines) - (self.angle * 1.5)
            
            # Inner and outer coordinate mappings
            x1 = self.center + radius * math.cos(theta1)
            y1 = self.center + radius * math.sin(theta1)
            
            x2 = self.center + (radius / 2) * math.cos(theta2)
            y2 = self.center + (radius / 2) * math.sin(theta2)
            
            # Subtle, elegant color shifting (gradient from deep slate to cyan)
            green_val = int(100 + (pulse * 155))
            blue_val = int(180 + (math.cos(self.angle) * 75))
            color = f"#00{green_val:02x}{blue_val:02x}"
            
            # Draw the geometry
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=1.5)
            self.canvas.create_oval(x1-2, y1-2, x1+2, y1+2, fill="#ffffff", outline="")

        # ~60 frames per second smooth loop
        self.root.after(16, self.animate)

if __name__ == "__main__":
    window = tk.Tk()
    app = ElegantMatrix(window)
    window.mainloop()
