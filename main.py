import cv2
import numpy as np
from manim import *

class Scene1(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, RIGHT, buff=0.5)

        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6', font_size=96)
        self.add(tex)

        self.play(Create(circle), Create(square))
        self.play(Transform(square, tex))

def render_manim_scene_to_video(scene_class, output_file):
    config.pixel_height = 480
    config.pixel_width = 854
    config.frame_rate = 30
    config.output_file = output_file
    config.save_last_frame = False
    config.preview = False

    scene = scene_class()
    scene.render()

def display_video_with_opencv():
    cap = cv2.VideoCapture(r'media\videos\480p30\manim_animation.mp4')
    while True:
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = cap.read()
        cv2.imshow('Manim Animation', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        video_file = "manim_animation.mp4"
        render_manim_scene_to_video(Scene1, video_file)
        display_video_with_opencv()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure that all required executables (such as pdflatex) are installed and available in your system's PATH.")