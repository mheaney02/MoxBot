from card import Card
import deckfunctions as df

programEnd = False


while not programEnd:
	print("Welcome to MoxBot!  Make sure your decklist is in the MoxBot folder and each card is on a separate line.")
	print("There should be one card per line, and if it is a deck with a commander, it should not be included.")
	print("For example, if a deck has 3 of one card, each one of those cards should be a separate entry.")
	deck = df.import_deck()
	hand = df.enter_hand(deck)
	print("Importing card data from Scryfall...")
	for i in range(len(deck)):
		deck[i] = Card(deck[i])
	print("Card data imported!")
	deck_cmc, deck_landcount = df.cmc_land_count(deck)
	hand_cmc, hand_landcount = df.cmc_land_count(hand)
	result, reason = df.mulligan(hand, deck_cmc, hand_cmc, hand_landcount)
	df.define_outcome(result, reason)
	print("The average converted mana cost of your deck is", deck_cmc, "compared to your hand's CMC of", hand_cmc, ".")
	print("There are", deck_landcount, "lands in your deck, compared to", hand_landcount, "in your hand.")

	restart = input("Enter 'exit' to exit, and anything else to continue.")
	if restart == 'exit':
		programEnd = True
