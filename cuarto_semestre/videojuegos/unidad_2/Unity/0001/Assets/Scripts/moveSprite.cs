using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class moveSprite : MonoBehaviour
{
    Rigidbody2D rb;
    private int speed;
    private int v_speed;
    public Transform Checker;
    public float RadioChecker;
    public LayerMask IsFloor;
    private int jumps;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        speed = 10;
        v_speed = 500;
        jumps = 1;
    }

    void Update()
    {
        float h = Input.GetAxis("Horizontal");
        float v = Input.GetAxis("Vertical");
        rb.velocity = new Vector2(h * speed, rb.velocity.y);

        if (Input.GetButtonDown("Jump") && jumps > 0)
        {
            rb.AddForce(new Vector2(0, 1) * v_speed);
            jumps -= 1;
        }

        if (Physics2D.OverlapCircle(Checker.position, RadioChecker, IsFloor))
        {
            jumps = 1;
        }
    }

    void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.CompareTag("Star"))
        {
            collision.gameObject.SetActive(false);
        }

    }
}
