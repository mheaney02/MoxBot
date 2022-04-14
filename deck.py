from scrython import Named as cardName


class Card:

class Deck:
	def __init__(self, decktext):
		hand = []
		print("Importing card data from Scryfall...")
		for card in decktext:
			card = cardName(fuzzy=card)
			hand += [card.name()]
		self.hand = hand
		card_cmcs = []
		self.card_cmcs = card_cmcs
		#self.average_cmc = sum(card for card in self.card_cmcs) / len(hand)
		return

	def get_cmcs(self, hand):
		card_cmcs = []
		for card in hand:
			card = cardName(fuzzy=card)
			card_cmcs += [card.cmc()]

