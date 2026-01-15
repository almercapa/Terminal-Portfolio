DGTT: Terminal Battle Prototype

A robust, terminal-based combat engine and quiz application built with Python. This project serves as the logic prototype for a JJK-themed study SaaS, focusing on efficient data handling and interactive user experience.

Core Features

    Dynamic Damage Scaling: Implements a damage_map dictionary to assign damage based on question difficulty, ensuring modular and scalable logic.

    Visual Health Systems: Features real-time, color-coded HP bars rendered using integer division for consistent UI spacing.

    Robust Input Protection: Utilizes try-except blocks to catch ValueError exceptions, preventing application crashes from invalid user input.

    RNG Combat Mechanics: Includes a "Black Flash" critical hit system using Python's random module for unpredictable gameplay.

Technical Implementation

    Modularity: Game UI is abstracted into reusable functions (e.g., printHealthBar) to follow DRY (Don't Repeat Yourself) principles.

    State Management: Manages a complex loop that tracks player/enemy health and question indexing across a dynamic question_bank.

    Dependency Management: Integrates the colorist library for ANSI escape-sequence-based terminal styling.