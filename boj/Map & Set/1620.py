M, N = map(int, input().split())
pokemonListOne = []
pokemonListTwo = []

for i in range(1, M + 1):
    name = input()
    pokemonListOne.append([i, name])
    pokemonListTwo.append([name, i])

pokemonMapOne = dict(pokemonListOne)
pokemonMapTwo = dict(pokemonListTwo)

for i in range(N):
    target = input()
    try:
        if type(int(target)) == type(1):
            print(pokemonMapOne[int(target)])
    except:
        print(pokemonMapTwo[target])
