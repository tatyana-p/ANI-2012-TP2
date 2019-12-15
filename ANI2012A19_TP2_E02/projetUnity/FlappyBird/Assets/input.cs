using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class input : MonoBehaviour
{
        private Animator anim;    
    // Start is called before the first frame update
    void Start ()
    {
      anim = GetComponent<Animator> ();
    }

    // Update is called once per frame
    void Update()
    {
      if (Input.GetKey("space"))
      {
        anim.GetComponent<Animator>().enabled = false;
        anim.GetComponent<Animator>().enabled = true;
        anim.Play("up");
        anim.SetBool("updown", true);
      }else if (Input.GetKeyUp(KeyCode.Space)){
        anim.GetComponent<Animator>().enabled = false;
        anim.GetComponent<Animator>().enabled = true;
        anim.Play("down");
        anim.SetBool("updown", true);
      }else{
        anim.SetBool("updown", false);
      }
    }
}
