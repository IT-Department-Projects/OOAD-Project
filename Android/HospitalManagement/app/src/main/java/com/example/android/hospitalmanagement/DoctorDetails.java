package com.example.android.hospitalmanagement;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.widget.Button;
import android.widget.EditText;

/**
 * Created by harsh on 4/4/17.
 */

public class DoctorDetails extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.doctor_details);

        EditText name = (EditText) findViewById(R.id.name);
        String docname = name.getText().toString();

        //Set up button to import pictures from gallery or take a picture from camera

        EditText hospital = (EditText) findViewById(R.id.hospital);
        String dochospital = name.getText().toString();

        EditText mobno = (EditText) findViewById(R.id.mobNo);
        String docmobno = name.getText().toString();

        EditText dept = (EditText) findViewById(R.id.department);
        String docdept = name.getText().toString();

        Button submit = (Button) findViewById(R.id.submit);
        //check conditions and upload to database and go to doctor activity
    }
}
