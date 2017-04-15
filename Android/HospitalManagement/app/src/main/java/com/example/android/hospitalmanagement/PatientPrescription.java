package com.example.android.hospitalmanagement;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

/**
 * Created by harsh on 4/4/17.
 */

public class PatientPrescription extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.patient_prescription);

        TextView subject = (TextView) findViewById(R.id.subject);
        //Set subject text view with detials from firebase

        TextView prescription = (TextView) findViewById(R.id.prescription);
        //Set prescription text view with details from firebase

    }
}
