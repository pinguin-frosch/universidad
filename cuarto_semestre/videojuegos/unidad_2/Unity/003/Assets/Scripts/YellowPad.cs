using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class YellowPad : MonoBehaviour
{
    public bool isActive;

    private void OnCollisionEnter2D(Collision2D other) {
        if (other.gameObject.CompareTag("Player"))
        {
            isActive = false;
        }
    }
}
