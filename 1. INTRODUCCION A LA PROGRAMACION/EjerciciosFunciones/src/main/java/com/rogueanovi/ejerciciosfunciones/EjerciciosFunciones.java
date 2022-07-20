/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.rogueanovi.ejerciciosfunciones;

/**
 *
 * @author ROGUEANOVI
 */
public class EjerciciosFunciones {

    public static void main(String[] args) {
        int total;
        total = suma(2,4,6); 
        
        Coche miCoche = new Coche();
        miCoche.incrementaPuerta();
        System.out.println(miCoche.numeroPuertas);
    }
    
    public static int suma(int num1,int num2,int num3){
        int resultado = num1 + num2 + num3;
        return resultado;
    }
}

class Coche{
    public int numeroPuertas = 4;
    
    public void incrementaPuerta(){
        this.numeroPuertas++;
    }
    
}