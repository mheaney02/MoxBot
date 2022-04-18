from scrython import Named as cardName


class Card:
	def __init__(self, name):
		card = cardName(fuzzy=name)  # Imports card data from Scryfall using Scrython
		self.name = card.name()
		self.cmc = card.cmc()  # Converted mana cost, or how "expensive" the card is in-game
		self.type = card.type_line()
		return
