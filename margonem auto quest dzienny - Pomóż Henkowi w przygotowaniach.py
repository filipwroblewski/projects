# misja:  quest na denary margonem - Pomóż Henkowi w przygotowaniach

import time
import pyautogui

def od_Henk_Hornigold_do_Tawerna():
    #droga do Tawarna Pod Szemrzącą beczułką
    pyautogui.click(897, 171, duration=0.5)
    pyautogui.click(1124, 177, duration=4)
    pyautogui.click(815, 168, duration=5)
    pyautogui.click(1624, 548, duration=4)
    pyautogui.click(1540, 596, duration=12)
    pyautogui.click(1530, 550, duration=14) # wejscie do budynku

def z_Tawerny_do_Henk_Hornigold():
    #droga z karczmy do Henk Hornigold
    pyautogui.click(20, 229, duration=6)
    pyautogui.click(634, 961, duration=19)
    pyautogui.click(804, 966, duration=5)
    pyautogui.click(664, 964, duration=6)
    pyautogui.click(712, 736, duration=5) # podejscie do henka
    pyautogui.click(867, 555, duration=5) # rozpoczecie dialogu z Henk Hinnigold


time.sleep(5)

pyautogui.click(868, 559, duration=0.5) #rozpoczecie rozmowy
pyautogui.click(839, 924, duration=0.5) #4th dialog
pyautogui.click(871, 751, duration=0.5) # 1st dialog
pyautogui.click(864, 717, duration=0.5) # 1st dialog
pyautogui.click(860, 774, duration=0.5) # 1st dialog
pyautogui.click(867, 801, duration=0.5) # 1st dialog
pyautogui.click(880, 743, duration=0.5) # zakonczenie rozmowy => rozpoczecie questa

od_Henk_Hornigold_do_Tawerna()

pyautogui.click(423, 602, duration=7) # podejscie do pirata (Klaban Grantis)
pyautogui.click(396, 571, duration=6) # rozpoczecie dialogu
pyautogui.click(655, 844, duration=0.5) # 3rd dialog
pyautogui.click(875, 785, duration=0.5) # 1st dialog
pyautogui.click(875, 765, duration=0.5) # 1st dialog
pyautogui.click(875, 765, duration=0.5) # 1st dialog
pyautogui.click(875, 770, duration=0.5) # 1st dialog => otrzymanie szbli


pyautogui.click(660, 926, duration=0.5) # wyjscie z budynku
pyautogui.click(1652, 565, duration=6) # do portu tuzmer
pyautogui.click(303, 961, duration=4)


pyautogui.click(1197, 646, duration=7) # do kuźni Kendala
pyautogui.click(859, 574, duration=10) # do Kendala

pyautogui.click(882, 543, duration=3) # rozpoczecie dialogu
pyautogui.click(882, 859, duration=0.5) # 3rd dialog
pyautogui.click(882, 741, duration=0.5) # 3rd dialog => Kendal zabiera szble


pyautogui.click(663, 534, duration=10) # zeby nie bylo afk zamiast 'time.sleep(3*60)'
pyautogui.click(851, 534, duration=10) # zeby nie bylo afk zamiast 'time.sleep(3*60)'
pyautogui.click(663, 534, duration=10) # zeby nie bylo afk zamiast 'time.sleep(3*60)'
pyautogui.click(851, 534, duration=10) # zeby nie bylo afk zamiast 'time.sleep(3*60)'
pyautogui.click(663, 534, duration=10) # zeby nie bylo afk zamiast 'time.sleep(3*60)'
pyautogui.click(851, 534, duration=10) # zeby nie bylo afk zamiast 'time.sleep(3*60)'
pyautogui.click(882, 543, duration=2) # ponowne rozpoczecie dialogu
pyautogui.click(882, 859, duration=0.5) # 3rd dialog => naostrzona szbla, utrata 1000 sztuk zlota
pyautogui.click(882, 725, duration=0.5) # zakonczenie dialogu

pyautogui.click(789, 711, duration=0.5) # wyjscie z budynku

pyautogui.click(13, 543, duration=4)
pyautogui.click(172, 213, duration=7)
pyautogui.click(14, 468, duration=10)
pyautogui.click(1531, 596, duration=4) # wejscie do budynku
pyautogui.click(423, 602, duration=8) # podejscie do pirata
pyautogui.click(396, 571, duration=6) # rozpoczecie dialogu
pyautogui.click(655, 844, duration=0.5) # 3rd dialog
pyautogui.click(875, 726, duration=0.5) # zakonczenie rozmowy (Klaban Grantis done)

