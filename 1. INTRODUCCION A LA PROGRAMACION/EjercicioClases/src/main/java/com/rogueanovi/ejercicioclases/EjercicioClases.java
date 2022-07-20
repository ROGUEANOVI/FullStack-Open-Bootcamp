/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.rogueanovi.ejercicioclases;

/**
 *
 * @author ROGUEANOVI
 */
public class EjercicioClases {

  public static void main(String[] args) {
    Persona persona = new Persona();
    persona.setEdad(28);
    persona.setNombre("Ovidio");
    persona.setTelefono("+57 12345678");
    
    System.out.println("Nombre: " + persona.getNombre() + "     Edad: " + persona.getEdad() + "     Telefono: " + persona.getTelefono() );
  }
    
}

class Persona{

  public Persona() {
  }

  private int edad;
  private String  nombre;
  private String telefono;

  /**
   * @return the edad
   */
  public int getEdad() {
    return edad;
  }

  /**
   * @param edad the edad to set
   */
  public void setEdad(int edad) {
    this.edad = edad;
  }

  /**
   * @return the nombre
   */
  public String getNombre() {
    return nombre;
  }

  /**
   * @param nombre the nombre to set
   */
  public void setNombre(String nombre) {
    this.nombre = nombre;
  }

  /**
   * @return the telefono
   */
  public String getTelefono() {
    return telefono;
  }

  /**
   * @param telefono the telefono to set
   */
  public void setTelefono(String telefono) {
    this.telefono = telefono;
  }
    
}