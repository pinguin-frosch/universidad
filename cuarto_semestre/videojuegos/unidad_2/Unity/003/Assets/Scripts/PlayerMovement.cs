using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    private float MoveSpeed = 10;
    private float JumpSpeed = 700;
    private bool isGrounded = false;
    private Vector3 startPosition = new Vector3(-13, -3, 0);
    private int attempts = 1;

    private float move;
    private Rigidbody2D rb;
    
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        rb.gravityScale = 3;
    }

    void Update()
    {
        move = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(move * MoveSpeed, rb.velocity.y);

        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            rb.AddForce(new Vector2(rb.velocity.x, JumpSpeed));
        }

        if (transform.position.y < -50 || transform.position.y > 50)
        {
            killPlayer();
        }
    }

    void killPlayer()
    {
        rb.velocity = new Vector2(0, 0);
        rb.gravityScale = 3;
        JumpSpeed = 700;
        transform.position = startPosition;
        attempts += 1;
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.gameObject.CompareTag("GravityPad"))
        {
            rb.gravityScale *= -1;
            JumpSpeed *= -1;
        }
        if (other.gameObject.CompareTag("Spike"))
        {
            killPlayer();
        }
        if (other.gameObject.CompareTag("GravityPortal"))
        {
            rb.gravityScale = 3;
            JumpSpeed = 700;
        }
        if (other.gameObject.CompareTag("InverseGravityPortal"))
        {
            rb.gravityScale = -3;
            JumpSpeed = -700;
        }
        if (other.gameObject.CompareTag("YellowOrb"))
        {
            rb.AddForce(new Vector2(rb.velocity.x, JumpSpeed * 1.5f));
        }
    }

    void OnCollisionEnter2D(Collision2D other)
    {
        if (other.gameObject.CompareTag("Ground"))
        {
            isGrounded = true;
        }
    }

    void OnCollisionExit2D(Collision2D other)
    {
        if (other.gameObject.CompareTag("Ground"))
        {
            isGrounded = false;
        }
    }
}
