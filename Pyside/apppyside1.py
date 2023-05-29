import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QFileDialog, QLabel, QVBoxLayout, QWidget, QSlider, QHBoxLayout, QPushButton
from PySide2.QtGui import QImageReader, QImage, QPixmap, QPainter, QPen, QColor
from PySide2.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Processing with PySide2")
        self.setGeometry(100, 100, 800, 600)

        # Menu bar
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("Fichier")

        open_action = QAction("Ouvrir", self)
        open_action.triggered.connect(self.open_image)
        file_menu.addAction(open_action)

        save_action = QAction("Enregistrer", self)
        save_action.triggered.connect(self.save_image)
        file_menu.addAction(save_action)

        # Image operations menu
        operations_menu = menu_bar.addMenu("Opérations")

        rotate_action = QAction("Rotation", self)
        rotate_action.triggered.connect(self.rotate_image)
        operations_menu.addAction(rotate_action)

        resize_action = QAction("Redimensionner", self)
        resize_action.triggered.connect(self.resize_image)
        operations_menu.addAction(resize_action)

        # New options
        invert_action = QAction("Inverser les couleurs", self)
        invert_action.triggered.connect(self.invert_colors)
        operations_menu.addAction(invert_action)

        grayscale_action = QAction("Niveaux de gris", self)
        grayscale_action.triggered.connect(self.convert_to_grayscale)
        operations_menu.addAction(grayscale_action)

        blur_action = QAction("Flou", self)
        blur_action.triggered.connect(self.apply_blur)
        operations_menu.addAction(blur_action)
        # New options
        # sepia_action = QAction("Filtre sépia", self)
        # sepia_action.triggered.connect(self.apply_sepia)
        # operations_menu.addAction(sepia_action)

        duplicate_action = QAction("Dupliquer", self)
        duplicate_action.triggered.connect(self.duplicate_image)
        operations_menu.addAction(duplicate_action)

        # add_text_action = QAction("Ajouter un texte", self)
        # add_text_action.triggered.connect(self.add_text)
        # operations_menu.addAction(add_text_action)

        # New options
        sepia_action = QAction("Filtre sépia", self)
        sepia_action.triggered.connect(self.apply_sepia_filter)
        operations_menu.addAction(sepia_action)

        duplicate_action = QAction("Dupliquer", self)
        duplicate_action.triggered.connect(self.duplicate_image)
        operations_menu.addAction(duplicate_action)

        mirror_horizontal_action = QAction("Miroir horizontal", self)
        mirror_horizontal_action.triggered.connect(self.mirror_horizontal)
        operations_menu.addAction(mirror_horizontal_action)

        mirror_vertical_action = QAction("Miroir vertical", self)
        mirror_vertical_action.triggered.connect(self.mirror_vertical)
        operations_menu.addAction(mirror_vertical_action)

        # Image display
        self.image_label = QLabel(self)
        self.setCentralWidget(self.image_label)

        # Image display
        self.image_label = QLabel(self)
        self.setCentralWidget(self.image_label)

    def apply_sepia_filter(self):
        if hasattr(self, 'image'):
            for y in range(self.image.height()):
                for x in range(self.image.width()):
                    pixel = QColor(self.image.pixel(x, y))
                    gray = pixel.red() * 0.3 + pixel.green() * 0.59 + pixel.blue() * 0.11
                    red = gray + 40
                    green = gray + 20
                    blue = gray
                    self.image.setPixel(x, y, QColor(red, green, blue).rgb())
            self.display_image()

    def duplicate_image(self):
        if hasattr(self, 'image'):
            self.image = self.image.copy()
            self.display_image()

    def mirror_horizontal(self):
        if hasattr(self, 'image'):
            self.image = self.image.mirrored(True, False)
            self.display_image()

    def mirror_vertical(self):
        if hasattr(self, 'image'):
            self.image = self.image.mirrored(False, True)
            self.display_image()

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Ouvrir l'image", "", "Images (*.png *.xpm *.jpg *.bmp)")
        if file_name:
            image_reader = QImageReader(file_name)
            self.image = image_reader.read()
            self.display_image()

    def invert_colors(self):
        if hasattr(self, 'image'):
            self.image.invertPixels()
            self.display_image()

    def convert_to_grayscale(self):
        if hasattr(self, 'image'):
            self.image = self.image.convertToFormat(QImage.Format_Grayscale8)
            self.display_image()

    def apply_blur(self):
        if hasattr(self, 'image'):
            self.image = self.image.scaled(self.image.width() * 2, self.image.height() * 2, Qt.KeepAspectRatio,
                                           Qt.SmoothTransformation)
            self.image = self.image.scaled(self.image.width() // 2, self.image.height() // 2, Qt.KeepAspectRatio,
                                           Qt.SmoothTransformation)
            self.display_image()

    def save_image(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Enregistrer l'image", "", "Images (*.png *.xpm *.jpg *.bmp)")
        if file_name:
            self.image.save(file_name)

    def display_image(self):
        pixmap = QPixmap.fromImage(self.image)
        self.image_label.setPixmap(pixmap)
        self.image_label.adjustSize()

    def rotate_image(self):
        if hasattr(self, 'image'):
            rotation_dialog = QWidget()
            rotation_dialog.setWindowTitle("Rotation")

            vbox = QVBoxLayout()

            slider = QSlider(Qt.Horizontal)
            vbox.addWidget(slider)

            hbox = QHBoxLayout()

            ok_button = QPushButton("OK")
            ok_button.clicked.connect(rotation_dialog.accept)
            hbox.addWidget(ok_button)

            cancel_button = QPushButton("Annuler")
            cancel_button.clicked.connect(rotation_dialog.reject)
            hbox.addWidget(cancel_button)

            vbox.addLayout(hbox)

            rotation_dialog.setLayout(vbox)

            if rotation_dialog.exec_():
                angle = slider.value()
                transform = QTransform().rotate(angle)
                self.image = self.image.transformed(transform)
                self.display_image()

    def resize_image(self):
        if hasattr(self, 'image'):
            resize_dialog = QWidget()
            resize_dialog.setWindowTitle("Redimensionner")

            vbox = QVBoxLayout()

            width_slider = QSlider(Qt.Horizontal)
            width_slider.setMaximum(self.image.width() * 2)
            width_slider.setValue(self.image.width())
            vbox.addWidget(width_slider)

            height_slider = QSlider(Qt.Horizontal)
            height_slider.setMaximum(self.image.height() * 2)
            height_slider.setValue(self.image.height())
            vbox.addWidget(height_slider)

            hbox = QHBoxLayout()

            ok_button = QPushButton("OK")
            ok_button.clicked.connect(resize_dialog.accept)
            hbox.addWidget(ok_button)

            cancel_button = QPushButton("Annuler")
            cancel_button.clicked.connect(resize_dialog.reject)
            hbox.addWidget(cancel_button)

            vbox.addLayout(hbox)

            resize_dialog.setLayout(vbox)

            if resize_dialog.exec_():
                new_width = width_slider.value()
                new_height = height_slider.value()
                self.image = self.image.scaled(new_width, new_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.display_image()
if __name__ == "__main__":
            app = QApplication(sys.argv)
            window = MainWindow()
            window.show()
            sys.exit(app.exec_())

