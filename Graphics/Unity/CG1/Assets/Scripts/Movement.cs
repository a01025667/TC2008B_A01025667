using UnityEngine;

public class Movement : MonoBehaviour
{
    [SerializeField] GameObject[] wheels; // Arreglo para guardar las ruedas 
    [SerializeField] float moveSpeed = 5f; // Velocidad de movimiento
    public Vector3 targetPosition; // Punto de destino del carro

    void Update()
    {
        MoveCar(); // Se llama a la función para mover el carro
    }

    void MoveCar()
    {
        Vector3 direction = targetPosition - transform.position; // Se calcula la dirección del carro hacia el punto de destino

        
        if (direction.magnitude > 0.01f) // Se verifica que la distancia entre el carro y el punto de destino sea mayor a 0.01
        {
            transform.Translate(Vector3.forward * moveSpeed * Time.deltaTime, Space.World); // Se mueve el carro hacia adelante

            foreach (GameObject wheel in wheels) // Se recorre el arreglo de ruedas
            {
                wheel.transform.Translate(Vector3.forward * moveSpeed * Time.deltaTime, Space.World); // Se mueven las ruedas hacia adelante
            }
        }
    }
    void LateUpdate()
    {
        RotateWheels(); // Se llama a la función para rotar las ruedas
    }

    void RotateWheels()
    {
        foreach (GameObject wheel in wheels) // Se recorre el arreglo de ruedas
        {
            wheel.transform.Rotate(Vector3.right, moveSpeed * Time.deltaTime * 100, Space.World); // Se rotan las ruedas
        }
    }
}
