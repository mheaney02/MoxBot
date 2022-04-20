def import_deck():
	"""
	Imports a .txt of a user-generated decklist into the program, so it can be utilized in the Card class.
	:return: the text of the decklist stripped of any extraneous characters
	"""
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


def enter_hand(valid_deck):
	"""
	Creates a seven card hand from valid cards in the deck.
	:param valid_deck: The imported deck of cards
	:return: A list of Card ob
	"""
	deck_hand = [0 for i in range(7)]
	for i in range(len(deck_hand)):
		valid_card = False
		while not valid_card:
			hand_input = input(f'What is card {i + 1} in your hand?')
			if hand_input in valid_deck:
				valid_card = True
				deck_hand[i] = hand_input
			elif hand_input not in valid_deck:
				print("That card is not in this deck! Please enter a valid card.")
	return deck_hand


def cmc_land_count(valid_deck):
	"""
	Calculated the converted mana cost "cmc" of a deck, excluding lands, which have a cmc of 0.
	:param valid_deck: A list of Card objects as imported from a text file and then Scryfall.
	:return: The average converted mana cost of the deck excluding lands, as well as the number of lands
	"""
	average_cmc = 0
	landcount = 0
	for card in valid_deck:
		if "Land" in card.type:
			landcount += 1
		elif "Land" not in card.type:
			average_cmc += card.cmc
	try:
		average_cmc = average_cmc / (len(valid_deck) - landcount)
	except ZeroDivisionError:
		average_cmc = 0
	return average_cmc, landcount


def mulligan(hand, hand_cmc, deck_cmc, hand_landcount):
	earlyplays = 0
	mull_hand = False
