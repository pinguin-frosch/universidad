using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LevelGenerator : MonoBehaviour
{
    public float MinimumDistance;
    public Transform PlayerTransform;
    public Transform LevelStart;
    public GameObject[] GameParts;
    public GameObject FinalPoint;
    public Transform endPosition;
    public int TotalLevels;

    private bool gameOver = false;

    void Update()
    {
        if (TotalLevels > 0)
        {
            if (Vector2.Distance(PlayerTransform.position, endPosition.position) < MinimumDistance)
            {
                TotalLevels -= 1;
                addNextLevel();
            }
        }
        else if (!gameOver)
        {
            gameOver = true;
            Instantiate(FinalPoint, endPosition.position, Quaternion.identity);
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
