import random
import numpy as np
from enum import Enum
from math import floor
from rich import print as rprint

class HEX(Enum):
    '''Enum for hex iconography'''
    EASY = 'E'
    MEDIUM = 'M'
    HARD = 'H'
    DEADLY = 'D'
    SAFE = 'S'

def main():
    '''Calculates and outputs grid information'''
    # grid is 13 x 11
    gridLength = 11
    gridHeight = 13
    grid = [[0 for i in range(gridLength)] for j in range(gridHeight)]
    numHexes = len(grid) * len(grid[0])
    rprint(f"[bold yellow]Number of hexes to fill: {numHexes}")
    
    # From the DMG:
    # Assuming typical Adventuring Conditions and average luck, most Adventuring parties can handle about six to eight medium or hard encounters in a day.
    # If the adventure has more easy encounters, the Adventurers can get through more. If it has more deadly encounters, they can handle fewer.
    easyRatio = .1
    mediumRatio = .2
    hardRatio = .4
    deadlyRatio = .2
    safeRatio = .1

    easyEncouters = floor(143*easyRatio)
    mediumEncouters = floor(143*mediumRatio)
    hardEncouters = floor(143*hardRatio)
    deadlyEncouters = floor(143*deadlyRatio)
    safeEncouters = floor(143*safeRatio)
    # pad with safe zones
    safeEncouters += (numHexes - easyEncouters - mediumEncouters - hardEncouters - deadlyEncouters - safeEncouters)

    rprint(f"That means we have: \
        \n[yellow bold]{easyEncouters} easy[/bold yellow] encounters, \
        \n[yellow bold]{mediumEncouters} medium[/bold yellow] encounters, \
        \n[yellow bold]{hardEncouters} hard[/bold yellow] encounters, \
        \n[yellow bold]{deadlyEncouters} deadly[/bold yellow] encounters, \
        \nand [yellow bold]{safeEncouters} safe[/bold yellow] encounters.")

    # fill an array
    se = [HEX.SAFE.name for i in range(safeEncouters)]
    ee = [HEX.EASY.name for i in range(easyEncouters)]
    me = [HEX.MEDIUM.name for i in range(mediumEncouters)]
    he = [HEX.HARD.name for i in range(hardEncouters)]
    de = [HEX.DEADLY.name for i in range(deadlyEncouters)]

    encounters = [*se, *ee, *me, *he, *de]
    random.shuffle(encounters)

    encounterGrid = np.array(encounters)

    rprint(f'Our encounter array!:\n [yellow]{encounterGrid.reshape(gridLength, gridHeight)}[/yellow]')
    

if __name__ == '__main__':
    # todo get args from cmd line
    main()