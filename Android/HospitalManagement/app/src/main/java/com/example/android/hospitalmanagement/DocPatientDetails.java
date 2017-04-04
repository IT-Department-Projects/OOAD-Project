package com.example.android.hospitalmanagement;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

/**
 * Created by harsh on 4/4/17.
 */

public class DocPatientDetails extends AppCompatActivity {

    private String name,mobno,fileno,insurance;
    private int image;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.doc_patient_details);

        //Pull data from firebase

        TextView nameTextView = (TextView) findViewById(R.id.name);
        nameTextView.setText(name);

        TextView mobnoTextView = (TextView) findViewById(R.id.mobNo);
        nameTextView.setText(mobno);

        TextView filenoTextView = (TextView) findViewById(R.id.fileno);
        nameTextView.setText(fileno);

        TextView insuranceTextView = (TextView) findViewById(R.id.insurance);
        nameTextView.setText(insurance);

        Button prescriptionButton = (Button) findViewById(R.id.prescription);
        prescriptionButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent prescriptionIntent = new Intent(DocPatientDetails.this,DoctorPrescription.class);
                startActivity(prescriptionIntent);
            }
        });
    }
}
