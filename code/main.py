from tkinter import Tk, filedialog, simpledialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import os

# Funkcja do określenia płci na podstawie końcówki imienia
def determine_certificate_background(first_name, female_template, male_template):
    return female_template if first_name.endswith('a') else male_template

# Wczytaj dane z pliku imiona.txt
def load_names_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip().split() for line in lines]

global triggerNumering
triggerNumering =1 #flaga do numerów

# Główna funkcja generowania certyfikatów
def generate_certificates(input_file, female_template, male_template, offset_x, offset_y, output_directory, start_number):
    data = load_names_from_file(input_file)

    font_path = "Zetafonts - Lovelace Text Regular.otf"  # Upewnij się, że czcionka jest dostępna

    current_number = start_number

    for first_name, last_name in data:
        background_file = determine_certificate_background(first_name, female_template, male_template)
        cert_image = Image.open(background_file)
        draw = ImageDraw.Draw(cert_image)

        image_width, image_height = cert_image.size  # wielkosc templatu
        font_size = image_height / 20  # dynamiczna wielkość liter w przypadku obrazów wysokiej jakości

        text = f"{first_name} {last_name}"
        text = text.upper()
        font = ImageFont.truetype(font_path, font_size)

        # Oblicz bounding box tekstu
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Ustaw pozycję tekstu z uwzględnieniem offsetów
        position = (
            (image_width - text_width) // 2 + offset_x,
            (image_height - text_height) // 2 + offset_y
        )

        # Rysowanie imienia i nazwiska pogrubionego
        for offset in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
            draw.text((position[0] + offset[0], position[1] + offset[1]), text, fill="black", font=font)



        # Dodaj numer na dole certyfikatu
        if triggerNumering==1:
            number_text = f"NR: {current_number:06}"
            number_font_size = 18
            number_font = ImageFont.truetype(font_path, number_font_size)
            number_position = (40, image_height - 50)
            draw.text(number_position, number_text, fill="lightgray", font=number_font)
            current_number += 1

        # Utwórz nazwę pliku i zapisz certyfikat w wybranym folderze
        output_filename = os.path.join(output_directory, f"certyfikat_{first_name}_{last_name}.png")
        cert_image.save(output_filename)
        print(f"Zapisano: {output_filename}, {number_text}")

    return current_number  # Zwróć ostatnią wartość licznika

# Wybór plików za pomocą okien dialogowych
def select_files_and_generate_certificates():
    # Utwórz ukryte okno Tkinter (potrzebne do otwarcia okien dialogowych)
    root = Tk()
    root.withdraw()

    # Wybierz plik z listą imion
    print("Wybierz plik tekstowy z listą imion (np. imiona.txt)...")
    input_file = filedialog.askopenfilename(title="Wybierz plik z listą imion", filetypes=[("Text Files", "*.txt")])
    if not input_file:
        print("Nie wybrano pliku z listą imion. Zakończono.")
        return

    # Wybierz szablon dla kobiet
    print("Wybierz szablon dla kobiet...")
    female_template = filedialog.askopenfilename(title="Wybierz szablon dla kobiet", filetypes=[("Image Files", "*.png *.jpg")])
    if not female_template:
        print("Nie wybrano szablonu dla kobiet. Zakończono.")
        return

    # Wybierz szablon dla mężczyzn
    print("Wybierz szablon dla mężczyzn...")
    male_template = filedialog.askopenfilename(title="Wybierz szablon dla mężczyzn", filetypes=[("Image Files", "*.png *.jpg")])
    if not male_template:
        print("Nie wybrano szablonu dla mężczyzn. Zakończono.")
        return

    # Pytanie o początkowy numer
    start_number = simpledialog.askinteger("Początkowy Numer", "Wprowadź początkowy numer:", initialvalue=0)
    if start_number is None:
        triggerNumering=0
        return
    if start_number == 0:
        triggerNumering = 0
        return

    # Otwórz szablon kobiety, aby dynamicznie obliczyć wymiary
    example_image = Image.open(female_template)
    example_draw = ImageDraw.Draw(example_image)
    example_text = "Przykładowy Tekst"
    font = ImageFont.truetype("arial.ttf", 48)
    text_bbox = example_draw.textbbox((0, 0), example_text, font=font)
    image_width, image_height = example_image.size
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Pytanie o offset X
    offset_x = simpledialog.askinteger(
        "Offset X",
        f"Wprowadź przesunięcie w osi X (poziome przesunięcie tekstu):\n"
        f"- 0: Wyśrodkowany tekst\n"
        f"- {(image_width - text_width)/2}: Tekst przy prawej krawędzi\n"
        f"- -{(image_width - text_width)/2}: Tekst przy lewej krawędzi",
        initialvalue=0
    )
    if offset_x is None:
        offset_x = 0

    # Pytanie o offset Y
    offset_y = simpledialog.askinteger(
        "Offset Y",
        f"Wprowadź przesunięcie w osi Y (pionowe przesunięcie tekstu):\n"
        f"- 0: Wyśrodkowany tekst\n"
        f"- {(image_height - text_height)/2}: Tekst przy górnej krawędzi\n"
        f"- -{(image_height - text_height)/2}: Tekst przy dolnej krawędzi",
        initialvalue=0
    )
    if offset_y is None:
        offset_y = 0

    # Wybór folderu zapisu certyfikatów
    print("Wybierz folder, w którym chcesz zapisać certyfikaty...")
    output_directory = filedialog.askdirectory(title="Wybierz folder zapisu certyfikatów")
    if not output_directory:
        print("Nie wybrano folderu do zapisu. Zakończono.")
        return

    print("Ustawiono offset x:", offset_x)
    print("Ustawiono offset y:", offset_y)

    # Informacja o generowaniu certyfikatów
    messagebox.showinfo("Wprowadzono Dane", "Proszę kliknąć Ok aby wygenerować certyfikaty. To może chwilę zająć.")

    # Uruchom proces generowania certyfikatów
    last_number = generate_certificates(input_file, female_template, male_template, offset_x, (offset_y*-1), output_directory, start_number)

    # Informacja końcowa
    messagebox.showinfo(
        f"Certyfikaty zostały wygenerowane z przesunięciem x {offset_x}, y {offset_y}\n",
        f"Ostatni numer: {last_number-1}\n"
        f"Proszę upewnić się, że tekst na certyfikatach został prawidłowo umieszczony.\n"
        "Proszę pamiętać iż program rozpoznaje płeć na podstawie zakończenia imion na 'a', w wyniku czego niektóre imiona niepolskie (np. Mary Smith) zostaną wygenerowane z użyciem szablonu dla mężczyzn.\n"
    )

# Uruchom funkcję wyboru plików i generowania certyfikatów
if __name__ == "__main__":
    select_files_and_generate_certificates()
