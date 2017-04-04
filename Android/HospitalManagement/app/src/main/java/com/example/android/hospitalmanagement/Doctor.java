package com.example.android.hospitalmanagement;

/**
 * Created by harsh on 3/4/17.
 */

public class Doctor {

    private String docname;
    private String doctime;
    private int docimage;

    public Doctor(String name,String time, int image)
    {
        docname=name;
        doctime=time;
        docimage=image;
    }

    public String getDocname() {return docname;}
    public String getDoctime() {return doctime;}
    public int getDocimage() {return docimage;}
}

