**# Problem Statement \& Project Scope**



**## Problem Statement**

**Traditional terminal-based utility games often lack structured modularity, explicit state management, and strict terminal cross-platform compatibility. Simple games like "Snake" are frequently written as monolithic single-file scripts, making them difficult to maintain, test, and scale. This project addresses the challenge of building a fully modular, command-line executable Snake game written in Python that enforces clear architecture, robust collision mechanics, automated score tracking, and continuous game-loop execution without external GUI dependencies.**



**## Target Users**

**\* \*\*Students and Academics:\*\* Individuals evaluating terminal-based game engine architecture, object-oriented concepts, and clean code practices.**

**\* \*\*Command-Line Enthusiasts:\*\* Users seeking lightweight, zero-dependency, terminal-executable entertainment tools playable directly via the CLI environment.**



**## Scope of the Project**

**The scope of this project includes:**

**\* \*\*Terminal Engine Architecture:\*\* Implementing an interactive, frame-refreshed 2D grid matrix operating strictly within the terminal environment.**

**\* \*\*Game Mechanics \& Logic:\*\* Precise collision detection algorithms (wall boundary, self-collision, and item consumption), state management, and dynamic snake tail growth.**

**\* \*\*Input \& Control Handling:\*\* Non-blocking continuous keyboard listener loops mapped to navigational vectors.**

**\* \*\*Persistent Scoring Engine:\*\* Local file storage for managing real-time score tracking and historical high scores across game sessions.**



**## High-Level Features**

**\* \*\*Interactive Command-Line Interface:\*\* Zero-GUI execution using terminal rendering modules.**

**\* \*\*Real-time Collision Engine:\*\* Frame-by-frame coordinate mapping for self-intersection and border checks.**

**\* \*\*Dynamic Score Tracking:\*\* Automated score increments with dynamic movement speed scaling.**

**\* \*\*Modularity and Extensibility:\*\* Clean package structure separated into engine core, entity models, input controllers, and persistent state handlers.**

