import os
from deck import Deck
from scrython import Named as cardName
import re

programEnd = False


def import_deck():
	deckImported = False
	while not deckImported:
		deckname = input("What is the name of the file?")
		try:
			with open(deckname, 'r') as f:
				decktext = f.readlines()
			deckImported = True
		except FileNotFoundError:
			print("That is not a valid deck!  Try again.")
		cleantext = []
	for entry in decktext:
		cleantext.append(str(entry.strip("\n")))
	print("Deck text imported!")
	return cleantext


while not programEnd:
	print("Welcome to MoxBot!  Make sure your decklist is in the Moxbot folder and each card is a separate entry.")
	print("There should be one card per line, and if it is a deck with a commander, it should not be included.")
	deck = import_deck()
	print("Importing card data from Scryfall...")
	#deck = Deck(deck)
	'''print(deck.hand)
	print(deck.card_cmcs)
	print(deck.average_cmc)'''
