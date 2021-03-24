import java.util.Scanner;

public class MolConversion{
    static double mole = 602214000000000000000000.0; // atoms in a mole.
    static double atoms;
    static double mass;
    static double mols;
    // write variables for all elements and their AMU 
    public static Scanner input = new Scanner(System.in);
    public static void main(String[] args) {
        //System.out.println(atomsToMass(195.084,4840000000000000000000.0));
        //System.out.println(massToAtoms(87.62,.08));
        System.out.println(22.99+1.008+12.011+(3*16));
        System.out.println((.300*84.009*1*1)/(1*1*58.443));
        System.out.println(.170);
    }
    public static double molsToAtoms(double convertMols){
        atoms = mole*convertMols;
        return atoms;
    }
    
    public static double atomsToMols(double convertAtoms){
        mols = convertAtoms/mole;
        return mols;
    }
    public static double molsToMass(double molarMass, double mols){
        mass = molarMass*mols;
        return mass;
    }
    public static double atomsToMass(double molarMass, double atom){
        mass = molarMass*atomsToMols(atom);
        return mass;
    }
    
    public static double massToAtoms(double amu, double massx){
        atoms = (massx/amu)*mole;
        return atoms;
    }
}