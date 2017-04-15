package com.example.android.hospitalmanagement;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class SignInActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_in);

        Button sign_in_doctor = (Button)findViewById(R.id.btn_signin_doctor);
        sign_in_doctor.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent doctor_intent = new Intent(SignInActivity.this, DoctorActivity.class);
                startActivity(doctor_intent);
            }
        });

        Button sign_in_patient = (Button)findViewById(R.id.btn_signin_patient);
        sign_in_patient.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent doctor_intent = new Intent(SignInActivity.this, PatientActivity.class);
                startActivity(doctor_intent);
            }
        });

        TextView sign_up = (TextView)findViewById(R.id.link_signup);
        sign_up.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent sign_up_intent = new Intent(SignInActivity.this, SignUpActivity.class);
                startActivity(sign_up_intent);
            }
        });

    }

}
