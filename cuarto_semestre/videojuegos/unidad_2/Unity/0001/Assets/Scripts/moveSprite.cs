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
    public bool TouchFloor;
    public LayerMask IsFloor;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        speed = 10;
        v_speed = 500;
    }

    void Update()
    {
        float h = Input.GetAxis("Horizontal");
        float v = Input.GetAxis("Vertical");
        rb.velocity = new Vector2(h * speed, rb.velocity.y);

        TouchFloor = Physics2D.OverlapCircle(Checker.position, RadioChecker, IsFloor);

        if (Input.GetButtonDown("Jump") && TouchFloor) {
            rb.AddForce(new Vector2(0, 1) * v_speed);
        }
    }

    void OnTriggerEnter2D(Collider2D collision) {
        if (collision.gameObject.CompareTag("Star")) {
            // Debug.Log(collision);
            collision.gameObject.SetActive(false);
        }
    }
}
