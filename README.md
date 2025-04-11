# Points

A text-based adventure game where the player delves deep into a dungeon to defeat enemies and overcome challenges. The game features a simple level-up system, enemy and boss battles, and allows you to quit or restart at any time.

## Installation

### Requirements

- Python 3.x

### Installation and Running

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Addiv420/Points.git
    cd Points
    ```

2. **Start the game**:  
    After cloning the repository, simply run the script:
    ```bash
    python points.py
    ```

## Gameplay

The game is a text-based dungeon crawler in which the player encounters enemies that must be defeated to progress deeper into the dungeon and gain experience.

**Goal:**  
- Go as deep as possible into the dungeon.  
- Defeat enemies and bosses to gain experience.  
- Level up and improve your abilities.  
- Avoid die. (Pretty self-explanatory)

## Controls

- **[W]**: Move forward into the dungeon.  
- **[S]**: Move back.  
- **[Quit]**: Exit the game.  
- **[Y]**: Restart the game after dying.  
- **[N]**: Quit the game after dying.  
- **Attack**: Press the correct attack key from the options (e.g., [Y], [X], [C], etc.).  
- **Dodge**: Use one of the four possible dodge keys ([Q], [E], [A], [D]).

## Game Flow

1. **Dungeon Depth and Enemies**:  
   You start at floor 0 of the dungeon. Each level could feature one or more random enemies and/or one random boss encounter.

2. **Fighting Enemies**:  
   When an enemy appears, press the correct attack key to defeat them. If you fail, you die and must choose whether to try again.

3. **Boss Fights**:  
   At the end of a dungeon depth, you could face a boss. You must press the right attack keys and dodge correctly to survive.

4. **Level-Up**:  
   Collect experience points to level up and gain more strength and reach deeper floors.

5. **Death and Restart**:  
   If you die, you can restart or quit the game. There is also a cheat code, but that’s a secret. :3

## Colors

The game uses colored text for feedback:

- **Green**: Indicates positive events such as level-ups or successful attacks.  
- **Red**: Indicates failures or enemy actions.  
- **Yellow**: Used for tips and status messages.

## Features

- **Points**: Your dungeon progress is measured in points.  
- **Level**: Your character levels up and grows stronger.  
- **Experience**: Earn EXP by defeating enemies and clearing challenges.  
- **Boss Battles**: Face a boss at the end of each dungeon tier to earn more points and EXP.  
- **Keyboard Input**: Use keys to move, attack, and dodge throughout the game.