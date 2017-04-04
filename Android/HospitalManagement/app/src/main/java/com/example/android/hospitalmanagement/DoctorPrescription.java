package com.example.android.hospitalmanagement;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.widget.EditText;

/**
 * Created by harsh on 4/4/17.
 */

public class DoctorPrescription extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.doc_prescription);

        EditText subjectet = (EditText) findViewById(R.id.subject_edit_text);
        String subject = subjectet.getText().toString();

        EditText prescriptionet = (EditText) findViewById(R.id.prescription_edit_text);
        String prescription = prescriptionet.getText().toString();

        //Set button to add details to databse and return to doctor activity
    }
}
