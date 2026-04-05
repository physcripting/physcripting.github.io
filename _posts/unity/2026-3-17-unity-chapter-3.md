---
title: "Chapter 3: 2D Game with C Shape"
author: PSK
date: 2026-03-17 14:10:00 +0800
categories: [eDocuments, Unity]
math: true
render_with_liquid: false
---

## 2.1 Introduction
In this chapter, you will learn how to create a simple 2D game inspired by Flappy Bird using a Unity template. In this game, a bird navigates through obstacles, and a scoring system tracks each successful pass.

This tutorial provides a step-by-step introduction to game development in Unity, covering everything, including the user interface to lines of **C Shape** code.

## 2.2 Creating New Project 
In Unity Hub, 
* Click New Project to begin creating a new project.
* Select 2D (Core) template. This template provides a basic setup with configurations optimized for developing 2D games.
* Enter a name for your project, for example, `Flarpy Blorb`, choose a location to save it, and click Create.

Once the project opens, you are ready to begin building your game.
## 2.3 Unity User Interface
In this section, you will become familiar with the default Unity user interface in windows visual studio. As you explore the different panels, you will also begin adding elements to your scene, such as displaying a character (e.g., a bird) on the screen.
When Unity opens, the default layout is divided into several key panels (Figure 1):

* **Project Panel**: Located at the bottom of the screen, the Project panel contains all the assets used in our game, including:
    - Sprites (images)
    - Sound effects
    - Scripts
    - Tiles and fonts

Some of these assets will be created within Unity, while others can be imported from external sources. For example, you can drag and drop image files.

* **Hierarchy Panel**: The Hierarchy panel displays all the objects currently present in the active scene. A scene typically represents a level or environment in your game.

Any object you add to your game—such as characters, cameras, or background elements—will appear in this panel.

We will introduce:
* Scene Window (for designing the world)
* Game Window (what the player sees)
* Inspector Panel (edit properties)

