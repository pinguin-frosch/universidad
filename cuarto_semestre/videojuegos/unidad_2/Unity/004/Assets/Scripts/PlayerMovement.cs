using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    private Rigidbody2D rb;
    public int Speed;
    public int JumpSpeed;
    public Transform GroundCheckTransform;
    public float GroundCheckRadius;
    public LayerMask GroundMask;
    public Vector2 StartingPosition;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        float movement = Input.GetAxis("Horizontal") * Speed;
        rb.velocity = new Vector2(movement, rb.velocity.y);

        if (Input.GetButtonDown("Jump") && onGround())
        {
            rb.velocity = Vector2.zero;
            rb.AddForce(Vector2.up * JumpSpeed, ForceMode2D.Impulse);
        }
    }

    public void resetPosition()
    {
        rb.velocity = Vector2.zero;
        transform.position = StartingPosition;
    }

    bool onGround()
    {
        return Physics2D.OverlapCircle(GroundCheckTransform.position, GroundCheckRadius, GroundMask);
    }
}
