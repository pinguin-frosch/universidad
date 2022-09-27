using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Move : MonoBehaviour
{
    Rigidbody2D rb;
    int speed;
    //variable para comprobar si toco el piso
    public bool TouchFloor;
    public LayerMask IsFloor;
    public Transform Checker;
    public float RadioChecker;
    //GameObject objectFind;
    // Start is called before the first frame update
    void Start()
    {
        //indicando que utilizamos el componente Rigidbody2D
        rb = GetComponent<Rigidbody2D>();
        speed = 10;       
    }

    // Update is called once per frame
    void Update()
    {
        //movimiento horizontal
        float h = Input.GetAxis("Horizontal");
        //movimiento vertical
        float v = Input.GetAxis("Vertical");
        //mover horizontal y vertical
        //rb.velocity = new Vector2(h,v)*speed;
        //mover solamente horizontal
        rb.velocity = new Vector2(h*speed,rb.velocity.y);
        
        if(Input.GetButtonDown("Jump") && TouchFloor) {
            rb.AddForce(new Vector2(0,5)*5000);
        }
        TouchFloor = Physics2D.OverlapCircle(Checker.position, RadioChecker, IsFloor);
    }
    private void OnTriggerEnter2D(Collider2D collision) {
        if(collision.gameObject.CompareTag("Ball")){
            collision.gameObject.SetActive(false);
        }
    }
}
