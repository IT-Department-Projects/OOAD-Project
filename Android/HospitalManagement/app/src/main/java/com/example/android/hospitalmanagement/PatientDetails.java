package com.example.android.hospitalmanagement;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.widget.Button;
import android.widget.EditText;

/**
 * Created by harsh on 4/4/17.
 */

public class PatientDetails extends AppCompatActivity{

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.patient_details);

        EditText name = (EditText) findViewById(R.id.name);
        String patientname = name.getText().toString();

        //Set up button to import pictures from gallery or take a picture from camera

        EditText mobno = (EditText) findViewById(R.id.mobNo);
        String patientmobno = name.getText().toString();


        EditText address = (EditText) findViewById(R.id.address);
        String patientaddress = name.getText().toString();

        EditText insurance = (EditText) findViewById(R.id.insurance);
        String patientinsurance = name.getText().toString();

        Button submit = (Button) findViewById(R.id.submit);
        //check conditions and upload to database and go to patient activity
    }
}
