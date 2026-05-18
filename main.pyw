import tkinter as tk
import random
import math

class ParticleSandbox:
    def __init__(self, root):
        self.root = root
        self.root.title("Orbit")
        self.root.configure(bg="#0b0c10")
        
        self.width, self.height = 700, 500
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="#0b0c10", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Particle properties: [x, y, vx, vy, color]
        self.particles = []
        self.max_particles = 120
        
        # Track mouse coordinates
        self.mx, self.my = self.width // 2, self.height // 2
        self.root.bind("<Motion>", self.track_mouse)
        
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False, False)
        
        self.update()

    def track_mouse(self, event):
        self.mx, self.my = event.x, event.y

    def spawn_particle(self):
        if len(self.particles) < self.max_particles:
            # Spawn near the top center with slight random drift
            self.particles.append([
                random.randint(self.width // 2 - 30, self.width // 2 + 30), 0,
                random.uniform(-0.5, 0.5), random.uniform(1, 3),
                random.choice(["#66fcf1", "#45f3ff", "#1f2833"])
            ])

    def update(self):
        self.canvas.delete("all")
        self.spawn_particle()
        
        # Physics constants
        gravity_strength = 0.25
        friction = 0.99
        
        for p in self.particles[:]:
            # Vector math toward mouse cursor
            dx = self.mx - p[0]
            dy = self.my - p[1]
            distance = math.sqrt(dx**2 + dy**2) + 0.1  # Prevents division by zero
            
            if distance < 400:
                # Stronger pull the closer it gets
                force = (400 - distance) / 400 * gravity_strength
                p[2] += (dx / distance) * force
                p[3] += (dy / distance) * force
            
            # Apply physics and inertia
            p[2] *= friction
            p[3] *= friction
            p[0] += p[2]
            p[1] += p[3]
            
            # Natural downward gravity drift if far from mouse
            p[3] += 0.05 
            
            # Draw particle
            self.canvas.create_rectangle(p[0], p[1], p[0]+3, p[1]+3, fill=p[4], outline="")
            
            # Recycle particles that leave the screen bounds
            if p[1] > self.height or p[0] < 0 or p[0] > self.width:
                self.particles.remove(p)
                
        self.root.after(16, self.update)

if __name__ == "__main__":
    window = tk.Tk()
    app = ParticleSandbox(window)
    window.mainloop()
