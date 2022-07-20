/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package com.rogueanovi.ejercicioclasesherencia;

/**
 *
 * @author ROGUEANOVI
 */
public class EjercicioClasesHerencia {

  public static void main(String[] args) {

    Cliente cliente = new Cliente();
    cliente.setEdad(50);
    cliente.setNombre("Rafael");
    cliente.setTelefono("+57 938458784");
    cliente.setCredito(true);
    System.out.println("Nombre: " + cliente.getNombre() + "     Edad: " + cliente.getEdad() + "     Telefono: " + cliente.getTelefono() + "    Credito: " + cliente.getCredito());
  
    Trabajador trabajador = new Trabajador();
    trabajador.setEdad(30);
    trabajador.setNombre("Ana MAria");
    trabajador.setTelefono("+57 2305958684");
    trabajador.setSalario(2500000);

    System.out.println("Nombre: " + trabajador.getNombre() + "     Edad: " + trabajador.getEdad() + "     Telefono: " + trabajador.getTelefono() + "    Credito: " + trabajador.getSalario());

  }
}

class Persona {

  public Persona() {
  }

  private int edad;
  private String nombre;
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

class Cliente extends Persona {

  private boolean credito;

  /**
   * @return the credito
   */
  public boolean getCredito() {
    return credito;
  }

  /**
   * @param credito the credito to set
   */
  public void setCredito(boolean credito) {
    this.credito = credito;
  }

}

class Trabajador extends Persona{
  
  private float salario;

  /**
   * @return the salario
   */
  public float getSalario() {
    return salario;
  }

  /**
   * @param salario the salario to set
   */
  public void setSalario(float salario) {
    this.salario = salario;
  }
  
}
