---
title: "Chapter 4: Simple 3D Coin Collction Game"
author: PSK
date: 2026-03-17 14:10:00 +0800
categories: [eDocuments, Unity]
math: true
render_with_liquid: false
---

## 4.1 Introduction
This chapter teaches you how to build a very basic 3D game where a player moves around and collects coins. It introduces the most important Unity concepts in a hands-on way.  By the end, you will understand:
* Unity interface basics
* GameObjects and components
* Materials and visual design
* Prefabs and procedural spawning
* Player movement with physics
* Camera control
* Collision detection and scoring

## 4.2 Creating New Project 
This step sets in Unity Hub up your workspace where your game will be created. 
* Select **New Project** to begin creating a project.
* Choose **3D (Core)** template, which is optimized for developing 3D games.
* Name your project (for example, `CoinCollector`)
* Disable Version Control (optional). 
* Click **Create** to generate the project.

## 4.3 Creating the Game Environment 
### 4.3.1 Ground Object
* Right-click in `Hierarchy → 3D Object → Cube`
* Rename to `Ground`
* Set Transform:
	- `Position: (0, 0, 0)`
	- `Scale: (20, 1, 20)`
### 4.3.2 Player Object
* `Right-click → 3D Object → Cube`
* Rename to `Player`
* Set Position:
	- (0, 1, 0) (on top of ground)

## 4.4 Adding Materils
### 4.4.1 Create Materials Folder
Keeps your project organized
* Right-click at Project  `Create → Folder` and name it `Materials`
### 4.4.2 Create and Apply Materials
We will create three materils by Right-click `Create → Material`
* Ground → Green (grass-like)
* Player → Red : 
* Coin → Yellow/Gold (high smoothness)
* Drag material onto objects in Scene
## 4.5 Creating the Coin System
### 4.5.1 Create Coin Object
* Create Cube → rename Coin
* Scale to (0.5, 0.5, 0.5)
* Assign coin material
### 4.5.2 Convert to Prefab
Prefac is a gameobject with present value
* Create folder → Prefabs
* Drag Coin into Prefabs folder
* Delete coin from scene through Right-click in Hierachy
## 4.6 Coin Spawner Script
* Create empty GameObject:
* Name: `CoinSpawner`
### 4.6.1 Script: CoinSpawner.cs
This script automatically creates many coins randomly and place  them randomly on the ground.

```csharp
using UnityEngine;

public class CoinSpawner : MonoBehaviour
{
    [SerializeField] private GameObject coinPrefab;
    [SerializeField] private BoxCollider groundCollider;
    [SerializeField] private int coinAmount = 10;

    void Start()
    {
        for (int i = 0; i < coinAmount; i++)
        {
            Vector3 startPos = GetRandomPoint();
            Instantiate(coinPrefab, startPos, Quaternion.identity);
        }
    }

    Vector3 GetRandomPoint()
    {
        Bounds bounds = groundCollider.bounds;

        float x = Random.Range(bounds.min.x, bounds.max.x);
        float z = Random.Range(bounds.min.z, bounds.max.z);

        return new Vector3(x, 1f, z);
    }
}
```
### 4.6.2 Setup in Inspector
* Assign Coin Spawner Script:
	- Coin Prefab: Drag and drop the `coin` from Prefab into Coin Prefab of `Coin Spawner (Script).
	- Ground Collider: drag the ground box and drop into Ground Collider
	- Set Coin Amount to 20. 
## 4.7 Player Movement
 
### 4.7.1 Add Rigidbody
Adds physics so the player can move naturally
* Select Player → Add Component → Rigidbody
### 4.7.2 Script: PlayerHandler.cs
Click Add component in the Player and add new scropt `PlayerHandler`
Allows movement using keyboard keys.

```csharp
using UnityEngine;

public class PlayerHandler : MonoBehaviour
{
    private Rigidbody rb;
    [SerializeField] private float speed = 10f;
    private int points = 0;

    void Awake()
    {
        rb = GetComponent<Rigidbody>();
    }

    void FixedUpdate()
    {
        float h = Input.GetAxis("Horizontal");
        float v = Input.GetAxis("Vertical");

        Vector3 movement = new Vector3(h, 0, v);

        rb.MovePosition(rb.position + movement * speed * Time.fixedDeltaTime);
    }

    public void IncreasePoints()
    {
        points++;
        Debug.Log("Points: " + points);
    }
}
```

## 4.8 Camera Follow System
Click Add Component and add camera and call it `FollowPlayer`
Makes the camera follow the player smoothly.
* `Script: FollowPlayer.cs`

```csharp
using UnityEngine;

public class FollowPlayer : MonoBehaviour
{
    [SerializeField] private Transform target;
    [SerializeField] private Vector3 offset;
    [SerializeField] private float smoothTime = 0.25f;

    private Vector3 velocity;

    void FixedUpdate()
    {
        Vector3 targetPosition = target.position + offset;

        transform.position = Vector3.SmoothDamp(
            transform.position,
            targetPosition,
            ref velocity,
            
            smoothTime
        );

        transform.LookAt(target);
    }
    public void IncreasePoints()
    {
        points++;
    }
}
```

**Setup**:
* Camera Target → Player
* Offset → (0, 10, -10)
## 4.9 Coin Collection Logic
### 4.9.1 Enable Trigger
Allows player to pass through coins and detect overlap.

* Open Coin Prefab
* Check "Is Trigger" in BoxCollider
### 4.9.2 Script: Coin.cs
Detects when player touches coin and remove and updates score.

```csharp
using UnityEngine;

public class Coin : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        PlayerHandler player = other.GetComponent<PlayerHandler>();

        if (player != null)
        {
            player.IncreasePoints();
            Destroy(gameObject);
        }
    }
}
```

## 4.10 Testing the Game
Run your game and check if everything works.
* Press ▶ Play:
	- Move using WASD or Arrow Keys
	- Collect coins
	- Watch coins disappear and score increase

## 4.11 Debugging Tip
To view private variables such as hidden values like score:
* Click three dots in Inspector
* Select Debug Mode