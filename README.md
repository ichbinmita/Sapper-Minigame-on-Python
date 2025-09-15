# Sapper+ Game

A hybrid puzzle game that combines elements of Minesweeper (Sapper) with navigation challenges, built using Pygame.

## Game Description

Sapper+ is an innovative twist on the classic Minesweeper game. Players must first reveal safe paths by strategically clicking on cells to avoid hidden mines, then navigate their character through the revealed safe areas to reach the target destination.

### Game Features

- **Dual Gameplay Modes**:
  - **Sapper Mode**: Reveal cells to discover safe paths and avoid mines
  - **Walking Mode**: Navigate your character through revealed safe cells

- **Strategic Gameplay**: Plan your path carefully as you can only move through cells you've previously revealed

- **Visual Feedback**: Color-coded cells indicate mine locations, safe paths, and adjacent mine counts

- **Win Condition**: Successfully navigate your character from the starting position to the target

## How to Play

1. **Sapper Mode (Default)**:
   - Click on cells to reveal what's underneath
   - Green cells are unrevealed, gray cells are safe, red cells contain mines
   - Numbers indicate how many mines are adjacent to that cell
   - Press SPACE to switch to Walking Mode

2. **Walking Mode**:
   - Use arrow keys to move your character (white square)
   - You can only move on revealed safe cells (gray)
   - Press SPACE to return to Sapper Mode
   - Reach the red target cell to win the game

## Technical Details

This implementation uses:
- Pygame for rendering and event handling
- 2D grid system for game state management
- Random mine placement with safe zones around start and end points
- Adjacency counting algorithm to calculate mine proximity

### Code Structure

- **Grid Setup**: 15×10 grid with 20 randomly placed mines
- **Game States**: Toggles between "sapper" (revealing cells) and "walking" (navigation) modes
- **Rendering**: Visual distinction between revealed/unrevealed cells, mines, and safe paths
- **Win/Lose Conditions**: Game ends when player hits a mine or reaches the target

## Requirements

- Python 3.x
- Pygame library

Install dependencies with:
```
pip install pygame
```

## Future Enhancements

Potential improvements could include:
- Multiple difficulty levels
- Timer and scoring system
- Sound effects
- Level editor
- Animations and visual effects

Enjoy playing Sapper+!