pyautogui.click(1048, 521, duration=0.5) # podejscie do Aslan Szpon
pyautogui.click(1076, 590, duration=8) # rozpoczecie dialogu
pyautogui.click(1076, 858, duration=0.5) # 4th dialog
pyautogui.click(1076, 729, duration=0.5) # 1st dialog
pyautogui.click(1076, 764, duration=0.5) # 1st dialog
pyautogui.click(1076, 764, duration=0.5) # 1st dialog
pyautogui.click(1076, 724, duration=0.5) # 1st dialog
pyautogui.click(1076, 724, duration=0.5) # zakonczenie dialogu => idziemy po wino
pyautogui.click(660, 960, duration=0.5) # wyjscie z budynku
pyautogui.click(1652, 565, duration=13) # do portu tuzmer
pyautogui.click(1488, 176, duration=7)
pyautogui.click(866, 150, duration=14) # do tuzmer

pyautogui.click(868, 186, duration=7)
pyautogui.click(965, 406, duration=7)

pyautogui.click(832, 521, duration=3) # zakon astralny dialog

pyautogui.click(832, 745, duration=1) # 1st dialog
pyautogui.click(832, 765, duration=0.5) # tp do astralnego koncentratora (Trupia Przełęcz) => stracono5k
pyautogui.click(104, 520, duration=3) # dialog z koncentratorem
pyautogui.click(690, 908, duration=2) # 6th dialog => tp do nithal => stracono 5k
pyautogui.click(420, 960, duration=3)

pyautogui.click(840, 900, duration=7) # przejscie do winnicy melfkasti
pyautogui.click(980, 940, duration=5)
pyautogui.click(1000, 940, duration=5)
pyautogui.click(1000, 940, duration=5)
pyautogui.click(17, 760, duration=6)
pyautogui.click(17, 271, duration=13)
pyautogui.click(517, 563, duration=9) # podejscie do Mafla

pyautogui.click(492, 527, duration=3) # rozpoczecie rozmowy z Meflem
pyautogui.click(640, 870, duration=0.5) # 3rd dialog
pyautogui.click(640, 720, duration=1) # 1st dialog => otrzymujesz: bardzo stare wino + stracono 10k
pyautogui.click(1080, 720, duration=1)

pyautogui.click(1080, 720, duration=1) # zakonczenie rozmowy
pyautogui.click(1358, 966, duration=1)
pyautogui.click(1646, 576, duration=11)
pyautogui.click(1158, 172, duration=6)
pyautogui.click(1044, 174, duration=7)
pyautogui.click(1044, 174, duration=5)
pyautogui.click(1051, 310, duration=4) # wejscie do nithal

pyautogui.click(1216, 241, duration=4) # podejscie do tp
pyautogui.click(865, 549, duration=7) # rozpoczecie dialogu z tp
pyautogui.click(865, 770, duration=0.5) # 1st dialog
pyautogui.click(865, 919, duration=0.5) # 7 dialog => tp do Trupia przelecz => stracono 5k

pyautogui.click(104, 520, duration=3) # dialog z koncentratorem
pyautogui.click(666, 937, duration=3) # tp do Tuzmer => stracono 5k
pyautogui.click(651, 958, duration=3)
pyautogui.click(823, 961, duration=3)
pyautogui.click(833, 961, duration=4) # przejscie do portu tuzmer

pyautogui.click(14, 787, duration=5)
pyautogui.click(14, 641, duration=12) # przejscie na latarniane wybrzeże
pyautogui.click(1531, 596, duration=8) # wejscie do budynku
pyautogui.click(1051, 524, duration=5) # podejscie do Aslana
pyautogui.click(1074, 593, duration=10) # rozpoczecie dialogu
pyautogui.click(1074, 846, duration=0.5) # 4th dialog => oddanie wina
pyautogui.click(1074, 762, duration=0.5) # 1st zakonczenie rozmowy => Aslan done


pyautogui.click(781, 678, duration=1) # podejscie do Miralasa
pyautogui.click(781, 627, duration=8) # rozpoczecie dialogu

pyautogui.click(781, 828, duration=0.5) # 4th dialog
pyautogui.click(781, 741, duration=0.5) # 1st dialog
pyautogui.click(781, 741, duration=0.5) # 1st dialog
pyautogui.click(781, 720, duration=1) # 1st dialog => zakonczenie rozmowy
pyautogui.click(656, 928, duration=2) # wyjscie z budynku

z_Tawerny_do_Henk_Hornigold()

pyautogui.click(744, 729, duration=0.5) # 1st dialog
pyautogui.click(744, 729, duration=0.5) # 1st dialog => zakonczenie rozmowy

od_Henk_Hornigold_do_Tawerna()

pyautogui.click(782, 637, duration=5)
pyautogui.click(656, 928, duration=0.5) # wyjscie z budynku

pyautogui.click(1654, 569, duration=3) # do portu tuzmer

pyautogui.click(1459, 694, duration=3) # podejscie do Marynarz Typolis
pyautogui.click(866, 527, duration=16) # rozpoczecie dialogu z Marynarz Typolis
pyautogui.click(866, 883, duration=0.5) # 3rd dialog
pyautogui.click(866, 751, duration=0.5) # 1st dialog => stracono 1k
pyautogui.click(866, 726, duration=3)

