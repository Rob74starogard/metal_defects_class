______________________________
Projekt zawiera próbę klasyfikacji uszkodzeń powierzchni metalu na podstawie rzeczywistych zdjęć wykonanych podczas oceny przydatności komponentu. 
Jako zbiór teningowo - walidacyjny wykorzystano dataset Kaggla - https://www.kaggle.com/datasets/alex000kim/gc10det .
W związku z niezadawalającymi wynikami otrzymanymi na bazie podejścia bazującego w 100% na CNN zaproponowano hybrydę zlożoną z modelu VGG16 do selekcji cech a następnie LightGBM do klasyfikacji. Podjęto również próbę uzyskania informacji o wielkości wad na podstawie obróbki zdjęcia biblioteką Scikit - image. https://scikit-image.org/.
W razie pytań lub sugestii zapraszam  - rkucharski74@gmail.com
