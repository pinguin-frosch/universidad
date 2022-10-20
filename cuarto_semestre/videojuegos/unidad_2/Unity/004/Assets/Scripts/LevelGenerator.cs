using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LevelGenerator : MonoBehaviour
{
    public float MinimumDistance;
    public Transform PlayerTransform;
    public Transform LevelStart;
    public GameObject[] GameParts;
    public Transform endPosition;

    void Update()
    {
        if (Vector2.Distance(PlayerTransform.position, endPosition.position) < MinimumDistance)
        {
            addNextLevel();
        }
    }

    void addNextLevel()
    {
        // Obtener siguiente parte del nivel
        GameObject nextLevel = GameParts[Random.Range(0, GameParts.Length)];

        // Crear la parte del nivel en la escena
        Transform newEndPosition = Instantiate(nextLevel, endPosition.position, Quaternion.identity).transform;

        // Actualizar la posición final
        endPosition.position = newEndPosition.Find("EndPosition").position;
    }
}
