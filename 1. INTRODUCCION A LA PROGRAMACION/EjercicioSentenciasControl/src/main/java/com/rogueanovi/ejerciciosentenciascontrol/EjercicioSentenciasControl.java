/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.rogueanovi.ejerciciosentenciascontrol;

/**
 *
 * @author ROGUEANOVI
 */
public class EjercicioSentenciasControl {

  public static void main(String[] args) {
    int numeroIf = 0;
    // CODICIONALES    
    if (numeroIf > 0) {
      System.out.println("Numero positivo");
    } 
    else if(numeroIf < 0){
      System.out.println("Numero negativo");
    }
    else {
      System.out.println("El numero es 0");
    }
    
    int numeroWhile = 0;
    // WHILE
    while (numeroWhile < 3) {
      numeroWhile = numeroWhile + 1;
      System.out.println(numeroWhile);
    }
    
    int numeroDoWhile = 0;
    // DO WHILE
    do {      
      numeroDoWhile = numeroDoWhile + 1;
      System.out.println(numeroDoWhile);
    } while (numeroDoWhile > 3);
    
    
    // FOR
    for (int numeroFor = 0; numeroFor <= 3; numeroFor++) {
      System.out.println(numeroFor);
    }
    
    String estacion = "CALIENTE";
    // SWITCH CASE
    switch (estacion) {
      case "VERANO":
        System.out.println("Estamos en VERANO");
        break;
      case "INVIERNO":
        System.out.println("Estamos en INVIERNO");
        break;
      case "OTONO":
        System.out.println("Estamos en OTONO");
        break;
      case "PRIMAVERA":
        System.out.println("Estamos en PRIMAVERA");
        break;
      default:
        System.out.println("Esto NO es una ESTACION");;
    }
  }
}
