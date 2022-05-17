import requests
import colorama
from colorama import Back, Fore, Style
from bs4 import BeautifulSoup

#   Loading the webpage content
runeGoldberg_page = requests.get("https://runescape.wiki/w/Rune_Goldberg_Machine")              # CONFIRMED
travelingMerchant_page = requests.get("https://runescape.wiki/w/Travelling_Merchant%27s_Shop")  # CONFIRMED
frostDragonBones_page = requests.get("https://runescape.wiki/w/Frost_dragon_bones")             # CONFIRMED

#   Parsing page content
runeGoldberg_wiki = BeautifulSoup(runeGoldberg_page.content, "html.parser")
wiki_table = runeGoldberg_wiki.find_all('table', class_="wikitable")


#   Displaying the title in color
colorama.init(autoreset=True)
print(Fore.RED + "~~~~~ Runescape 3 Information ~~~~~")


#   Getting Today's date
date = wiki_table[0].td.next
print("\t   " + Fore.LIGHTGREEN_EX + date + "\n")

#   RuneGoldberg Machine & Finding 1st Rune Slot
slot1 = wiki_table[0].a.next.next.next
slot1_rune = slot1.contents[0]
print("Slot 1: " + slot1_rune)

#   RuneGoldberg Machine & Finding 2nd Rune Slot (1st Option)
slot2_one = wiki_table[0].a.next.next.next.next.next.next.next.next.next.next.next.next.next.next
slot2_rune1 = slot2_one.contents[0]
print("Slot 2 (Option 1): " + slot2_rune1)

#   RuneGoldberg Machine & Finding 2nd Rune Slot (2nd Option)
slot2_two = wiki_table[0].tr.findNext('tr').findNext('tr').findNext('tr').next.next.next.next.next
slot2_rune2 = slot2_two.contents[0]
print("Slot 2 (Option 2): " + slot2_rune2)

#   RuneGoldberg Machine & Finding 2nd Rune Slot (2nd Option)
slot2_three = wiki_table[0].tr.findNext('tr').findNext('tr').findNext('tr').findNext('tr').next.next.next.next.next
slot2_rune3 = slot2_three.contents[0]
print("Slot 2 (Option 3): " + slot2_rune3)


#TODO: Get prices of big ticket items
#TODO: Show the change in prices from the last time it was ran (save to a text file)


input('Press ENTER to exit')