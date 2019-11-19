"""  
Lets imagine we creating the game. Game world is a set of cells. We need  
to create some quantity of cells with grass, stone and water and place  
them in the world. We've decided to check if the cell already taken using  
`in` operator, type of object doesn't matter, only coordinates x, y  
matter. Also we should check whether cell already taken without creation  
of object - simply with tuple of x and y coordinates.  
Please implement classes Grass, Stone, Water to pass all assertions.  
"""  
` 
if name == '__main__':
    world = {Grass(1, 2), Stone(3, 4), Water(5, 3), Stone(2, 2)}

    assert Stone(1, 2) in world
    assert Grass(3, 5) not in world
    assert (3, 4) in world
    assert (4, 3) not in world`
