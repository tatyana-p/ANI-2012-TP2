using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{
    public float x = 0.2f;
    public float y = 0.2f;
    public float z = 0.2f;

    public void PlayGame()
    {
        GameObject playButton = GameObject.Find("PlayButton");
        playButton.transform.localScale += new Vector3(x, y, z);

        SceneManager.LoadScene(1);
    }

    public void QuitGame()
    {
        GameObject quitButton = GameObject.Find("QuitButton");

        quitButton.transform.localScale += new Vector3(x, y, z);

        Application.Quit();
    }
    public void OptionGame()
    {
        GameObject optionButton = GameObject.Find("OptionButton");

        if (optionButton)
        {
            optionButton.transform.localScale += new Vector3(x, y, z);
        }
    }
}
