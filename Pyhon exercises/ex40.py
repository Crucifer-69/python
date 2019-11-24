class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_birthday = Song(["Happy bitrhday to you","I don't want to get sued","So I'll stop right there"])

bull_in_parade = Song(["They rally around the family","with pockets full of shell"])

happy_birthday_again = "\nHappy bitrhday to you","I don't want to get sued","So I'll stop right there AGAIN\n"

happy_birthday.sing_me_a_song()

bull_in_parade.sing_me_a_song()

Song(happy_birthday_again).sing_me_a_song()