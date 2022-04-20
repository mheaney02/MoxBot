from card import Card
import deckfunctions as df

programEnd = False


while not programEnd:
	print("Welcome to MoxBot!  Make sure your decklist is in the MoxBot folder and each card is on a separate line.")
	print("There should be one card per line, and if it is a deck with a commander, it should not be included.")
	deck = df.import_deck()
	hand = df.enter_hand(deck)
	print("Importing card data from Scryfall...")
	for i in range(len(deck)):
		deck[i] = Card(deck[i])  # Imports card data from Scryfall using the Scrython module
	for i in range(len(hand)):
		hand[i] = Card(hand[i])
	print("Card data imported!")
	deck_cmc, deck_landcount = df.cmc_land_count(deck)
	hand_cmc, hand_landcount = df.cmc_land_count(hand)
	print(deck_cmc, deck_landcount)
	print(hand_cmc, hand_landcount)

