#utils


def get_adjacent(pos):
	return (
		(pos[0]+1, pos[1]),
		(pos[0]-1, pos[1]),
		(pos[0], pos[1]+1),
		(pos[0], pos[1]-1)
	)

def random_from(EM, thingy, rng_name):
	l = len(thingy)
	if l < 1:
		raise IndexError("Thingy is empty")
	i = EM.randint(0, l-1, rng_name)
	return thingy[i]

