package com.example.android.hospitalmanagement;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import org.w3c.dom.Text;

/**
 * Created by harsh on 4/4/17.
 */

public class PatientDocDetails extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.patient_doc_details);

        ImageView photo = (ImageView) findViewById(R.id.image);
        //Set imageresource to photo from firebase.

        TextView name = (TextView) findViewById(R.id.name);
        //Set text to name from firebase

        Button button = (Button) findViewById(R.id.fixappointment);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //check the radio button and fix the appointment
            }
        });
    }
}
