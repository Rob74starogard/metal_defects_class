# metal_defects_class
last project for SDA
Projekt zawiera próbę klasyfikacji uszkodzeń powierzchni metalu na podstawie rzczywistych zdjęć wykonanych podczas oceny przydatności komponentu. 
Jako zbiór teningowo walidacyjny wykorzystano zbiór Kaggla - https://www.kaggle.com/datasets/alex000kim/gc10det
W związku z niezadawalającym podejściem bazującym w 100% na podejściu opartym na CNN zaproponowano hybrydę zlożoną z modelu VGG16 do selekcji cech a następnie LightGBM do klasyfikacji. Podjęto również próbę uzyskania informacji o wielkości wad na podstawie obróbki zdjęcia biblioteką Scikit - image. https://scikit-image.org/.
W razie pytań lub sugestii zapraszam  - rkucharski74@gmail.com
