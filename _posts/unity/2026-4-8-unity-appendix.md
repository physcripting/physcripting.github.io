---
title: "Appendix"
author: PSK
date: 2026-04-17 08:10:00 +0800
categories: [eDocuments, Unity]
math: true
render_with_liquid: false
---

## 3.1 Introduction
It will provide useful tips and commands to work on unity. 

## 3.2 3D GrameObjects
* **Zooming**: 
	- After selecting any object press `F` to zoom 
	- Use the scroll wheel or trackpad to get to a good distance.  
* **Orbit around view**: Select object in `Scene view`  then Hold `Alt` and `left-click` and drag with your mouse to orbit around the object. 
* **blocking the old  input API** (`Input.GetKeyDown`). It is not about physics or Rigidbody. It is only about input handling mismatch.
1. Option 1: **Enable BOTH input systems**- Steps
	- Go to Edit → Project Settings
	- Click Player
	- Scroll to Other Settings
	- Find Active Input Handling
	- Change it to: `Both`
	- Click `Apply` to Restart Unity. You code should work
```csharp
if (Input.GetKeyDown(KeyCode.Space))
{
    myRigidbody.velocity = Vector2.up * 10;
}
```

2. Option 2: **Use New Input System Properly**- If you want to stay modern, replace your input code:
	- Add this at the top `using UnityEngine.InputSystem;`
	- update code to for using space bar key
```csharp
void Update()
{
    if (Keyboard.current.spaceKey.wasPressedThisFrame)
    {
        myRigidbody.velocity = Vector2.up * 10;
    }
}
```
