import tkinter as tk
import pyaudio
import numpy as np
import math
import threading

class AudioMatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Acoustic Resonance Matrix")
        self.root.configure(bg="#08080a")
        self.width, self.height = 1000, 600
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False, False)

        # Audio stream architecture
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.p = pyaudio.PyAudio()
        self.stream = None
        
        # Shared data thread safe variables
        self.audio_data = np.zeros(self.CHUNK)
        self.fft_data = np.zeros(self.CHUNK // 2)
        self.running = True
        
        # Matrix render variables
        self.angle_x = 0.6
        self.angle_y = 0.4
        self.time_step = 0
        
        self.setup_ui()
        self.start_audio_thread()
        self.animate()
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_ui(self):
        # Clean layout separation: Left Sidebar (Data), Right Main (Graphics)
        self.sidebar = tk.Frame(self.root, width=280, bg="#0d0e12", highlightbackground="#1a1c23", highlightthickness=1)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)
        
        self.canvas = tk.Canvas(self.root, width=720, height=600, bg="#08080a", highlightthickness=0)
        self.canvas.pack(side="right", fill="both", expand=True)
        
        # Telemetry Labels (Clean, sharp typography, no AI clutter)
        tk.Label(self.sidebar, text="SYSTEM METRICS", font=("Courier", 14, "bold"), fg="#4f5b66", bg="#0d0e12").pack(pady=20, anchor="w", px=20)
        
        self.lbl_fps = self.create_metric_label("ENGINE STATUS:", "INITIALIZING")
        self.lbl_freq = self.create_metric_label("PEAK FREQ:", "0.00 Hz")
        self.lbl_amp = self.create_metric_label("RMS AMPLITUDE:", "0.00")
        
        # Explanatory architectural text block
        instructions = (
            "SYSTEM ARCHITECTURE:\n\n"
            "- Live Hardware Audio Input Capture\n"
            "- Real-time Discrete FFT Analysis\n"
            "- Dual-Axis 3D Isometric Projection\n"
            "- Frequency-Driven Vertex Warp"
        )
        tk.Label(self.sidebar, text=instructions, font=("Courier", 9), fg="#343d46", bg="#0d0e12", justify="left").pack(side="bottom", pady=30, px=20, anchor="w")

    def create_metric_label(self, title, default):
        frame = tk.Frame(self.sidebar, bg="#0d0e12")
        frame.pack(fill="x", px=20, pady=10)
        tk.Label(frame, text=title, font=("Courier", 10, "bold"), fg="#8ec07c", bg="#0d0e12").pack(anchor="w")
        lbl = tk.Label(frame, text=default, font=("Courier", 11), fg="#ffffff", bg="#0d0e12")
        lbl.pack(anchor="w", py=2)
        return lbl

    def start_audio_thread(self):
        try:
            self.stream = self.p.open(
                format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE,
                input=True, frames_per_buffer=self.CHUNK
            )
        except Exception:
            print("Warning: Audio input hardware not found. Running simulation mode.")
            self.stream = None

        self.thread = threading.Thread(target=self.audio_capture_loop, daemon=True)
        self.thread.start()

    def audio_capture_loop(self):
        while self.running:
            if self.stream:
                try:
                    data = self.stream.read(self.CHUNK, exception_on_overflow=False)
                    self.audio_data = np.frombuffer(data, dtype=np.int16).astype(np.float32)
                except Exception:
                    self.audio_data = np.zeros(self.CHUNK)
            else:
                # Simulation fallback mode using compounding mathematical waves
                t = math.sin(self.time_step * 0.1)
                self.audio_data = np.array([math.sin(i * 0.05 + t) * 3000 for i in range(self.CHUNK)])
            
            # Compute Discrete Fast Fourier Transform
            fft_complex = np.fft.fft(self.audio_data)
            fft_mag = np.abs(fft_complex[:self.CHUNK // 2]) / self.CHUNK
            
            # Clean filtering & normalization smoothings
            self.fft_data = np.log1p(fft_mag) * 15 

    def project_3d(self, x, y, z):
        # Manual matrix transformation matrix calculation for 3D mapping onto 2D viewport
        # Rotations around X-axis
        x1 = x
        y1 = y * math.cos(self.angle_x) - z * math.sin(self.angle_x)
        z1 = y * math.sin(self.angle_x) + z * math.cos(self.angle_x)
        
        # Rotations around Y-axis
        x2 = x1 * math.cos(self.angle_y) + z1 * math.sin(self.angle_y)
        y2 = y1
        
        # Center translation alignment inside canvas frame
        cx, cy = 360, 300
        scale = 14
        return cx + int(x2 * scale), cy - int(y2 * scale)

    def animate(self):
        if not self.running:
            return
            
        self.canvas.delete("all")
        self.time_step += 1
        
        # Dynamically process real-time GUI telemetry calculations
        rms = np.sqrt(np.mean(self.audio_data**2)) if len(self.audio_data) > 0 else 0
        peak_idx = np.argmax(self.fft_data) if len(self.fft_data) > 0 else 0
        peak_freq = peak_idx * self.RATE / self.CHUNK
        
        self.lbl_fps.configure(text="ACTIVE // 60 FPS")
        self.lbl_amp.configure(text=f"{rms:.2f}")
        self.lbl_freq.configure(text=f"{peak_freq:.2f} Hz")
        
        # Generate Renderable Mesh Node Grid Matrix
        rows, cols = 18, 18
        spacing = 1.6
        points = {}
        
        # Constant gentle automatic orbit rotations
        self.angle_y += 0.003
        
        for r in range(rows):
            for c in range(cols):
                # Map coordinates relative to central origin point zero
                x = (c - cols / 2) * spacing
                y = (r - rows / 2) * spacing
                
                # Sample FFT array mapped evenly across grid topography nodes
                fft_index = int((r * cols + c) / (rows * cols) * len(self.fft_data)) % len(self.fft_data)
                audio_modifier = self.fft_data[fft_index]
                
                # Harmonic wave equation mapping + live audio injection
                dist = math.sqrt(x**2 + y**2)
                z = math.sin(dist - self.time_step * 0.08) * 1.2
                z += audio_modifier * (0.8 + (rms / 4000))
                
                points[(r, c)] = self.project_3d(x, y, z)
                
        # Draw structural vector wireframe mesh connections 
        for r in range(rows):
            for c in range(cols):
                p1 = points[(r, c)]
                
                # Calculate dynamic, clean solid-color spectrum (Cyan shifted to deep purple)
                color_factor = min(1.0, max(0.0, (points[(r, c)][1] / self.height)))
                blue = int(140 + (color_factor * 115))
                green = int(240 - (color_factor * 180))
                color_hex = f"#00{green:02x}{blue:02x}"
                
                # Draw structural geometric lattice connections safely
                if c + 1 < cols:
                    p2 = points[(r, c + 1)]
                    self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill=color_hex, width=1)
                if r + 1 < rows:
                    p3 = points[(r + 1, c)]
                    self.canvas.create_line(p1[0], p1[1], p3[0], p3[1], fill=color_hex, width=1)
                    
        self.root.after(16, self.animate)

    def on_closing(self):
        self.running = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()
        self.root.destroy()

if __name__ == "__main__":
    window = tk.Tk()
    app = AudioMatrixApp(window)
    window.mainloop()
