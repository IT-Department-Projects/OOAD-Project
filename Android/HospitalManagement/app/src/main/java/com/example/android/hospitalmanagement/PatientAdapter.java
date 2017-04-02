package com.example.android.hospitalmanagement;

import android.content.Context;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by harsh on 3/4/17.
 */

public class PatientAdapter extends ArrayAdapter<Patient> {

    public PatientAdapter(Context context, ArrayList<Patient> patient)
    {
        super(context,0,patient);
    }

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        View listItemView = convertView;

        if(listItemView==null)
        {
            listItemView = LayoutInflater.from(getContext()).inflate(R.layout.patient_list_item,parent,false);
        }

        Patient currentPatient = getItem(position);

        TextView nameTextView = (TextView) listItemView.findViewById(R.id.name_text_view);
        nameTextView.setText(currentPatient.getPatientname());

        TextView deptTextView = (TextView) listItemView.findViewById(R.id.dept_text_view);
        deptTextView.setText(currentPatient.getPatientdept());

        TextView hospitalTextView = (TextView) listItemView.findViewById(R.id.hospital_text_view);
        hospitalTextView.setText(currentPatient.getPatienthospital());

        ImageView imageView = (ImageView) listItemView.findViewById(R.id.patient_image);
        imageView.setImageResource(currentPatient.getPatientimage());

        return listItemView;
    }
}
