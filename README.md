# AutoCertyfikat

UWAGA: PLIK EXE JEST NIEAKUTALNY. (działa ale .py jest lepszy)

Program ułatwiający tworzenie wielu spersonalizowanych certyfikatów w python
Pobierz cały folder "Download this to use the program" i uruchom plik .exe aby natychmiast użyć programu.

# Opisz szczegółowy:

Program służy do łątwiejszego wypełniania dużej ilości certyfikatów (np. dyplomów ukończenia kursów. 
Pozwala on na oszczędzenie czasu - zamiast wypełniać np 2000 nazwisk ręcznie, program może zrobić to dla nas
W program włożyć należy kolejno:

--plik tekstowy z listą podpisów (W formacie imię spacja nazwisko)

--szablon certyfikatu w wersji i "żeńskiej" ("Pani") i "męskiej" ("Pan") ("pusty" certyfikat z miejscem na wpisanie imienia i nazwiska)

--numer od którego zacząć należy numerację certyfikatów (każdy certyfikat jest numerowany małym szarym numerem w lewym dolnym rogu)

--przesunięcie podpisu na certyfikacie w osiach X (góra/dół) i Y (prawo/lewo). W przypadku wpisania X=0 Y=0 podpis będzie umieszczony idealnie na środku certyfikatu. (w szkoleniu "Od Inżyniera do Negocjatora" podano parametry Y=0 X=75, powodując przesunięcie podpisu trochę w górę). Program podaje przy tym zakres sensownych do wpisania wartości, takich aby podpis nie wychodził poza certyfikat (np. Jeśli certyfikat ma wysokość 1000 pikseli, program poda wartości około -450 i 450, aby dać informację jaką wartość trzeba wpisać aby przesunąć podpis np. o 1/6 wysokości obrazu - wie wówczas, iż będzie to około 160)

Następnie wybrać należy folder, w którym zapisane będą certyfikaty, a następnie potwierdzić. Po krótkiej chwili otrzymamy Informację z numerem ostatniego utworzonego certyfikatu, oraz przestrogą informującą o wymogu uważności przy uważaniu programu do automatyzacji wystawiania certyfikatów osobom z imionami zagranicznymi, jako że program dopasowuje płeć na podstawie zasady mówiącej, iż wszystkie żeńskie imiona Polskie  kończą się na literę "a".

Pamiętać przy tym należy, iż programu należy używać wraz z dostarczonym fontem "Zetafonts_-Lovelace_Text_Regular.otf" - jest to font wybrany przez KNCPI i bez niego program nie działa. Font należy umieścić w tym samym miejscu gdzie program.

Uwaga: pliki .exe mogą być nieaktualne w porównaniu do kodu.

mirrory:

https://www.mediafire.com/file/opx6kxtx2ickdzt/AutoCertyfikaty_KNCPI.exe/file     -program
https://www.mediafire.com/file/yx6vzvaby5iq8m4/Zetafonts-_Lovelace_Text_Regular.otf/file     -font

