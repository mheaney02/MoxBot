from card import Card


def import_deck():
	"""
	Imports a .txt of a user-generated decklist into the program, so it can be utilized in the Card class.
	:return: the text of the decklist stripped of any extraneous characters
	"""
	deckImported = False
	while not deckImported:
		deckname = input("What is the name of the file? ")
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
	:return: A list of Card objects for each card in the hand,
	"""
	deck_hand = [0 for i in range(7)]
	for i in range(len(deck_hand)):
		valid_card = False
		while not valid_card:
			hand_input = input(f'What is card {i + 1} in your hand? ')
			hand_input = Card(hand_input)
			if hand_input.name in valid_deck:
				valid_card = True
				deck_hand[i] = hand_input  # Imports card data from Scryfall using the Scrython module
			elif hand_input not in valid_deck:
				print("That card is not in this deck! Please enter a valid card. ")
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


def mulligan(hand, deck_cmc, hand_cmc, hand_landcount):
	"""
	Determines whether the entered hand is good enough to be kept.
	:param hand: The user-entered hand of seven valid cards.
	:param deck_cmc: The total converted mana cost of the deck.
	:param hand_cmc: The total converted mana cost of the hand.
	:param hand_landcount: The number of lands present in the hand.
	:return: A boolean which indicates whether the hand should be kept, as well as a reason if it cannot.
	"""
	earlyplays = 0  # the number of cards that can be played in turns 1-3, excluding lands
	mull_hand = False
	reason = "none"
	lands_entered = False
	while not lands_entered:
		try:
			minlands = int(input("What is the minimum number of lands that can be in your opening hand? "))
			maxlands = int(input("What is the maximum number of lands? "))
			lands_entered = True
		except ValueError:
			print("That is not a valid input!  Please try again. ")
	for card in hand:
		if card.cmc <= 3:
			earlyplays += 1
	if earlyplays < 3:
		mull_hand = True
		reason = reason + "early"

	if not minlands < hand_landcount < maxlands:  # Checks the number of lands in the deck to see if it is playable
		mull_hand = True
		reason = reason + "land"

	if hand_cmc >= deck_cmc:  # If the cards in hand are more expensive than the average card, mulligan
		mull_hand = True
		reason = reason + "expensive"

	return mull_hand, reason


def define_outcome(result, reason):
	"""
	Prints the outcome of the mulligan algorithm, as well as the reason.
	:param result: The boolean result of the mulligan algorithm.
	:param reason: The list of reasons given by the mulligan algorithm.
	:return:
	"""
	if result:
		print("You should mulligan this hand, it is not playable.")
		if "land" in reason:
			print("There was not an appropriate number of lands in this hand.")
		if "expensive" in reason:
			print("The average converted mana cost of this hand was too high.")
		if "early" in reason:
			print("There were not enough early plays in this hand.")
	if not result:
		print("Keep this hand. Good luck!")
	return
