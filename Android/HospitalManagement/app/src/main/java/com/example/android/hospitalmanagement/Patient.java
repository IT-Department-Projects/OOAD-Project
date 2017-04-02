package com.example.android.hospitalmanagement;

/**
 * Created by harsh on 3/4/17.
 */

public class Patient {
    private String patientname;
    private String patientdept;
    private String patienthospital;
    private int patientimage;

    public Patient(String name,String dept, String hospital,int image)
    {
        patientname=name;
        patientdept=dept;
        patienthospital=hospital;
        patientimage=image;
    }

    public String getPatientname() {return patientname;}
    public String getPatientdept() {return patientdept;}
    public String getPatienthospital() {return patienthospital;}
    public int getPatientimage() {return patientimage;}

}
