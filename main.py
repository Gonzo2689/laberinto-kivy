from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from random import randint

# ======================================================
# CONFIGURACIÓN
# ======================================================
Window.size = (400, 700)

TAM_JUGADOR = 40
VELOCIDAD = 20

# ======================================================
# CLASE DEL JUEGO
# ======================================================
class Juego(Widget):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        # ==========================
        # JUGADOR
        # ==========================
        self.jugador_x = 50
        self.jugador_y = 50

        # ==========================
        # META
        # ==========================
        self.meta_x = 300
        self.meta_y = 600

        # ==========================
        # DIBUJAR
        # ==========================
        with self.canvas:

            # Fondo
            Color(0.9, 0.9, 0.9)
            self.fondo = Rectangle(
                pos=(0, 0),
                size=Window.size
            )

            # Meta
            Color(0, 1, 0)
            self.meta = Rectangle(
                pos=(self.meta_x, self.meta_y),
                size=(50, 50)
            )

            # Jugador
            Color(1, 0, 0)
            self.jugador = Rectangle(
                pos=(self.jugador_x, self.jugador_y),
                size=(TAM_JUGADOR, TAM_JUGADOR)
            )

        # ==========================
        # TEXTO GANADOR
        # ==========================
        self.label = Label(
            text="",
            font_size=30,
            pos=(0, 300)
        )

        self.add_widget(self.label)

        # ==========================
        # BOTONES
        # ==========================
        btn_up = Button(
            text="↑",
            size_hint=(None, None),
            size=(80, 80),
            pos=(160, 150)
        )

        btn_down = Button(
            text="↓",
            size_hint=(None, None),
            size=(80, 80),
            pos=(160, 50)
        )

        btn_left = Button(
            text="←",
            size_hint=(None, None),
            size=(80, 80),
            pos=(70, 50)
        )

        btn_right = Button(
            text="→",
            size_hint=(None, None),
            size=(80, 80),
            pos=(250, 50)
        )

        btn_up.bind(on_press=self.mover_arriba)
        btn_down.bind(on_press=self.mover_abajo)
        btn_left.bind(on_press=self.mover_izquierda)
        btn_right.bind(on_press=self.mover_derecha)

        self.add_widget(btn_up)
        self.add_widget(btn_down)
        self.add_widget(btn_left)
        self.add_widget(btn_right)

        Clock.schedule_interval(self.update, 1/60)

    # ==================================================
    # MOVIMIENTO
    # ==================================================
    def mover_arriba(self, instance):

        self.jugador_y += VELOCIDAD

    def mover_abajo(self, instance):

        self.jugador_y -= VELOCIDAD

    def mover_izquierda(self, instance):

        self.jugador_x -= VELOCIDAD

    def mover_derecha(self, instance):

        self.jugador_x += VELOCIDAD

    # ==================================================
    # UPDATE
    # ==================================================
    def update(self, dt):

        # Limitar pantalla
        if self.jugador_x < 0:
            self.jugador_x = 0

        if self.jugador_x > Window.width - TAM_JUGADOR:
            self.jugador_x = Window.width - TAM_JUGADOR

        if self.jugador_y < 0:
            self.jugador_y = 0

        if self.jugador_y > Window.height - TAM_JUGADOR:
            self.jugador_y = Window.height - TAM_JUGADOR

        # Actualizar posición
        self.jugador.pos = (
            self.jugador_x,
            self.jugador_y
        )

        # Detectar victoria
        if (
            abs(self.jugador_x - self.meta_x) < 40 and
            abs(self.jugador_y - self.meta_y) < 40
        ):

            self.label.text = "¡GANASTE!"

# ======================================================
# APP
# ======================================================
class LaberintoApp(App):

    def build(self):

        return Juego()

# ======================================================
# EJECUTAR
# ======================================================
if __name__ == "__main__":

    LaberintoApp().run()