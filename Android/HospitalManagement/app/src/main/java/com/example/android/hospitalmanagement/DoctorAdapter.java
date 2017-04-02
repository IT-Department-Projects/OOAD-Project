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

public class DoctorAdapter extends ArrayAdapter<Doctor> {

    public DoctorAdapter(Context context, ArrayList<Doctor> doctor)
    {
        super(context,0,doctor);
    }

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        View listItemView = convertView;

        if(listItemView==null)
        {
            listItemView = LayoutInflater.from(getContext()).inflate(R.layout.doctor_list_item,parent,false);
        }

        Doctor currentDoctor = getItem(position);

        TextView nameTextView = (TextView) listItemView.findViewById(R.id.name_text_view);
        nameTextView.setText(currentDoctor.getDocname());

        TextView timeTextView = (TextView) listItemView.findViewById(R.id.time_text_view);
        timeTextView.setText(currentDoctor.getDoctime());

        ImageView imageView = (ImageView) listItemView.findViewById(R.id.doctor_image);
        imageView.setImageResource(currentDoctor.getDocimage());

        return listItemView;
    }
}
