using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMovement : MonoBehaviour
{
    public Transform PlayerTransform;

    void Update()
    {
        transform.position = new Vector3(PlayerTransform.position.x + 6, PlayerTransform.position.y, -1);
    }
}