pyautogui.click(866, 726, duration=1) # 1st dialog => zakonczenie rozmowy
pyautogui.click(12, 383, duration=3)

pyautogui.click(14, 605, duration=12) # przejscie na latarniane wybrzeże

pyautogui.click(1530, 590, duration=9) # wejscie do budynku

# juz chyba ok
pyautogui.click(789, 668, duration=4) # podejscie do Miralas
pyautogui.click(783, 625, duration=4) # rozpoczecie dialogu z Miralas
pyautogui.click(783, 843, duration=0.5) # 4th dialog
pyautogui.click(783, 717, duration=0.5)
pyautogui.click(783, 717, duration=0.5) # 1st dialog => zakonczenie rozmowy

pyautogui.click(726, 506, duration=1) # podejscie do Hak Odeward
pyautogui.click(721, 523, duration=3) # rozpoczecie dialogu z Hak Odeward
pyautogui.click(721, 822, duration=0.5) # 4th dialog
pyautogui.click(721, 729, duration=0.5) # 4th dialog
pyautogui.click(721, 729, duration=0.5) # 1st dialog
pyautogui.click(721, 729, duration=0.5) # 1st dialog => zakonczenie rozmowy
pyautogui.click(686, 801, duration=0.5)
pyautogui.click(659, 926, duration=3) # wyjscie z budynku

z_Tawerny_do_Henk_Hornigold()

pyautogui.click(744, 729, duration=0.5) # 1st dialog
pyautogui.click(744, 766, duration=0.5) # 1st dialog
pyautogui.click(744, 745, duration=0.5) # 1st dialog => zakonczenie rozmowy

od_Henk_Hornigold_do_Tawerna()
pyautogui.click(782, 637, duration=5)
pyautogui.click(656, 928, duration=0.5) # wyjscie z budynku



pyautogui.click(1654, 569, duration=4) # do portu tuzmer
pyautogui.click(1488, 176, duration=4)

pyautogui.click(866, 148, duration=14) # do tuzmer
pyautogui.click(868, 186, duration=6)
pyautogui.click(1094, 180, duration=6)
pyautogui.click(1317, 168, duration=8)
pyautogui.click(855, 423, duration=6)

pyautogui.click(851, 451, duration=2) # rozpoczecie dialogu z Przemytnik Polifiks


pyautogui.click(863, 854, duration=0.5) # 4th dialog
pyautogui.click(863, 718, duration=0.5) # 1st dialog
pyautogui.click(863, 718, duration=0.5) # 1st dialog
pyautogui.click(863, 718, duration=0.5) # 1st dialog => otrzymano: kufer z bronia, stracono 50k
pyautogui.click(863, 718, duration=0.5) # 1st dialog => zakonczenie rozmowy
pyautogui.click(357, 960, duration=0.5)
pyautogui.click(739, 956, duration=5)
pyautogui.click(707, 954, duration=5)
pyautogui.click(817, 961, duration=5)
pyautogui.click(842, 955, duration=3) # przejscie do portu tuzmer
pyautogui.click(14, 787, duration=5)
pyautogui.click(14, 641, duration=12) # przejscie na latarniane wybrzeże
pyautogui.click(1532, 601, duration=8) # wejscie do tawerny
pyautogui.click(658, 764, duration=3)
pyautogui.click(659, 945, duration=0.5) # wyjscie z tawerny

z_Tawerny_do_Henk_Hornigold()

pyautogui.click(866, 559, duration=2) # rozpoczecie rozmowy
pyautogui.click(866, 720, duration=0.5) # 1st dialog
pyautogui.click(866, 750, duration=0.5) # 1st dialog => zakonczenie rozmowy

od_Henk_Hornigold_do_Tawerna()

pyautogui.click(662, 173, duration=4)
pyautogui.click(717, 370, duration=6)

pyautogui.click(717, 370, duration=2) # rozpoczecie dialogu z Barman Wichran
pyautogui.click(717, 718, duration=0.5) # 1st dialog
pyautogui.click(717, 718, duration=0.5) # 1st dialog
pyautogui.click(717, 718, duration=0.5) # 1st dialog
pyautogui.click(717, 718, duration=0.5) # 1st dialog => stracono 30k, otrzymano beczka rumu
pyautogui.click(717, 718, duration=0.5) # 1st dialog => zakonczenie rozmowy
pyautogui.click(560, 962, duration=0.5)
pyautogui.click(657, 926, duration=7)
z_Tawerny_do_Henk_Hornigold()
pyautogui.click(866, 559, duration=4) # rozpoczecie dialogu
pyautogui.click(777, 720, duration=0.5) # rozpoczecie dialogu => koniec questa => otrzymano 300k + 300k exp + 1 denar
pyautogui.click(794, 793, duration=0.5) # 1st dialog => zakonczenie rozmowy
print('quest done: otrzymano 300k exp, 300k złota, 1 denar')





