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
		deck[i] = Card(deck[i])
	print("Card data imported!")
	deck_cmc, deck_landcount = df.cmc_land_count(deck)
	hand_cmc, hand_landcount = df.cmc_land_count(hand)
	result, reason = df.mulligan(hand, deck_cmc, hand_cmc, hand_landcount)
	if result:
		print("You should mulligan this hand, it is not playable.")
		if "land" in reason:
			print("There was not an appropriate number of lands in this hand.")
		if "expensive" in reason:
			print("The average converted mana cost of this hand was too expensive.")
		if "early" in reason:
			print("There were not enough early plays in this hand.")
	if not result:
		print("Keep this hand. Good luck!")

	print("The average converted mana cost of your deck is ", deck_cmc, " compared to your hand's cmc of ", hand_cmc, ".")
	print("There are ", deck_landcount, " lands in your deck, compared to ", hand_landcount, " in your hand.")

	restart = input("Enter 'exit' to exit, and anything else to continue.")
	if restart == 'exit':
		programEnd = True
