using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

public class transform : MonoBehaviour
{
    public float moveSpeed = 5f;
    public bool reset = false;
    void Update ()
    {
		  transform.Translate(Vector3.down * moveSpeed * Time.deltaTime);
      
      if (Input.GetKey("space"))
      {
        if (reset == true) {
             SceneManager.LoadScene("flappyBird");
             Time.timeScale = 1;
             reset = false;
         }
        transform.Translate(Vector3.forward * Time.deltaTime*2);
      }else{
        transform.Translate(Vector3.back * Time.deltaTime*2);
      }
    }

    void OnTriggerEnter(Collider collider)
    {
         Time.timeScale = 0;
         reset = true;
    }
}
